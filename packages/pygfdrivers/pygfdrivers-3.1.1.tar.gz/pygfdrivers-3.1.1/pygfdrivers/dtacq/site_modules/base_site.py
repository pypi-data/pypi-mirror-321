from collections import defaultdict
from typing import List, Dict, Union, Any
from functools import cached_property
from acq400_hapi.acq400 import Acq400

from pygfdrivers.common.util.utilities import has_prop, has_setter

from gf_data_models.dtacq.scope import DtacqSiteModel, DtacqScopeModel


class BaseSite:
    def __init__(self, dtacq: Acq400, config: DtacqScopeModel) -> None:
        self.dtacq = dtacq
        self.log = self.dtacq.log
        self.carrier = self.dtacq.carrier
        self.config = config or self.dtacq.config

        self.master_site = None
        self.site_infos = self.dtacq.scope_info.sites
        self.sites_dict = self.carrier.modules.copy()

        self.site = None
        self.site_ch = ''
        self.site_num = ''
        self._source_id = defaultdict(lambda: defaultdict(dict))
        self._source_name = defaultdict(lambda: defaultdict(dict))

    def apply_site_config(
            self,
            active_sites: Dict[str, List[int]],
            site_configs: Dict[str, DtacqSiteModel]
    ) -> None:
        try:
            for site in active_sites:
                site_num = int(site.split('_')[1])
                self.site_num = str(site_num)
                self.site = self.sites_dict.get(site_num)

                if self.site is None:
                    raise ValueError(f"Site '{site_num}' not installed in carrier.")

                active_chs = active_sites[site]
                site_config = site_configs[site]

                for ch in active_chs:
                    self.site_ch = str(ch).zfill(2)
                    ch_config = site_config.channels[ch]

                    for field in ch_config.model_fields_set:
                        setting = getattr(ch_config, field)

                        if has_setter(self, field):
                            self.log.debug(f"[SITE: {site_num}] Setting channel '{ch}' '{field}' to '{setting}'...")
                            setattr(self, field, setting)

        except Exception as e:
            self.log.error(f"Applying site configuration encountered error: {e}")
            raise

    def fetch_site_config(
            self,
            active_sites: Dict[str, List[int]],
            site_infos: Dict[str, DtacqSiteModel]
    ) -> None:
        try:
            for site in active_sites:
                site_num = int(site.split('_')[1])
                self.site_num = str(site_num)
                self.site = self.sites_dict.get(site_num)

                if self.site is None:
                    raise ValueError(f"Site '{site_num}' not installed in carrier.")

                active_chs = active_sites[site]
                site_info = site_infos[site]

                for ch in active_chs:
                    self.site_ch = str(ch).zfill(2)
                    ch_info = site_info.channels[str(ch)]

                    for field in ch_info.model_fields:
                        if has_prop(self, field):
                            self.log.debug(f"[SITE: {site_num}] Fetching channel '{ch}' '{field}'...")
                            setattr(ch_info, field, getattr(self, field))

        except Exception as e:
            self.log.error(f"Fetching site configuration encountered error: {e}")

    def set_site(self, site: int = None, abs_ch: int = None) -> None:
        if site is None and abs_ch is not None:
            site, _ = divmod(abs_ch - 1, self.nchan)
            site += 1  # Adjust site number to start from 1

        self.site = self.sites_dict.get(site)

        if self.site is None:
            raise ValueError(f"No daq module, or wrong module type installed in this site.")

    def set_site_knob(self, site: int, site_ch: int, setter: str, set_value: Union[int, float, bool, str]) -> None:
        self.site_ch = str(site_ch).zfill(2)

        try:
            self.set_site(site)
            setattr(self, setter, set_value)
        except Exception as e:
            self.log.error(f"Setting '{setter}' for site '{site}', channel '{site_ch}' encountered error: {e}")

    def get_site_knob(self, site: int, site_ch: int, getter: str) -> Union[int, float, bool, str]:
        self.site_ch = str(site_ch).zfill(2)

        try:
            self.set_site(site)
            return getattr(self, getter)
        except Exception as e:
            self.log.error(f"Fetching '{getter}' for site '{site}', channel '{site_ch}' encountered error: {e}")

    # ------------------------------------------------------------------------------------
    # Read Only Methods
    # ------------------------------------------------------------------------------------

    @cached_property
    def max_srate(self) -> int:
        _max_srate = int(self.master_site.get_knob('MAX_KHZ')) * 1000
        return _max_srate

    @cached_property
    def min_srate(self) -> int:
        _min_srate = int(self.master_site.get_knob('MIN_KHZ')) * 1000
        return _min_srate

    @cached_property
    def nchan(self) -> int:
        _nchan = int(self.master_site.get_knob('NCHAN'))
        return _nchan
