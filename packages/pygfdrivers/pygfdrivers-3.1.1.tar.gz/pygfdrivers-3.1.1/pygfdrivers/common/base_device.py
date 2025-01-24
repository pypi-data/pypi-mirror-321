import os
from pydantic import BaseModel
from typing import Callable, Any
from abc import ABC, abstractmethod

from pygfdrivers.common.util.save_utility import SaveUtil
from pygfdrivers.common.util.logger_manager import LOGGING_MODE, LoggerManager

from gf_data_models.common.infrastructure.config import BaseConfigDeviceModel

class BaseDevice(ABC):
    def __init__(self, device_config: BaseModel) -> None:

        # Device configuration attributes
        self.config = device_config
        self.apply_config_metadata()

        # Logging attributes
        self.log_manager = LoggerManager(self.name, LOGGING_MODE.DEBUG)
        self.log = self.log_manager.log

        # File related attributes
        self.saveUtil = SaveUtil()

        # Device status flag attributes
        self.is_armed = False
        self.is_aborted = False
        self.is_connected = False
        self.is_triggered = False
        self.is_configured = False
        self.is_downloaded = False

        # Data storage attribute
        self.data = None

    def apply_config_metadata(self) -> None:
        # Driver metadata attributes
        self.name = self.config.device.device_name
        self.save_path = self.config.device.file_save_path
        self.file_type = self.config.device.file_format

        # FlexCollect metadata attributes
        self.handler_type = self.config.handler_type
        self.is_enabled = self.config.config_enabled

    def fetch_config_metadata(self, info_model: BaseModel) -> None:
        # BaseDeviceConfigModel metadata attributes
        for field in BaseConfigDeviceModel().model_fields:
            config_value = getattr(self.config, field)
            setattr(info_model, field, config_value)

    def __del__(self) -> None:
        self.disconnect()

    def init(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError("Child classes must implement 'init' method.")

    # ------------------------------------------------------------------------------------
    #  Base Device Connection Methods - Must be overridden by the child class
    # ------------------------------------------------------------------------------------

    @abstractmethod
    def connect(self) -> None:
        raise NotImplementedError("Child classes must implement 'connect' method.")

    @abstractmethod
    def disconnect(self) -> None:
        raise NotImplementedError("Child classes must implement 'disconnect' method.")

    @abstractmethod
    def check_connection(self) -> bool:
        raise NotImplementedError("Child classes must implement 'check_connection' method.")

    # ------------------------------------------------------------------------------------
    #  Base Device Control Methods - Must be overridden by the child class
    # ------------------------------------------------------------------------------------

    @abstractmethod
    def apply_configurations(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError("Child classes must implement 'applyConfigurations' method.")

    @abstractmethod
    def arm(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError("Child classes must implement 'arm' method.")

    @abstractmethod
    def abort(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError("Child classes must implement 'abort' method.")

    @abstractmethod
    def prep_shot(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError("Child classes must implement 'prep_shot' method.")

    # ------------------------------------------------------------------------------------
    #  Base Data Methods - Must be overridden by the child class
    # ------------------------------------------------------------------------------------

    @abstractmethod
    def fetch_data(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError("Child classes must implement 'fetch_data' method.")

    @abstractmethod
    def fetch_metadata(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError("Child classes must implement 'fetch_metadata' method.")

    # ------------------------------------------------------------------------------------
    #  File Util Method - Call to run fetch_data then save data to file
    # ------------------------------------------------------------------------------------

    def save_data(self):
        if not hasattr(self, 'scope_info'):
            raise AttributeError("scope_info attribute is missing.")

        data = getattr(self, 'scope_info')

        if data is None:
            raise ValueError("Data attribute is empty.")

        file_path = os.path.join(self.save_path, self.name)
        self.saveUtil.save_file(data, str(file_path), self.file_type)

    def reconnect(self) -> None:
        self.disconnect()
        self.connect()

    # ------------------------------------------------------------------------------------
    #  Misc. Methods
    # ------------------------------------------------------------------------------------

    def handle_exceptions(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        try:
            ret = func(*args, **kwargs)
            return ret
        except Exception as e:
            self.log.error(f"{func.__name__} encountered error: {repr(e)}")
