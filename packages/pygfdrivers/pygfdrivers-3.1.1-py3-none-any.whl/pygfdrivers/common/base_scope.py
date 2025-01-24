from abc import ABC
from pydantic import BaseModel
from collections import defaultdict

from pygfdrivers.common.base_device import BaseDevice

from gf_data_models.dtacq.scope import DtacqSiteModel
from gf_data_models.factory.models import factory_models
from gf_data_models.lecroy.scope.channel import LecroyChannelModel
from gf_data_models.keysight.scope.channel import KeysightChannelModel
from gf_data_models.gf.digitizer.digitizer import GfChannelModel


class BaseScope(BaseDevice, ABC):
    def __init__(self, scope_config: BaseModel) -> None:
        super().__init__(scope_config)

        self.scope = None
        self.scope_series = None
        self.file_name = self.name

        self.scope_talk_delay = 0.1  # 0.1 not working for Lecroys
        self.scope_type = self.config.device.device_type

        self.init_scope_info()

    def init_scope_info(self) -> None:
        # TODO: Need to make this dynamic to the scope_info specific to the scope_type
        try:
            self.scope_info = factory_models.get(self.scope_type)()

            if self.scope_info is None:
                raise ValueError(f"Scope type '{self.scope_type}' does not have mapped scope_info model.'")

            self.fetch_config_metadata(self.scope_info)
            setattr(self.scope_info, 'device', self.config.device)

            if 'dtacq' in self.scope_type:
                setattr(self.scope_info, 'active_sites', self.config.active_sites)
            else:
                setattr(self.scope_info, 'active_channels', self.config.active_channels)

        except Exception as e:
            self.log.error(f"Initializing scope info encountered error: {e}")

    def clear_scope_info_data(self) -> None:
        if 'dtacq' in self.scope_type:
            setattr(self.scope_info, 'sites', defaultdict(DtacqSiteModel))
        elif 'keysight' in self.scope_type:
            setattr(self.scope_info, 'channels', defaultdict(KeysightChannelModel))
        elif 'lecroy' in self.scope_type:
            setattr(self.scope_info, 'channels', defaultdict(LecroyChannelModel))
        elif 'digitizer' in self.scope_type:
            setattr(self.scope_info, 'channels', defaultdict(GfChannelModel))
