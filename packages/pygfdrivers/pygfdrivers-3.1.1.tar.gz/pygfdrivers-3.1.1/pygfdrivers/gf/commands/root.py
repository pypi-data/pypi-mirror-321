import platform

from pygfdrivers.common.usb_scope import UsbScope
from pygfdrivers.common.visa_scope import VisaScope
from pygfdrivers.common.base_command import VisaCommand, UsbCommand


# Determine the base class based on the platform
if platform.system() == 'Linux':
    ScopeClass = UsbScope
    CommandClass = UsbCommand
elif platform.system() == 'Windows':
    ScopeClass = VisaScope
    CommandClass = VisaCommand
else:
    raise RuntimeError("Unsupported platform")


class GFDigitizerRoot(CommandClass):
    def __init__(self, scope: ScopeClass) -> None:
        super().__init__(scope)

    def arm(self) -> str:
        return self.query(cmd='set_trigger_arm')

    def trig_force(self) -> str:
        return self.query(cmd='set_trigger_force')

    def clear(self) -> None:
        self.write(cmd='clear')

    def rabbit(self) -> str:    # !ONLY works with new digitizer firmware
        return self.query(cmd='rabbit')
    
    def is_trig_armed(self) -> str:
        return self.query(cmd='is_trigger_armed')

    @property
    def arm_status(self) -> bool:
        _arm_status = self.query(cmd='is_trigger_armed')
        return _arm_status.split('|')[2] == 'TRUE'

    @property
    def trig_status(self) -> bool:
        _trig_status = self.query(cmd='is_trigger_armed')
        return _trig_status.split('|')[2] == 'FALSE'
