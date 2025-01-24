import re
import logging
from typing import Optional
from pyvisa import ResourceManager
from pyvisa.resources import Resource

log = logging.getLogger(__name__)


def fetch_keysight_series(scope: Resource = None, ip_addr = None) -> Optional[str]:
    if scope is None and ip_addr is None:
        raise ValueError("Need either scope or ip_addr passed")

    scope = scope or ResourceManager().open_resource(f"TCPIP0::{ip_addr}::inst0::INSTR")
    scope_id = scope.query('*IDN?')

    # FIXME
    # MXR108A scope response from IDN query returns no model number so have to do a bandaid solution
    if 'MY61310124' in scope_id:
        return 'MXR'

    # Extract the model and series information from query
    if match := re.search(r'(MXR|DSO[-X]*|DSO)\s*(\d+)', scope_id, re.IGNORECASE):
        model, series = match.groups()

        if model == "MXR":
            return 'MXR'
        elif model in ["DSOX", "DSO-X"]:
            if series.startswith("12"):
                return 'DSOX1200'
            elif series.startswith("20"):
                return 'DSOX2000'
            elif series.startswith("40"):
                return 'DSOX4000'
            return 'DSOX'
        elif model == "DSO":
            if series.startswith("50"):
                return 'DSO5000'
            return 'DSO'
    else:
        log.error(f"No matching keysight model found for {scope_id}")
        return None


def fetch_num_channels(scope: Resource) -> Optional[int]:
    mxr108a_sn = 'MY61310124'
    mxr058a_sn = 'MY61310312'
    dsox2002a_sn1 = 'MY56274783'
    dsox2002a_sn2 = 'MY56274750'

    scope_id = scope.query('*IDN?')

    if mxr108a_sn in scope_id or mxr058a_sn in scope_id :
        return 8
    elif dsox2002a_sn1 in scope_id or dsox2002a_sn2 in scope_id:
        return 2
    else:
        return 4