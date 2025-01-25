import pkg_resources
import requests

# Import all modules and functionalities
from .autocorr import autocorr
from .batchapply import batch_apply
from .case_selection import select_cases
from .cdc import calculate_trend, cdc
from .combine import combine
from .corrected_tau import kendall_full, corrected_tau
from .data_processing import fill_missing
from .data_transformation import moving_median, moving_mean, local_regression, transform_single_case
from .describe import describe
from .dummies_model import plm_dummy, add_model_dummies
from .formula_utils import create_fixed_formula, create_random_formula
from .hplm import add_dummies, define_formulas, fit_hierarchical_model, calculate_icc, hplm
from .ird import ird
from .nap import nap
from .outlier_handling import outlier
from .overlap import overlap
from .pand import pand
from .prepare_data import opt, revise_names, _check_scdf, check_scdf, prepare_scdf
from .rank_transformation import ranks
from .readdata import readdata
from .select_case import select_case
from .singlecasedf import SingleCaseData
from .stat_utils import mad, trend
from .trend import trend
from .variable_management import set_vars, set_dvar, set_mvar, set_pvar

# Check for the latest version of the package
def check_for_updates():
    current_version = pkg_resources.get_distribution("scepy").version
    try:
        response = requests.get("https://pypi.org/pypi/scepy/json", timeout=5)
        if response.status_code == 200:
            latest_version = response.json()["info"]["version"]
            if latest_version != current_version:
                print(
                    f"\033[93m[WARNING] A newer version of scepy ({latest_version}) is available. "
                    f"Please update your package using the command:\033[0m\n"
                    f"    pip install --upgrade scepy"
                )
    except Exception as e:
        print(f"\033[91m[ERROR] Failed to check for updates: {e}\033[0m")

# Run the version check
check_for_updates()

# Specify what should be exposed when importing *
__all__ = [
    'autocorr', 'batch_apply', 'select_cases', 'calculate_trend', 'cdc', 'combine',
    'kendall_full', 'corrected_tau', 'fill_missing', 'moving_median', 'moving_mean',
    'local_regression', 'transform_single_case', 'describe', 'plm_dummy', 'add_model_dummies',
    'create_fixed_formula', 'create_random_formula', 'add_dummies', 'define_formulas',
    'fit_hierarchical_model', 'calculate_icc', 'hplm', 'ird', 'nap', 'outlier', 'overlap', 'pand',
    'opt', 'revise_names', '_check_scdf', 'check_scdf', 'prepare_scdf', 'ranks', 'readdata',
    'select_case', 'SingleCaseData', 'mad', 'trend', 'set_vars', 'set_dvar', 'set_mvar', 'set_pvar'
]
