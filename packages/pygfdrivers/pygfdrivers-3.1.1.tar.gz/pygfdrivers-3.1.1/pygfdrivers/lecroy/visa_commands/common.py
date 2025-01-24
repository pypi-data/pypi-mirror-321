from typing import TYPE_CHECKING

from pygfdrivers.common.base_command import VisaCommand

from gf_data_models.common.device.cmd import create_cmd_class, CmdClassType

if TYPE_CHECKING:
    from ..lecroy_visa_scope import LecroyVisaScope


def init_common_cmds():
    common: CmdClassType = create_cmd_class('Common')
    common.add_cmd(key='idn', cmd='*idn')
    common.add_cmd(key='arm', cmd='arm')
    common.add_cmd(key='stop', cmd='stop')
    common.add_cmd(key='reset', cmd='*rst')
    common.add_cmd(key='status', cmd='inr')
    common.add_cmd(key='op_complete', cmd='*opc')
    common.add_cmd(key='clear_status', cmd='*cls')
    common.add_cmd(key='single', cmd='trmd single')
    common.add_cmd(key='comm_header', cmd='chdr', args=['long', 'short', 'off'])
    common.add_cmd(key='save', cmd='*sav', args=[1, 2, 3, 4, 5, 6], default=6)
    common.add_cmd(key='recall', cmd='*rcl', args=[1, 2, 3, 4, 5, 6], default=0)
    return common


class LecroyCommon(VisaCommand):
    def __init__(self, scope: 'LecroyVisaScope') -> None:
        super().__init__(scope)

        self.common_cmds = init_common_cmds()

        if self.is_pdv:
            self.common_cmds.add_cmd(key='store_panel', cmd='stpn', args=['hdd', 'usb', 'micro'], default='hdd')
            self.common_cmds.add_cmd(key='recall_panel', cmd='rcpn', args=['hdd', 'usb', 'micro'], default='hdd')
            self.common_cmds.add_cmd(key='panel_setup', cmd='pnsu')

    @property
    def idn(self) -> str:
        _idn = self.query(self.common_cmds, 'idn')
        return _idn.lower()

    @property
    def op_complete(self) -> bool:
        _op_complete = self.query(self.common_cmds, 'op_complete')
        return bool(int(_op_complete))

    @op_complete.setter
    def op_complete(self, state: bool) -> None:
        self.write(self.common_cmds, 'op_complete', setting=int(state))

    def reset(self) -> None:
        self.log.debug("Resetting scope to factory default settings.")
        self.write(self.common_cmds, 'reset')

    def comm_header(self, setting: str) -> None:
        try:
            self.write(self.common_cmds, 'comm_header', setting=setting.lower())
        except Exception as e:
            self.log.error(f"Setting comm_header encountered error: {e}")

    @property
    def status(self) -> int:
        _status = self.query(self.common_cmds, 'status')
        return int(_status)

    def clear_status(self) -> None:
        self.log.debug("Clearing scope status")
        self.write(self.common_cmds, 'clear_status')

    def single_mode(self) -> None:
        self.write(cmd='arm')

    def stop_mode(self) -> None:
        self.write(cmd='stop')

    def run_mode(self) -> None:
        raise NotImplementedError

    def save(self, setup_num: int) -> None:
        cmd_key = 'save'
        setup_opts = self.common_cmds.fetch_args(cmd_key)
        setup_default = self.common_cmds.fetch_default(cmd_key)

        try:
            if setup_num not in setup_opts:
                self.log.warning(f"save: setup '{setup_num}' not in available options:'{setup_opts}',"
                                 f" default to '{setup_default}'.")
                setup_num = setup_default

            self.write(self.common_cmds, 'save', setting=setup_num)
        except Exception as e:
            self.log.error(f"Saving scope settings to setup '{setup_num}' encountered error: {e}")

    def recall(self, setup_num: int) -> None:
        cmd_key = 'recall'
        setup_opts = self.common_cmds.fetch_args(cmd_key)
        setup_default = self.common_cmds.fetch_default(cmd_key)

        try:
            if setup_num not in setup_opts:
                self.log.warning(f"recall: setup '{setup_num}' not in available options:'{setup_opts}',"
                                 f" default to '{setup_default}'.")
                setup_num = setup_default

            self.log.debug(f"Recalling scope setup '{setup_num}'.")
            self.write(self.common_cmds, 'recall', setting=setup_num)
        except Exception as e:
            self.log.error(f"Recalling scope settings from setup '{setup_num}' encountered error: {e}")

    def store_panel(self, store_loc: str, file_name: str) -> None:
        if self.is_pdv:
            cmd_key = 'store_panel'
            cmd_str = f"{self.common_cmds.fetch_cmd(cmd_key)}"
            store_opts = self.common_cmds.fetch_args(cmd_key)
            store_default = self.common_cmds.fetch_default(cmd_key)

            try:
                if store_loc not in store_opts:
                    self.log.warning(f"store_panel: storage location '{store_loc}' not in available options:"
                                     f"'{store_opts}', default to '{store_default}'.")
                    store_loc = store_default

                self.log.debug(f"Storing scope setup via '{store_loc}' in '{file_name}'.")
                self.write(cmd=f"{cmd_str} disk,{store_loc},file,{file_name}")
            except Exception as e:
                self.log.error(f"Storing scope settings via '{store_loc}' in '{file_name}' encountered error: {e}")

    def recall_panel(self, store_loc: str, file_name: str) -> None:
        if self.is_pdv:
            cmd_key = 'recall_panel'
            cmd_str = f"{self.common_cmds.fetch_cmd(cmd_key)}"
            store_opts = self.common_cmds.fetch_args(cmd_key)
            store_default = self.common_cmds.fetch_default(cmd_key)

            try:
                if store_loc not in store_opts:
                    self.log.warning(
                        f"recall_panel: storage location '{store_loc}' not in available options:"
                        f"'{store_opts}', default to '{store_default}'."
                    )
                    store_loc = store_default

                self.log.debug(f"Recalling scope setup via '{store_loc}' in '{file_name}'.")
                self.write(cmd=f"{cmd_str} disk,{store_loc},file,{file_name}")
            except Exception as e:
                self.log.error(f"Recalling scope settings via '{store_loc}' in '{file_name}' encountered error: {e}")

    def panel_setup(self) -> str:
        if self.is_pdv:
            current_setup = self.query(self.common_cmds, 'panel_setup')
            return current_setup
