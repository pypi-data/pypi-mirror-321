from typing import List, Dict, TYPE_CHECKING

from pygfdrivers.common.util.utilities import has_prop
from pygfdrivers.common.base_command import VisaCommand

from gf_data_models.lecroy.scope.channel import LecroyChannelModel
from gf_data_models.common.device.cmd import create_cmd_class, CmdClassType

if TYPE_CHECKING:
    from ..lecroy_visa_scope import LecroyVisaScope


def init_wave_cmds() -> CmdClassType:
    wave: CmdClassType = create_cmd_class('Waveform')
    wave.add_cmd(key='wave_data', cmd='wf', args=['c1', 'c2', 'c3', 'c4', 'math'], default='c1')
    return wave


class LecroyWaveform(VisaCommand):
    def __init__(self, visa_scope: 'LecroyVisaScope') -> None:
        super().__init__(visa_scope)

        self.visa_scope = self.scope.scope
        self.wave_cmds = init_wave_cmds()
        self.wave_fields = [field for field in self.source_fields if field.startswith('wave')]

        if self.is_pdv:
            self.wave_cmds.add_cmd(key='wave_points', cmd="insp? 'wave_array_count'")
            self.wave_cmds.add_cmd(key='wave_xinc', cmd="insp? 'horiz_interval'")
            self.wave_cmds.add_cmd(key='wave_source', cmd="insp? 'wave_source'")
            self.wave_cmds.add_cmd(key='wave_yinc', cmd="insp? 'vertical_gain'")
            self.wave_cmds.add_cmd(key='wave_yorigin', cmd="insp? 'vertical_offset'")
            self.wave_cmds.add_cmd(key='wave_format', cmd='cfmt', args=['byte', 'word'], default='byte')
            self.wave_cmds.add_cmd(key='wave_byte_order', cmd='cord', args=['hi', 'lo'], default='hi')
            self.wave_cmds.update_cmd_args(
                key='wave_data',
                args=[
                    'c1', 'c2', 'c3', 'c4',
                    'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                    'm1', 'm2', 'm3', 'm4',
                    'ta', 'tb', 'tc', 'td'
                ]
            )

    def fetch_wave_config(self, active_chs: List[int], wave_info: Dict[str, LecroyChannelModel]) -> None:
        try:
            for ch in active_chs:
                info = wave_info[str(ch)]
                self.ch_num = ch
                for field in self.wave_fields:
                    if has_prop(self, field):
                        setattr(info, field, getattr(self, field))
        except Exception as e:
            self.log.error(f"Fetching waveform configurations encountered error: {e}.")

    def wave_data(self, source: str) -> list:
        cmd_key = 'wave_data'
        source_opts = self.wave_cmds.fetch_args(cmd_key)
        source_default = self.wave_cmds.fetch_default(cmd_key)

        if source_opts is not None and source not in source_opts:
            self.log.warning(f"source: '{source}' not in '{source_opts}', default to '{source_default}'.")
            source = source_default

        try:
            # Command string must be structured <source>:wf? datn
            # i.e. for channel 1 data -- c1:wf? datn
            cmd_value = 'dat1' if self.is_pdv else 'dat2'
            cmd_str = f"{source}:{self.wave_cmds.fetch_cmd(cmd_key)}? {cmd_value}"

            # Values could be queried as different types to avoid post conversion but capturing
            # as bytes yields the fastest transfer times as there is no conversion overhead
            # from PyVISA
            _wave_data = self.visa_scope.query_binary_values(cmd_str, datatype='B', container=bytes)

            # Remove padding from data only for the WaveRunner or LabMaster scopes
            return _wave_data[:-2] if self.is_pdv else _wave_data
        except Exception as e:
            self.log.error(f"Fetching wave_data from source '{source}' encountered error: {e}.")

    # ------------------------------------------------------------------------------------
    #  Non-Core Wave Methods - not universal amongst all Lecroy scopes
    # ------------------------------------------------------------------------------------

    # --------------LabMaster, Waverunner-------------------------------------------------

    @property
    def wave_points(self) -> int:
        if self.is_pdv:
            _wave_points = self.query(cmd=f"c{self.ch_num}:insp? 'wave_array_count'")
            _wave_points = _wave_points.split(':')[-1].split()[0]

            # Remove padding in the wave data array
            _wave_points = int(_wave_points) - 2
            return int(_wave_points)

    @property
    def wave_xinc(self) -> float:
        if self.is_pdv:
            _wave_xinc = self.query(cmd=f"c{self.ch_num}:insp? 'horiz_interval'")
            _wave_xinc = _wave_xinc.split(':')[-1].split()[0]
            return float(_wave_xinc)

    @property
    def wave_source(self) -> str:
        if self.is_pdv:
            _wave_source = self.query(cmd=f"c{self.ch_num}:insp? 'wave_source'")
            _wave_source = _wave_source.split(':')[-1].split()[0]
            return _wave_source.lower()

    @property
    def wave_yinc(self) -> float:
        if self.is_pdv:
            _wave_yinc = self.query(cmd=f"c{self.ch_num}:insp? 'vertical_gain'")
            _wave_yinc = _wave_yinc.split(':')[-1].split()[0]
            return float(_wave_yinc)

    @property
    def wave_yorigin(self) -> float:
        if self.is_pdv:
            _wave_yinc = self.query(cmd=f"c{self.ch_num}:insp? 'vertical_offset'")
            _wave_yinc = _wave_yinc.split(':')[-1].split()[0]
            return float(_wave_yinc)

    @property
    def wave_format(self) -> str:
        if self.is_pdv:
            _wave_format = self.query(self.wave_cmds, 'wave_format')
            _wave_format = _wave_format.split(',')[1]
            return _wave_format.lower()

    @property
    def wave_byte_order(self) -> str:
        if self.is_pdv:
            _wave_byte_order = self.query(self.wave_cmds, 'wave_byte_order')
            return _wave_byte_order.lower()
