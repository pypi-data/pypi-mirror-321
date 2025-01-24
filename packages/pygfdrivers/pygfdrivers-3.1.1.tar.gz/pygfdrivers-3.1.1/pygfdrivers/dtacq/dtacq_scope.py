from collections import defaultdict
from functools import cached_property
from time import perf_counter, sleep
from typing import Dict, List

import numpy as np
from acq400_hapi.acq400 import STATE, factory
from gf_data_models.dtacq.scope import DtacqScopeModel

from pygfdrivers.common.base_scope import BaseScope
from pygfdrivers.common.util.utilities import has_prop, int_key_to_str
from pygfdrivers.dtacq.acq400_commands.acquire import DtacqAcquire
from pygfdrivers.dtacq.acq400_commands.trigger import DtacqTrigger
from pygfdrivers.dtacq.site_modules.modules_map import modules_map
from pygfdrivers.dtacq.util.utilities import pv


class TIMEOUT:
    ARM = 10
    ABORT = 5
    DOWNLOAD = 10


class DtacqScope(BaseScope):
    def __init__(self, scope_config: DtacqScopeModel) -> None:
        super().__init__(scope_config)

    def init(self):
        try:
            self.connect()
        except Exception as e:
            self.log.error(f"Initializing DTACQ scope encountered error: {e}")
            self.is_connected = False

    def apply_configurations(self):
        self.log.info("Applying scope configurations...")

        try:
            # Ensure that the DTACQ is in idle state before applying configurations
            target_state = STATE.str(STATE.IDLE)

            if self.transient_state != target_state:
                self.log.debug(f"Scope in '{self.transient_state}' and not '{target_state}'.")
                self.abort()

            self.log.info("Applying capture configurations...")
            self.acquire.acq_srate = self.config.capture.acq_srate
            self.acquire.set_time_range(self.config.capture.time_pre, self.config.capture.time_post)
            self.acquire.acq_bit_res = self.ai_modules.bit_depth

            self.log.info("Applying trigger configurations...")
            self.trigger.trig_slope = self.config.trigger.trig_slope
            self.trigger.trig_source = self.config.trigger.trig_source

            self.log.info("Applying site channel configurations...")
            self.ai_modules.apply_site_config(self.config.active_sites, self.config.sites)

            self.log.info(f"Applying transient configurations...")
            try:
                self.carrier.configure_transient(
                    pre                 = self.acquire.acq_pre_samples,
                    post                = self.acquire.acq_post_samples,
                    sig_DX              = self.trigger.trig_source,
                    auto_soft_trigger   = 1 if self.acquire.acq_pre_samples > 0 else 0,
                    demux               = 1,
                    edge                = self.trigger.trig_slope
                )
            except Exception as e:
                self.log.error(f"Applying transient config encountered error: {e}")
                
            self.is_configured = True
            self.log.info("Finished applying scope configurations.")
        except Exception as e:
            self.log.error(f"Applying scope configurations encountered error: {e}.")
            self.is_configured = False

    def connect(self):
        try:
            # Function from pygfdrivers.dtacq to determine if ACQ2106 or some other acq400_commands
            self.carrier = factory(self.config.device.device_conn_str)
            self.motherboard = self.carrier.s0      # site 0 is always the motherboard

            # Determine the site locations of the different modules and create appropriate module objects
            site_type_dict = self.carrier.get_site_types()
            self.init_site_obj(site_type_dict)
            self.master_site = self.ai_modules.master_site

            # Max constants required by acq400_commands to configure memory and clock
            self.min_clock = self.ai_modules.min_srate
            self.max_clock = self.ai_modules.max_srate
            self.max_samples = self.ai_modules.max_samples

            # Initialize command class objects
            self.acquire = DtacqAcquire(self)
            self.trigger = DtacqTrigger(self)

            self.log.info(f"DTACQ SCOPE TYPE FOR SCOPE NAME ---- {self.name}")
            self.is_connected = True
        except Exception as e:
            self.log.info(f"DTACQ {self.name} failed to connect: {e}")
            self.is_connected = False

    def arm(self):
        self.log.info("Arming scope...")

        self.prep_shot()
        self.motherboard.set_knob('set_arm', True)

        # There is a slight delay between sending the arm command to the device
        # to when the status of the device is updated with the appropriate
        # status so we have to momentarily poll for it
        state = STATE.RUNPRE if self.acquire.acq_pre_samples > 0 else STATE.ARM
        self.is_armed = self.wait_for_state(STATE.str(state), TIMEOUT.ARM)
        self.log.info(f"{'Scope armed.' if self.is_armed else 'Scope failed to arm.'}")

    def abort(self):
        self.log.info("Aborting scope...")
        self.motherboard.set_knob('TIM_CTRL_LOCK', 0)
        self.motherboard.set_knob('TRANSIENT_SET_ABORT', 1)
        sleep(1)
        self.motherboard.set_knob('streamtonowhered', 'stop')
        self.motherboard.set_abort = 1

        success = self.wait_for_state(STATE.str(STATE.IDLE))
        self.is_aborted = not success
        self.log.info(f"{'Scope aborted.' if success else 'Scope failed to abort.'}")

    def prep_shot(self) -> None:
        self.log.debug("Preparing shot...")
        self.carrier.statmon.stopped.clear()
        self.carrier.statmon.armed.clear()

        self.clear_scope_info_data()
        self.last_shot_num = self.shot_num

        self.data = None
        self.is_armed = False
        self.is_aborted = False
        self.is_triggered = False
        self.is_downloaded = False

    def trigger_software(self):
        self.log.debug("Software triggering scope...")
        self.motherboard.set_knob('soft_trigger', 1)
        self.is_triggered = True

    def disconnect(self):
        if not self.is_connected:
            self.log.info(f"DTACQ {self.name} already disconnected.")
            return

        try:
            self.carrier.close()
            self.is_connected = False
            self.log.info("Disconnect attempt successful")
        except Exception as e:
            self.log.info(f"DTACQ {self.name} failed to disconnect: {e}")

    # ------------------------------------------------------------------------------------
    #  Read only methods
    # ------------------------------------------------------------------------------------

    @property
    def trigger_status(self) -> bool:
        # If we successfully triggered, our shot number should have increased.
        current_shot_num = self.shot_num
        trigger_status = (current_shot_num != self.last_shot_num)
        self.is_triggered = trigger_status
        return trigger_status

    @property
    def transient_state(self) -> str:
        _transient_state = pv(self.motherboard.get_knob("TRANS_ACT_STATE"))

        if '_' in _transient_state:
            _transient_state = _transient_state.replace('_', '')

        # _transient_state = STATE.str(self.scope.statmon.get_state())
        self.log.debug(f"transient_state: '{_transient_state}'")
        return _transient_state

    @property
    def shot_num(self) -> int:
        try:
            _shot_num = int(self.motherboard.get_knob('shot_complete'))
            self.log.debug(f"shot_num: '{_shot_num}'")
            return _shot_num
        except Exception as e:
            self.log.error(f"Querying shot number encountered error: {e}")

    @property
    def idn(self) -> str:
        return self.carrier.get_sys_info()

    @cached_property
    def serial_num(self) -> str:
        return self.motherboard.get_knob('SERIAL')

    @cached_property
    def model(self) -> str:
        return self.motherboard.get_knob('MODEL')

    @cached_property
    def nchan(self) -> int:
        return int(self.motherboard.get_knob('NCHAN'))

    @property
    def sys_temps(self) -> Dict:
        _sys_temps = defaultdict(float)
        sys_temps = self.motherboard.get_knob('SYS_TEMP').split(',')

        for sys_temp in sys_temps:
            sys, value = sys_temp.split('=')
            _sys_temps[sys] = float(value)

        return _sys_temps

    # ------------------------------------------------------------------------------------
    # Data Capture Methods
    # ------------------------------------------------------------------------------------

    def fetch_data(self) -> None:
        if self.is_triggered:
            self.fetch_raw_data()
        else:
            self.log.warning("Scope did not trigger, skipping raw data download.")

        self.fetch_metadata()
        self.is_downloaded = True


    def fetch_raw_data(self) -> None:
        self.log.debug(f"Fetching raw data for active sites and channels...")

        try:
            # TODO: Add a field in the site model that stores the module name
            is_acq480 = 'acq480' in self.master_site.get_knob('module_name')
            pre_samples = self.acquire.acq_pre_samples if is_acq480 else None

            # TODO: This value needs to be obtained from the site object rather than hardcoded
            # Holds the max channels value of the master analog input site
            site_nchan = 4 if is_acq480 else 16

            # Convert the active sites dictionary and its local site channel number list into
            # a list of absolute channel numbers. This means that channels are not differentiated
            # by the site number and instead by their channel number out of the total number of
            # analog input channels on the carrier.
            # TODO: Could access a property in the model that holds the list of absolute channels
            active_chs = [
                ch_num + (int(site_name.split('_')[-1]) - 1) * site_nchan
                for site_name, ch_list in self.config.active_sites.items()
                for ch_num in ch_list
            ]

            # Read raw data from analog input modules.
            # NOTE: raw data obtained from ACQ425 is returned as a numpy array of signed 16-bit
            # integers with little endian (LSB first).
            self.log.debug(f"Reading data from active_channels '{active_chs}'...")
            data_array = self.carrier.read_channels(active_chs)

            if data_array is None:
                raise ValueError("No data was obtained from the scope.")

            for index, abs_ch_num in enumerate(active_chs):
                site_num, site_ch_num = divmod(abs_ch_num - 1, site_nchan)
                site_ch_num += 1
                site_name = f'site_{site_num + 1}'

                channel = self.scope_info.sites[site_name].channels[str(site_ch_num)]
                self.log.debug(f"Parsing read data and storing for '{site_name}' channel '{site_ch_num}'...")

                if is_acq480:
                    data = np.concatenate([
                        data_array[index][:pre_samples],
                        data_array[(index + 2) % len(active_chs)][pre_samples:]
                    ])
                else:
                    data = data_array[index]

                channel.raw_data.append(data.tobytes())

            self.log.debug(f"Finished populating data for active channels.")
        except Exception as e:
            self.log.error(f"Fetching raw data encountered error: {e}")

    def fetch_metadata(self) -> None:
        self.log.info("Fetching metadata for active sites and channels...")

        try:
            for top_field in self.config.model_fields:
                if top_field in ['capture', 'trigger']:
                    config = getattr(self.scope_info, top_field)

                    for field in config.model_fields:
                        # FIXME: Bandaid to access self.acquire using 'capture' field from the model
                        cmd_obj = getattr(self, 'acquire' if top_field == 'capture' else top_field)

                        if has_prop(cmd_obj, field):
                            self.log.debug(f"Fetching {top_field} setting '{field}'...")
                            setattr(config, field, getattr(cmd_obj, field))

            self.ai_modules.fetch_site_config(self.config.active_sites, self.scope_info.sites)
        except Exception as e:
            self.log.error(f"Fetching metadata encountered error: {e}")

    # ------------------------------------------------------------------------------------
    #  Helper Methods
    # ------------------------------------------------------------------------------------

    def calc_time(self) -> None:
        try:
            t_zero = self.scope_info.capture.time_pre
            t_range = self.scope_info.capture.time_post
            t_delta = 1 / self.scope_info.capture.acq_srate

            for site, site_model in self.scope_info.sites.items():
                ch_models = site_model.channels

                for ch_model in ch_models.values():
                    num_samples = len(ch_model.raw_data)

                    if num_samples is not None:
                        if num_samples > int(t_range / t_delta):
                            time_values = np.linspace(0, num_samples * t_delta, num_samples)
                        else:
                            time_values = np.linspace(t_zero, t_range, int(t_range / t_delta))

                        if not ch_model.time_values:
                            ch_model.time_values.extend(time_values.tolist())
                        else:
                            ch_model.time_values.append(time_values.tolist())
        except Exception as e:
            self.log.error(f"Calculating time values encountered error: {e}")

    def calc_volts(self) -> None:
        try:
            bit_res = self.ai_modules.bit_depth

            for site, site_model in self.scope_info.sites.items():
                ch_models = site_model.channels

                for ch_model in ch_models.values():
                    raw_data = ch_model.raw_data
                    v_range = ch_model.ch_range or (10 / ch_model.ch_gain)
                    v_offset = ch_model.ch_offset or 0

                    volt_values = np.array(raw_data) * ((v_range / 2) / 2 ** (bit_res - 1)) + v_offset
                    ch_model.volt_values = volt_values.tolist()
        except Exception as e:
            self.log.error(f"Calculating volt values encountered error: {e}")

    def wait_for_state(self, state: str = None, timeout: float = None) -> bool:
        self.log.debug(f"Waiting for scope to reach state '{state}' within timeout '{timeout}'.")
        success = False

        try:
            start = perf_counter()

            while self.transient_state != state:
                if timeout is not None and (perf_counter() - start) > timeout:
                    raise TimeoutError(f"Timeout occurred while waiting for transient state '{state}'.")

                sleep(0.1)

            success = True
        except TimeoutError:
            self.log.error(f"Timeout occurred while waiting for transient state '{state}'.")
        except Exception as e:
            self.log.error(f"Waiting for transient state '{state}' encountered error: {e}.")
        finally:
            return success

    def check_connection(self) -> bool:
        self.log.debug("Checking scope connection status...")

        try:
            self.is_connected = False if self.carrier.get_sys_info() is None else True
            self.log.debug(f"Scope connection status: {self.is_connected}.")
        except Exception as e:
            self.log.error(f"Checking connection encountered error: {e}")
            self.is_connected = False
        finally:
            return self.is_connected

    def init_site_obj(self, site_type_dict: Dict[str, List[int]]) -> None:
        self.log.debug("Creating site objects...")

        try:
            for site_type, site_list in site_type_dict.items():
                if site_list:
                    module_type = self.carrier.svc[f's{site_list[0]}'].get_knob('MTYPE')
                    sites_obj = modules_map[module_type](self, self.config)

                    if site_type == 'AISITES':
                        self.ai_modules = sites_obj
                    elif site_type == 'AOSITES':
                        self.ao_modules = sites_obj
                    elif site_type == 'DIOSITES':
                        self.dio_modules = sites_obj
                    else:
                        raise ValueError(f"Site type '{site_type}' not yet supported.")

                    self.find_master_site(sites_obj)
        except Exception as e:
            self.log.error(f"Creating site object encountered error: {e}.")

    def find_master_site(self, sites_obj) -> None:
        self.log.debug("Locating master site...")

        try:
            for site in sites_obj.sites_dict.values():
                if site.get_knob('module_role') == 'MASTER':
                    sites_obj.master_site = site
                    self.log.debug(f"master_site: '{site}'")
                    return

            raise ValueError("Cannot find 'MASTER' site.")
        except Exception as e:
            self.log.error(f"Finding master site encountered error: {e}.")
