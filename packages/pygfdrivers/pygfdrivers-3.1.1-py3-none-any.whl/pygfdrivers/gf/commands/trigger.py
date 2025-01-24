import platform

from pygfdrivers.common.usb_scope import UsbScope
from pygfdrivers.common.visa_scope import VisaScope
from pygfdrivers.common.util.utilities import has_prop, has_setter
from pygfdrivers.common.base_command import VisaCommand, UsbCommand

from pygfdrivers.gf.util.utilities import format_trig_level

from gf_data_models.gf.digitizer.digitizer import GfTriggerModel

# Determine the base class based on the platform
if platform.system() == "Linux":
    ScopeClass = UsbScope
    CommandClass = UsbCommand
elif platform.system() == "Windows":
    ScopeClass = VisaScope
    CommandClass = VisaCommand
else:
    raise RuntimeError("Unsupported platform")


class GFDigitizerTrigger(CommandClass):
    def __init__(self, scope: ScopeClass) -> None:
        super().__init__(scope)

    def apply_trig_config(self, config: GfTriggerModel) -> None:
        try:   
            for field, setting in config.dict().items():
                if has_setter(self, field) and setting is not None:
                    setattr(self, field, setting)

        except Exception as e:
            self.log.error(f"Applying trigger configuration encountered error: {e}")
            raise

    def fetch_trig_config(self, config: GfTriggerModel) -> None:
        try:
            for field in self.trig_fields:
                if has_prop(self, field):
                    setattr(config, field, getattr(self, field))

        except Exception as e:
            self.log.error(f"Fetching trigger configuration encountered error: {e}")

    @property
    def trig_level(self) -> int:
        return self._trig_level

    @trig_level.setter
    def trig_level(self, level: int) -> None:
        self._trig_level = level
        level = format_trig_level(level)
        self.query(cmd = f"set_pwm_value pwm=triglevel value={level}")
