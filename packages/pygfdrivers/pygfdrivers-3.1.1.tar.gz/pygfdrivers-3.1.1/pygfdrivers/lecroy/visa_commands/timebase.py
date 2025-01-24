from typing import TYPE_CHECKING

from pygfdrivers.common.base_command import VisaCommand
from pygfdrivers.common.util.utilities import has_setter, has_prop, convert_si_suffix

from gf_data_models.lecroy.scope.capture import LecroyCaptureModel
from gf_data_models.common.device.cmd import create_cmd_class, CmdClassType

if TYPE_CHECKING:
    from ..lecroy_visa_scope import LecroyVisaScope


def init_time_cmds() -> CmdClassType:
    time: CmdClassType = create_cmd_class('Timebase')
    time.add_cmd(key='time_pos', cmd='trdl')
    time.add_cmd(key='time_scale', cmd='tdiv')
    return time


class LecroyTimebase(VisaCommand):
    def __init__(self, scope: 'LecroyVisaScope') -> None:
        super().__init__(scope)

        self.time_cmds = init_time_cmds()
        self.time_fields = [field for field in self.capture_fields if field.startswith('time')]

    def apply_time_config(self, time_config: LecroyCaptureModel) -> None:
        try:
            for field in self.time_fields:
                setting = getattr(time_config, field)

                if has_setter(self, field) and setting is not None:
                    setattr(self, field, setting)

        except Exception as e:
            self.log.error(f"Applying trigger configuration encountered error: {e}")
            raise

    def fetch_time_config(self, time_info: LecroyCaptureModel) -> None:
        try:
            for field in self.time_fields:
                if has_prop(self, field):
                    setattr(time_info, field, getattr(self, field))

        except Exception as e:
            self.log.error(f"Fetching trigger configuration encountered error: {e}")

    @property
    def time_pos(self) -> float:
        query = self.query(self.time_cmds, 'time_pos')
        _time_pos = convert_si_suffix(query.rstrip('s'))
        return _time_pos

    @time_pos.setter
    def time_pos(self, t_pos: float) -> None:
        cmd_key = 'time_pos'

        try:
            cmd_str = f"{self.time_cmds.fetch_cmd(cmd_key)}"
            self.write(cmd=cmd_str, setting=f"{t_pos:.2e}")
        except Exception as e:
            self.log.error(f"Setting time_pos to '{t_pos}' encountered error: {e}")

    @property
    def time_scale(self) -> float:
        query = self.query(self.time_cmds, 'time_scale')
        _time_scale = convert_si_suffix(query.rstrip('s'))
        return _time_scale

    @time_scale.setter
    def time_scale(self, t_scale: float) -> None:
        cmd_key = 'time_scale'

        try:
            cmd_str = f"{self.time_cmds.fetch_cmd(cmd_key)}"
            self.write(cmd=cmd_str, setting=f"{t_scale:.2e}")

        except Exception as e:
            self.log.error(f"Setting time_scale to '{t_scale}' encountered error: {e}")

    @property
    def time_range(self) -> float:
        _time_range = self.time_scale * 10 if self.is_pdv else self.time_scale * 14
        return _time_range

    @time_range.setter
    def time_range(self, t_range: float) -> None:
        self.time_scale = t_range / 10 if self.is_pdv else t_range / 14

    @property
    def time_zero(self) -> float:
        _time_zero = (self.time_scale * 5 if self.is_pdv else self.time_scale * 7) - self.time_pos
        return _time_zero

    @time_zero.setter
    def time_zero(self, t_zero: float) -> None:
        t_pos = (self.time_scale * 5 if self.is_pdv else self.time_scale * 7) - t_zero
        self.log.debug(f"Calculated time position '{t_pos}' setting from time zero = '{t_zero}'.")
        self.time_pos = t_pos
