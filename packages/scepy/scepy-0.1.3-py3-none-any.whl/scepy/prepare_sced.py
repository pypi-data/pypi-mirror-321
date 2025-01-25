import pandas as pd
import numpy as np

def prepare_sced(data, dvar, pvar, na_rm=False):
    """
    Prepares SCED data by ensuring conformity, handling missing values, and setting phases as categories.

    Parameters:
    - data: List of Pandas DataFrames.
    - dvar: Dependent variable name.
    - pvar: Phase variable name.
    - na_rm: Whether to remove rows with missing values in the dependent variable.

    Returns:
    - List of cleaned Pandas DataFrames.
    """
    prepared_data = []
    for case in data:
        case = case.copy()
        
        # Drop rows with NA in the dependent variable
        if na_rm:
            case = case.dropna(subset=[dvar])
        
        # Ensure the phase variable is categorical
        case[pvar] = case[pvar].astype('category')
        case[pvar] = case[pvar].cat.remove_unused_categories()
        
        prepared_data.append(case)
    return prepared_data