import platform
from logging import getLogger
from typing import TYPE_CHECKING

from pygfdrivers.common.usb_scope import UsbScope
from pygfdrivers.common.visa_scope import VisaScope

if TYPE_CHECKING:
    if platform.system() == "Linux":
        ScopeClass = UsbScope
    elif platform.system() == "Windows":
        ScopeClass = VisaScope
    else:
        raise RuntimeError("Unsupported platform")


class BaseCommand:
    def __init__(self, scope: 'ScopeClass') -> None:
        self.log = getLogger(scope.name)

        self.scope = scope
        self.scope_series = scope.scope_series

        self.write = self.scope.write_scope
        self.query = self.scope.query_scope
        self.read_bytes = self.scope.read_bytes_from_scope

        self.trig_fields = getattr(self.scope.scope_info.trigger, 'model_fields')
        self.capture_fields = getattr(self.scope.scope_info.capture, 'model_fields')
        self.source_fields = getattr(getattr(self.scope.scope_info.channels, 'default_factory'), 'model_fields')


class VisaCommand(BaseCommand):
    def __init__(self, visa_scope: VisaScope) -> None:
        super().__init__(visa_scope)

        self.is_mxr = visa_scope.scope_series == 'MXR'
        self.is_pdv = visa_scope.scope_series == 'LabMaster' or visa_scope.scope_series == 'WaveRunner'
        self.set_and_verify_config = self.scope.set_and_verify_config


class UsbCommand(BaseCommand):
    def __init__(self, usb_scope: UsbScope) -> None:
        super().__init__(usb_scope)
