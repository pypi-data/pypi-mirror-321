import numpy as np
from time import sleep

from pygfdrivers.common.visa_scope import VisaScope

from pygfdrivers.lecroy.visa_commands.common import LecroyCommon
from pygfdrivers.lecroy.visa_commands.acquire import LecroyAcquire
from pygfdrivers.lecroy.visa_commands.channel import LecroyChannel
from pygfdrivers.lecroy.visa_commands.trigger import LecroyTrigger
from pygfdrivers.lecroy.visa_commands.timebase import LecroyTimebase
from pygfdrivers.lecroy.visa_commands.waveform import LecroyWaveform

from gf_data_models.lecroy.scope.scope import LecroyScopeModel


class LecroyVisaScope(VisaScope):
    def __init__(self, scope_config: LecroyScopeModel) -> None:
        super().__init__(scope_config)
    
    def init(self) -> None:
        super().init()

        try:
            if self.scope is None:
                raise ValueError("LeCroy VISA scope did not connect properly.")

            # LeCroy scopes require a higher transfer chunk to prevent "illegal operations" errors
            # This value was chosen arbitrarily and has seemingly worked with all the WaveRunners,
            # LabMaster and the T3DSO2000(A) LeCroy scopes.
            self.scope.chunk_size = 20 * 1024 * 1024

            # T3DSO2000 scopes are requiring 10 seconds per channel to download data with mem_size=7m
            # if the timeout is set below 10 seconds, the scopes will be unable to download waveform data
            self.scope.timeout = 30_000

            self.common = LecroyCommon(self)
            self.acquire = LecroyAcquire(self)
            self.channel = LecroyChannel(self)
            self.trigger = LecroyTrigger(self)
            self.timebase = LecroyTimebase(self)
            self.waveform = LecroyWaveform(self)

            self.common.comm_header('off')
            self.active_chs = self.config.active_channels

            self.log.info(f"LECROY SCOPE TYPE FOR SCOPE NAME ---- {self.name}")
        except Exception as e:
            self.log.error(f"Initializing LeCroy VISA scope encountered error: {e}")
            raise

    def apply_configurations(self):
        self.log.info("Applying scope configurations...")

        try:
            self.log.info("Applying trigger configurations...")
            self.trigger.apply_trig_config(self.config.trigger)

            self.log.info("Applying capture configurations...")
            self.timebase.apply_time_config(self.config.capture)

            self.log.info("Applying acquire configurations...")
            self.acquire.apply_acq_config(self.config.capture)

            self.log.info("Applying channel configurations...")
            self.channel.apply_ch_config(self.active_chs, self.config.channels)

            self.log.info("Applying scope configurations has finished.")
            self.is_configured = True
        except Exception as e:
            self.log.error(f"Applying scope configurations encountered error: {e}.")
            self.is_configured = False

    def arm(self):
        self.log.info("Arming scope...")
        try:
            self.prep_shot()
            self.common.single_mode()

            # 0.2 seconds seemed to be the most consistent to ensure that the scope has
            # had enough time to turn the required registers or flags to accurately
            # determine its armed status
            sleep(0.2)

            self.is_armed = self.arm_status
            self.log.info(f"Scope {'armed.' if self.is_armed else 'failed to arm.'}")
        except Exception as e:
            self.log.info(f"Arming scope encountered error: {e}")

    def abort(self) -> None:
        self.log.info("Aborting scope...")
        try:
            self.common.stop_mode()
            self.log.info("Scope aborted.")
            self.is_aborted = True
        except Exception as e:
            self.log.error(f"Aborting scope encountered error: {e}")

    def trigger_software(self) -> None:
        self.trigger.trig_force()
        self.is_triggered = True

    def prep_shot(self) -> None:
        self.log.info(f"Preparing shot...")

        try:
            self.common.clear_status()
            self.clear_scope_info_data()

            # Setting the scope in stop mode and clearing the status ensures the armed status is read correctly
            self.common.stop_mode()

            # querying the status ensures the arm and trigger register is set to 0
            self.common.status

            self.is_armed = False
            self.is_aborted = False
            self.is_triggered = False
            self.is_downloaded = False
            self.log.info(f"Finished preparing shot.")
        except Exception as e:
            self.log.error(f"Preparing shot encountered error: {e}.")

    def check_connection(self) -> bool:
        try:
            query = self.common.idn
            self.is_connected = True if query is not None else False
        except Exception as e:
            self.log.error(f"Checking connection encountered error: {e}")
            self.is_connected = False
        finally:
            return self.is_connected

    # ------------------------------------------------------------------------------------
    #  Read Only Methods
    # ------------------------------------------------------------------------------------

    @property
    def arm_status(self) -> bool:
        try:
            status_code = self.common.status
            _arm_status = status_code == 8192
            self.log.info(f"Armed Status: {_arm_status}")
            return _arm_status
        except Exception as e:
            self.log.error(f"Querying arm status encountered error: {e}")

    @property
    def trigger_status(self) -> bool:
        try:
            # read status code integer as a binary string
            status_code = bin(self.common.status)

            # only examine bit 0 in the binary string to check trigger status
            _trigger_status = status_code[-1] == '1'

            self.is_triggered = _trigger_status
            self.log.info(f"Trigger Status: {_trigger_status}")
            return _trigger_status
        except Exception as e:
            self.log.error(f"Querying trigger status encountered error: {e}")
            return False

    # ------------------------------------------------------------------------------------
    #  Data Storage Methods
    # ------------------------------------------------------------------------------------

    def fetch_data(self) -> None:
        self.log.info("Downloading real-time data...")
        try:
            if self.is_triggered:
                for ch in self.active_chs:
                    self.log.info(f"Downloading wave source '{ch}'...")
                    data = self.waveform.wave_data(f"c{ch}")
                    raw_data = self.scope_info.channels[str(ch)].raw_data
                    raw_data.append(data) if isinstance(data, bytes) else raw_data.extend(data)

                self.fetch_metadata()

                # self.log.info("Calculating waveform time values...")
                # self.calc_time()
                #
                # self.log.info("Calculating waveform voltage values...")
                # self.calc_volts()

                self.log.debug(f"Finished populating data for active channels.")
            else:
                self.log.warning('Scope did not trigger, skipping waveform data download.')
                self.fetch_metadata()
            self.is_downloaded = True
        except Exception as e:
            raise ValueError(f"Failed downloading data with error: {e}.")

    def fetch_metadata(self) -> None:
        self.log.info("Fetching channel metadata...")

        try:
            for top_field in self.scope_info.model_fields:
                if top_field not in ['scope', 'active_channels']:
                    if top_field == 'capture':
                        self.acquire.fetch_acq_config(self.scope_info.capture)
                        self.timebase.fetch_time_config(self.scope_info.capture)
                    elif top_field == 'trigger':
                        self.trigger.fetch_trig_config(self.scope_info.trigger)
                    elif top_field == 'channels':
                        self.channel.fetch_ch_config(self.active_chs, self.scope_info.channels)
                        self.waveform.fetch_wave_config(self.active_chs, self.scope_info.channels)
        except Exception as e:
            self.log.error(f"Fetching metadata encountered error: {e}")

    # ------------------------------------------------------------------------------------
    #  Helper Methods
    # ------------------------------------------------------------------------------------

    def calc_time(self) -> None:
        try:
            t_zero = self.scope_info.capture.time_zero
            t_delta = 1 / self.scope_info.capture.acq_srate
            num_samples = 0

            if not self.common.is_pdv:
                num_samples = self.scope_info.capture.acq_mem_size.upper()

                try:
                    num_samples = float(num_samples)
                except ValueError:
                    if 'K' in num_samples:
                        num_samples = int(num_samples.rstrip('K')) * 1e3
                    else:
                        num_samples = int(num_samples.rstrip('M')) * 1e6

            for ch_model in self.scope_info.channels.values():
                if self.common.is_pdv:
                    num_samples = ch_model.wave_points

                time_values = t_zero + (t_delta * np.arange(num_samples))

                if not ch_model.time_values:
                    ch_model.time_values.extend(time_values.tolist())
                else:
                    ch_model.time_values.append(time_values.tolist())
        except Exception as e:
            self.log.error(f"Calculating time values encountered error: {e}")

    def calc_volts(self) -> None:
        try:
            for ch_model in self.scope_info.channels.values():
                raw_data = ch_model.raw_data

                if len(raw_data) > 1 and all(isinstance(raw_data[i], (list, bytes)) for i in range(2)):
                    is_segmented = True
                else:
                    is_segmented = False

                for segment in raw_data:
                    segment = np.frombuffer(segment, dtype=np.int8)

                    if not self.common.is_pdv:
                        bit_res = 8
                        code_per_div = 30 if bit_res == 8 else 30 * 4
                        code_per_div = 25 if bit_res == 8 else 30 * 4

                        v_div = ch_model.ch_scale
                        v_offset = ch_model.ch_offset if hasattr(ch_model, 'ch_offset') else 0

                        volt_values = np.array(segment) * (v_div / code_per_div) - v_offset
                    else:
                        y_inc = ch_model.wave_yinc
                        y_origin = ch_model.wave_yorigin

                        volt_values = (np.array(segment) * y_inc) - y_origin

                    if is_segmented:
                        ch_model.volt_values.append(volt_values.tolist())
                    else:
                        ch_model.volt_values = volt_values.tolist()
        except Exception as e:
            self.log.error(f"Calculating volt values encountered error: {e}")



