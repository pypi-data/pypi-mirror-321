import re
import logging
from typing import Optional
from pyvisa import ResourceManager
from pyvisa.resources import Resource

log = logging.getLogger(__name__)


def fetch_lecroy_series(scope: Resource = None, ip_addr = None) -> Optional[str]:
    if scope is None and ip_addr is None:
        raise ValueError("Need either scope or ip_addr passed")

    scope = scope or ResourceManager().open_resource(f"TCPIP0::{ip_addr}::inst0::INSTR")
    scope_id = scope.query('*IDN?')

    # Extract the model information from query
    if match := re.search(r',(\w[\w\-]*),', scope_id, re.IGNORECASE):
        model = match.group(1)

        if model == "MCM-ZI-A":
            return 'LabMaster'
        elif model == "WR640ZI":
            return 'WaveRunner'
        elif "T3DSO2" in model:
            model_end = model[len("T3DSO2"):]

            if model_end.startswith("20"):
                return 'T3DSO2204A'
            elif model_end.startswith("10"):
                return 'T3DSO2104'
    else:
        log.error(f"No matching lecroy model found for {scope_id}")
        return None