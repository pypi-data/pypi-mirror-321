"""
SCEPY: Single-Case Experiment Python Package
"""

from .combined import *
from .pnd import *
from .prepared_sced import *
from .readdata import *
from .sced import *
from .select_case import *
from .variable_management import *

# Version check on import
from ._version import version as __version__

import requests
import warnings

def check_new_version():
    try:
        response = requests.get("https://pypi.org/pypi/scepy/json", timeout=3)
        response.raise_for_status()
        latest_version = response.json()["info"]["version"]
        if latest_version != __version__:
            warnings.warn(
                f"A newer version ({latest_version}) of SCEPY is available. "
                f"Please update using 'pip install --upgrade scepy'."
            )
    except Exception:
        pass  # Ignore any errors during the version check

check_new_version()
