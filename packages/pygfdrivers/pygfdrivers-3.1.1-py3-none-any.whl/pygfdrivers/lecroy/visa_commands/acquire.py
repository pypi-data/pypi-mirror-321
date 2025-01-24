from typing import TYPE_CHECKING

from pygfdrivers.common.base_command import VisaCommand
from pygfdrivers.common.util.utilities import has_setter, has_prop, convert_si_suffix

from gf_data_models.lecroy.scope.capture import LecroyCaptureModel
from gf_data_models.common.device.cmd import create_cmd_class, CmdClassType

if TYPE_CHECKING:
    from ..lecroy_visa_scope import LecroyVisaScope


def init_acq_cmds() -> CmdClassType:
    acq: CmdClassType = create_cmd_class('acquire')
    acq.add_cmd(key='acq_arm', cmd='arm')
    acq.add_cmd(key='acq_stop', cmd='stop')
    acq.add_cmd(key='acq_srate', cmd='sara')
    acq.add_cmd(key='acq_sample_status', cmd='sast')
    acq.add_cmd(key='acq_points', cmd='sanu', args=['c1', 'c2', 'c3', 'c4'])
    acq.add_cmd(key='acq_count', cmd='avga', args={'max': 1024, 'min': 4}, default=16)
    acq.add_cmd(key='acq_interpolation', cmd='sxsa', args=[1, 0, 'on', 'off'], default='off')
    acq.add_cmd(key='acq_mem_size', cmd='msiz', args=['7k', '70k', '700k', '7m'], default='700k')
    acq.add_cmd(
        key='acq_mode',
        cmd='acqw',
        args=['sampling', 'peak_detect', 'average', 'high_res'],
        default='sampling'
    )
    return acq


class LecroyAcquire(VisaCommand):
    def __init__(self, scope: 'LecroyVisaScope') -> None:
        super().__init__(scope)

        self.acq_cmds = init_acq_cmds()
        self.acq_fields = [field for field in self.capture_fields if field.startswith('acq')]
        self._acq_bit_res = 8

        if self.is_pdv:
            self.acq_cmds.add_cmd(key='acq_srate', cmd='vbs app.Acquisition.Horizontal.SampleRate')
            self.acq_cmds.add_cmd(
                key='acq_xmax',
                cmd='vbs app.Acquisition.Horizontal.Maximize',
                args=['"fixedsamplerate"', '"setmaximummemory"'],
                default='"fixedsamplerate"'
            )
            self.acq_cmds.update_cmd_args(
                key='acq_mem_size',
                args=[
                    '500', '1000', '2500',
                    '5000', '10k', '25k',
                    '50k', '100k', '250k',
                    '500k', '1ma', '2.5ma',
                    '5ma', '10ma', '25ma',
                    '32ma'
                ]
            )

    def apply_acq_config(self, acq_config: LecroyCaptureModel) -> None:
        try:
            for field in self.acq_fields:
                setting = getattr(acq_config, field)

                if has_setter(self, field) and setting is not None:
                    setattr(self, field, setting)

        except Exception as e:
            self.log.error(f"Applying acquire configuration encountered error: {e}")
            raise

    def fetch_acq_config(self, acq_info: LecroyCaptureModel) -> None:
        try:
            for field in self.acq_fields:
                if has_prop(self, field):
                    setattr(acq_info, field, getattr(self, field))

        except Exception as e:
            self.log.error(f"Fetching acquire configuration encountered error: {e}")

    def acq_arm(self) -> None:
        try:
            self.write(self.acq_cmds, 'acq_arm')
        except Exception as e:
            self.log.error(f"Setting scope to single mode encountered error: {e}")

    def acq_stop(self) -> None:
        try:
            self.write(self.acq_cmds, 'acq_stop')
        except Exception as e:
            self.log.error(f"Setting scope to stop mode encountered error: {e}")

    @property
    def acq_bit_res(self) -> int:
        return self._acq_bit_res

    @acq_bit_res.setter
    def acq_bit_res(self, bit_res: int) -> None:
        self._acq_bit_res = bit_res

    @property
    def acq_mem_size(self) -> str:
        query = self.query(self.acq_cmds, 'acq_mem_size')
        _acq_mem_size = int(convert_si_suffix(query))
        return query.lower()

    @acq_mem_size.setter
    def acq_mem_size(self, mem_size: str) -> None:
        # requires SI units for this to work correctly - primarily K and M (case sensitive)
        cmd_key = 'acq_mem_size'
        mem_size_opts = self.acq_cmds.fetch_args(cmd_key)
        mem_size_default = self.acq_cmds.fetch_default(cmd_key)

        try:
            if mem_size_opts is not None and mem_size.lower() not in mem_size_opts:
                self.log.warning(f"mem_size: '{mem_size}' not in '{mem_size_opts}', default to '{mem_size_default}'.")
                mem_size = mem_size_default

            cmd_str = f"{self.acq_cmds.fetch_cmd(cmd_key)}"
            self.write(cmd=cmd_str, setting=mem_size.upper())
        except Exception as e:
            self.log.error(f"Setting acq_mem_size to '{mem_size}' encountered error: {e}")

    @property
    def acq_srate(self) -> float:
        query = self.query(self.acq_cmds, 'acq_srate')
        _acq_srate = convert_si_suffix(query.rstrip('Sa/s'))
        return _acq_srate

    @acq_srate.setter
    def acq_srate(self, acq_srate: float) -> None:
        cmd_key = 'acq_srate'

        if self.is_pdv:
            try:
                # automatically set the scope to determine number of sampling points from acq_srate
                # other option is to use acq_xmax="SetMaximumMemory", which determines sample points from mem_size
                acq_xmax = self.acq_xmax
                if 'memory' in acq_xmax:
                    self.acq_xmax = '"FixedSampleRate"'

                cmd_str = f"{self.acq_cmds.fetch_cmd(cmd_key)}"
                self.write(cmd=cmd_str, setting=acq_srate)
            except Exception as e:
                self.log.error(f"Setting sampling rate to '{acq_srate}' encountered error: {e}")
        else:
            pass

    # TODO: Current version of the query_scope method adds a ? at the end of the command, but Lecroy adds in the middle
    # def acq_points(self, source: Union[int, str]) -> int:
    #     cmd_key = f'acq_points'
    #     if isinstance(source, str):
    #         source = source.replace('h', '') if 'ch' in source else source
    #     else:
    #         source = f"c{source}"
    #     source_opts = self.acq_cmds.fetch_args(cmd_key)
    #
    #     try:
    #         if source_opts is not None and source not in source_opts:
    #             raise ValueError(f"Source '{source}' not found in '{source_opts}'")
    #
    #         cmd_str = f"{self.acq_cmds.fetch_cmd(cmd_key)}? source"
    #         query = self.query(self.acq_cmds, 'acq_points')
    #         _acq_points = int(convert_si_suffix(query))
    #         return _acq_points
    #     except Exception as e:
    #         self.log.error(f"Querying acq_points from source: '{source}' encountered error: {e}")

    # ------------------------------------------------------------------------------------
    #  Non-Core Acquire Methods - not universal amongst all Lecroy scopes
    # ------------------------------------------------------------------------------------

    # ----------------------------------T3DSO2014-----------------------------------------

    @property
    def acq_count(self) -> int:
        if not self.is_pdv:
            query = self.query(self.acq_cmds, 'acq_count')
            _acq_count = int(convert_si_suffix(query.rstrip('pts')))
            return _acq_count

    @acq_count.setter
    def acq_count(self, count: int) -> None:
        if not self.is_pdv:
            cmd_key = 'acq_count'
            count_lim = self.acq_cmds.fetch_args(cmd_key)
            count = min(max(count, count_lim.get('min')), count_lim.get('max'))

            # checks if the count is a power of two and if not, set it to the closest power of 2 count
            if (count & (count - 1)) != 0:
                lower = 2 ** (count.bit_length() - 1)
                upper = lower * 2
                count = lower if (count - lower) < (upper - count) else upper

            try:
                cmd_str = f"{self.acq_cmds.fetch_cmd(cmd_key)}"
                self.write(cmd=cmd_str, setting=count)
            except Exception as e:
                self.log.error(f"Setting acquire average count to '{count}' encountered error: {e}")

    @property
    def acq_sample_status(self) -> str:
        if not self.is_pdv:
            _acq_sample_status = self.query(self.acq_cmds, 'acq_sample_status')
            return _acq_sample_status.lower()

    @property
    def acq_interpolation(self) -> str:
        if not self.is_pdv:
            query = self.query(self.acq_cmds, 'acq_interpolation').lower()
            _acq_interpolation = 'sine' if query == 'on' else 'linear'
            return _acq_interpolation

    @acq_interpolation.setter
    def acq_interpolation(self, interpolation: str) -> None:
        if not self.is_pdv:
            cmd_key = 'acq_interpolation'
            interpolation = interpolation.lower()
            inter_state = 'on' if interpolation == 'sine' else 'off'

            try:
                cmd_str = f"{self.acq_cmds.fetch_cmd(cmd_key)}"
                self.write(cmd=cmd_str, setting=inter_state)
            except Exception as e:
                self.log.error(f"Setting acquire interpolation to '{interpolation}' encountered error: {e}")

    @property
    def acq_type(self) -> str:
        if not self.is_pdv:
            _acq_type = self.query(self.acq_cmds, 'acq_type')
            return _acq_type.lower()

    @acq_type.setter
    def acq_type(self, acq_type: str) -> None:
        if not self.is_pdv:
            cmd_key = 'acq_type'
            acq_type = acq_type.lower()
            acq_type_opts = self.acq_cmds.fetch_args(cmd_key)
            acq_type_default = self.acq_cmds.fetch_default(cmd_key)

            try:
                if acq_type_opts is not None and acq_type not in acq_type_opts:
                    self.log.warning(f"acq_type: '{acq_type}' not in '{acq_type_opts}', default to '{acq_type_default}'.")
                    acq_type = acq_type_default

                cmd_str = f"{self.acq_cmds.fetch_cmd(cmd_key)}"
                self.write(cmd=cmd_str, setting=acq_type)
            except Exception as e:
                self.log.error(f"Setting acq_type to '{acq_type}' encountered error: {e}")

    # ---------------------------LabMaster 9Zi, WaveRunner 6Zi----------------------------

    @property
    def acq_xmax(self) -> str:
        if self.is_pdv:
            _acq_xmax = self.query(self.acq_cmds, 'acq_xmax')
            return _acq_xmax.lower()
        else:
            pass

    @acq_xmax.setter
    def acq_xmax(self, acq_xmax: str) -> None:
        if self.is_pdv:
            cmd_key = 'acq_xmax'
            acq_xmax = acq_xmax.lower()

            acq_xmax_opts = self.acq_cmds.fetch_args(cmd_key)
            acq_xmax_default = self.acq_cmds.fetch_default(cmd_key)

            try:
                if acq_xmax_opts is not None and acq_xmax not in acq_xmax_opts:
                    self.log.warning(f"acq_xmax: '{acq_xmax}' not in '{acq_xmax_opts}', default to '{acq_xmax_default}'.")
                    acq_xmax = acq_xmax_default

                cmd_str = f"{self.acq_cmds.fetch_cmd(cmd_key)}"
                self.write(cmd=cmd_str, setting=acq_xmax)
            except Exception as e:
                self.log.error(f"Setting acq_xmax to '{acq_xmax}' encountered error: {e}")
        else:
            pass
