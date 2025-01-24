import platform
from typing import List, Dict, Union

from pygfdrivers.common.usb_scope import UsbScope
from pygfdrivers.common.visa_scope import VisaScope
from pygfdrivers.common.util.utilities import has_prop, has_setter
from pygfdrivers.common.base_command import VisaCommand, UsbCommand

from pygfdrivers.gf.util.utilities import format_channel, format_gain, format_coupling

from gf_data_models.gf.digitizer.digitizer import GfChannelModel

# Determine the base class based on the platform
if platform.system() == "Linux":
    ScopeClass = UsbScope
    CommandClass = UsbCommand
elif platform.system() == "Windows":
    ScopeClass = VisaScope
    CommandClass = VisaCommand
else:
    raise RuntimeError("Unsupported platform")


class GFDigitizerChannel(CommandClass):
    def __init__(self, scope: ScopeClass) -> None:
        super().__init__(scope)

        self.ch_num = None
        self.ch_config = None

    def apply_ch_config(self, active_channels: List[int],  config: Dict[int, GfChannelModel]) -> None:
        self.ch_config = config

        try:
            for ch in active_channels:
                self.ch_num = ch
                ch_model = config[ch]

                for field, setting in ch_model.model_dump().items():
                    if has_setter(self, field) and setting is not None:
                        self.set_ch(field, setting, ch)

        except Exception as e:
            self.log.error(f"Applying channel configuration encountered error: {e}")
            raise

    def fetch_ch_config(self, active_chs: List[int], config: Dict[str, GfChannelModel]) -> None:
        try:
            for ch in active_chs:    
                self.ch_num = ch     
                ch_model = config[str(ch)]

                for field in self.source_fields:
                    if has_prop(self, field):
                        setattr(ch_model, field, getattr(self, field))

        except Exception as e:
            self.log.error(f"Fetching configuration encountered error: {e}")

    def set_ch(self, setter: str, setting: Union[int, float, str, bool], ch: int) -> None:
        try:
            self.ch_num = ch
            setattr(self, setter, setting)
        except Exception as e:
            self.log.error(f"Setting channel '{ch}' '{setter}' to '{setting}' encountered error: {e}.")

    def get_ch(self, getter: str, ch: int) -> None:
        try:
            self.ch_num = ch
            return getattr(self, getter)
        except Exception as e:
            self.log.error(f"Fetching channel '{ch}' '{getter}' encountered error: {e}.")

    @property
    def ch_gain(self) -> float:
        return self.ch_config[self.ch_num].ch_gain
    
    @ch_gain.setter
    def ch_gain(self, gain: int) -> None:
        ch = self.ch_num
        self.ch_config[self.ch_num].ch_gain = gain
        ch = format_channel(ch)
        gain = format_gain(gain)
        self.query(cmd=f"set_gain_value chan={ch} value={gain}")

    @property
    def ch_coupling(self) -> str:
        return self.ch_config[self.ch_num].ch_coupling

    @ch_coupling.setter
    def ch_coupling(self, coupling: str) -> None:
        ch = self.ch_num
        self.ch_config[self.ch_num].ch_coupling = coupling
        ch = format_channel(ch)
        coupling = format_coupling(coupling)
        self.query(cmd=f"set_coupling_state chan={ch} state={coupling}")

    @property
    def ch_offset(self) -> float:
        return self.ch_config[self.ch_num].ch_offset
    
    @ch_offset.setter
    def ch_offset(self, offset: float) -> None:
        self.ch_config[self.ch_num].ch_offset = offset

    # ------------------------------------------------------------------------------------
    # Waveform setter and properties
    # ------------------------------------------------------------------------------------

    @property
    def wave_byte_order(self) -> str:
        # GF digitizer does not have any other byte order other than 'big' endian (MSB first)
        return 'big'

    # ------------------------------------------------------------------------------------
    # Source setter and properties
    # ------------------------------------------------------------------------------------

    @property
    def source_name(self) -> str:
        return self.ch_config[self.ch_num].source_name

    @source_name.setter
    def source_name(self, source_name: str) -> None:
        self.ch_config[self.ch_num].source_name = source_name

    @property
    def source_id(self) -> str:
        return self.ch_config[self.ch_num].source_id

    @source_id.setter
    def source_id(self, source_id: str) -> None:
        self.ch_config[self.ch_num].source_id = source_id
