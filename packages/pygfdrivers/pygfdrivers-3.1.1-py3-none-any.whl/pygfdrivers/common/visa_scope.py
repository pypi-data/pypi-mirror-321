from abc import ABC
from fuzzywuzzy import fuzz
from typing import Union, Any
from pydantic import BaseModel
from pyvisa import ResourceManager, VisaIOError, InvalidSession

from pygfdrivers.common.base_scope import BaseScope
from pygfdrivers.common.util.utilities import convert_value
from pygfdrivers.keysight.util.utilities import fetch_keysight_series
from pygfdrivers.lecroy.util.fetch_lecroy_model import fetch_lecroy_series

from gf_data_models.common.device.cmd import CmdClassType


class VisaScope(BaseScope, ABC):
    def __init__(self, scope_config: BaseModel) -> None:
        super().__init__(scope_config)

        self.scope = None
        self.scope_series = None

    def init(self) -> None:
        try:
            self.conn_str = self.config.device.create_resource_str()

            if self.conn_str is None:
                self.conn_str = getattr(self.config.device, 'device_conn_str')

                if 'none' in self.conn_str.lower():
                    raise ValueError("Configuration missing 'ip_addr' and 'conn_str' field.")

            self.connect()
        except (Exception, VisaIOError) as e:
            self.log.error(f"Initializing VISA device encountered error: {e}")
        finally:
            self.is_connected = False if self.scope is None else True

    def connect(self) -> None:
        try:
            resource_manager = ResourceManager()
            self.scope = resource_manager.open_resource(f"{self.conn_str}")
            self.scope.read_termination = '\n'
            self.scope_series = self.get_device_series()
            self.log.info(f"VISA '{self.conn_str}' device connected.")
        except Exception as e:
            raise ValueError(f"Opening VISA resource failed with error: {e}")

    def disconnect(self) -> None:
        if self.scope:
            try:
                self.scope.close()
                self.log.info(f"VISA device disconnected")
            except VisaIOError as e:
                self.log.error(f"Closing VISA resource encountered error: {e}")

    def get_device_series(self) -> str:
        if 'keysight' in self.scope_type:
            device_series = fetch_keysight_series(self.scope)
            return device_series
        elif 'lecroy' in self.scope_type:
            device_series = fetch_lecroy_series(self.scope)
            return device_series

        return ''

    # ------------------------------------------------------------------------------------
    #  VISA Command Handler Methods
    # ------------------------------------------------------------------------------------

    def read_bytes_from_scope(self, num_bytes: int) -> bytes:
        try:
            byte_data = self.scope.read_bytes(num_bytes)
            return byte_data
        except Exception as e:
            self.handle_err(e, f"read_bytes : {num_bytes}")

    def write_scope(
            self,
            cmd_obj: CmdClassType = None,
            cmd_key: str = None,
            cmd: str = None,
            setting: Union[int, float, str] = None,
            channel: int = None
    ) -> None:

        try:
            if cmd is None:
                if cmd_obj is None or cmd_key is None:
                    raise ValueError("Require either 'cmd_obj and cmd_key' together or 'cmd' alone (or with 'val').")

                cmd_obj.is_valid_cmd_key(cmd_key)
                cmd = cmd_obj.fetch_cmd(cmd_key)

            # Automation commands for big lecroy scopes
            # TODO: Remove this when possible, method is doing too many things
            device_series = self.get_device_series()

            if device_series.lower() in {'waverunner', 'labmaster'} and 'vbs' in cmd and channel is None:
                vbs, remainder = cmd.split(' ', 1)
                cmd = f"{vbs} '{remainder}={setting}'"
            else:
                cmd = cmd if channel is None else f":CHANnel{channel}{cmd}"
                cmd = cmd if setting is None else f"{cmd} {setting}"

            self.log.debug(f"Writing '{cmd.upper()}' to scope.")
            self.scope.write(cmd)
        except Exception as e:
            self.log.error(f"Writing to VISA resource encountered error: {e}")

    def query_scope(
            self,
            cmd_obj: CmdClassType = None,
            cmd_key: str = None,
            cmd: str = None,
            channel: int = None
    ) -> Any:

        try:
            if cmd is None:
                if cmd_obj is None and cmd_key is None:
                    raise ValueError("Require either 'cmd_obj and cmd_key' together or 'cmd' alone.")

                cmd_obj.is_valid_cmd_key(cmd_key)
                cmd = cmd_obj.fetch_cmd(cmd_key)

            # Automation commands for big lecroy scopes
            # TODO: Remove this when possible, method is doing too many things
            device_series = self.get_device_series()

            if device_series.lower() in {'waverunner', 'labmaster'} and 'vbs' in cmd:
                vbs, remainder = cmd.split(" ", 1)
                cmd = f"{vbs}? 'return={remainder}'"
            elif cmd_obj:
                cmd = f":CHANnel{channel}{cmd}?" if channel is not None else f"{cmd}?"
            elif cmd_obj is None and channel is None:
                pass

            self.log.debug(f"Querying '{cmd.upper()}' on scope.")
            response = self.scope.query(cmd)
            return response
        except Exception as e:
            self.log.error(f"Querying VISA resource encountered error: {e}")

    def handle_err(self, err: Exception, cmd: str) -> None:
        if type(err) is VisaIOError or InvalidSession:
            self.log.error(f"Scope has disconnected.")
            self.is_connected = False
            raise err

        self.log.error(f"Writing '{cmd}' to scope encountered error: {err}")

    # ------------------------------------------------------------------------------------
    #  Experimental Methods
    # ------------------------------------------------------------------------------------

    def set_and_verify_config(
            self,
            cmd_obj: CmdClassType,
            cmd_key: str,
            setting: Union[str, int, float],
            channel: int = None,
    ) -> None:

        self.set_config(cmd_obj, cmd_key, setting, channel)
        self.verify_config(cmd_obj, cmd_key, setting, channel)

    def set_config(
            self,
            cmd_obj: CmdClassType,
            cmd_key: str,
            setting: Union[str, int, float],
            channel: int = None,
    ) -> None:
        """
        Ensures that either the value or channel being passed to the scope is valid before
        writing to the scope and configuring it based on the value.
        """
        try:
            cmd_obj.is_valid_cmd_key(cmd_key)

            try:
                self.is_valid_setting(cmd_obj, cmd_key, setting)
            except ValueError as e:
                self.log.warning(f"Invalid value: {e}")
                self.log.warning(f"Attempting to fetch default value for '{cmd_key}'...")
                setting = cmd_obj.fetch_default(cmd_key)

            msg = f"{channel = } to '{setting}'" if channel is not None else f"to '{setting}'"
            self.log.debug(f"Setting '{cmd_key}' {msg}.")
            self.write_scope(cmd_obj, cmd_key, setting=setting, channel=channel)
        except Exception as e:
            self.log.error(f"Configuring {cmd_key = } to {setting = } encountered error: {e}")

    def verify_config(
            self,
            cmd_obj: CmdClassType,
            cmd_key: str,
            setting: Union[str, int, float],
            channel: int = None
    ) -> None:
        """Validates the set_opt method and informs the user if the command value was correctly set or not. """
        try:
            cmd_obj.is_valid_cmd_key(cmd_key)
            query = convert_value(self.query_scope(cmd_obj, cmd_key, channel=channel))

            if cmd_key == 'ch_gain' and isinstance(query, str) and 'rat' in query:
                query = float(query.split(',')[0])

            # numerical configurations should always be a complete match, unless the scope auto
            # sets since some settings do not have valid args
            if isinstance(setting, (int, float)) and query == setting:
                self.log.debug(f"'{cmd_key}' {query = } and {setting = } match.")

            # string configuration matching based on how close they are a match
            elif isinstance(setting, str) and fuzz.partial_ratio(query, setting) >= 80:
                self.log.debug(f"'{cmd_key}' {query = } and {setting = } match.")

            # query and configuration does not match
            else:
                self.log.warning(f"'{cmd_key}' {query = } and {setting = } do not match.")

        except Exception as e:
            self.log.error(f"Validating '{cmd_key}' set to '{setting}' encountered error: {e}")

    def is_valid_setting(self, cmd_obj: CmdClassType, cmd_key: str, setting: Union[str, int, float]) -> None:
        """
        Checks the validity of the command value being sent to the scope compared to the valid options provided
        by the user. If not valid, attempts to return default value if available, else raises an exception to avoid
        writing an invalid command to scope when it will also just result in an exception.
        """
        cmd_args = cmd_obj.fetch_args(cmd_key)

        if cmd_args is None:
            self.log.debug(f"cmd_key '{cmd_key}' does not have 'args' attribute.")
            return

        if not isinstance(cmd_args, (list, dict)):
            self.log.warning(f"{cmd_args = } must be a 'list' or 'dict'.")
            return

        if isinstance(cmd_args, list):
            if setting not in cmd_args:
                raise ValueError(f"{setting = } not in {cmd_args = }.")

            return

        if isinstance(setting, (int, float)):
            _max = cmd_args.get('max')
            _min = cmd_args.get('min')

            if _max is None or _min is None:
                raise ValueError(f"Cannot validate {setting = } without both 'max' and 'min' values.")

            if not (_min <= setting <= _max):
                raise ValueError(f"{setting = } not within [{_min}, {_max}].")
        else:
            raise ValueError(f"{setting = } is not a valid type (i.e int, float or str).")
