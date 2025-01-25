import pandas as pd
import numpy as np
from .sced import sced
from .prepare_sced import prepare_sced

def pnd(data, dvar, pvar, decreasing=False, phases=("A", "B")):
    """
    Calculates the Percent Non-Overlapping Data (PND) for SCED data.

    Parameters:
    - data: List of Pandas DataFrames (single-case data format).
    - dvar: Dependent variable name.
    - pvar: Phase variable name.
    - decreasing: Whether PND should calculate a decrease in phase B (default: False).
    - phases: Tuple of phase names to analyze (default: ("A", "B")).

    Returns:
    - DataFrame: A structured table with PND, total points in phase B, and count of points exceeding A's max/min.
    """
    # Prepare the data
    data = prepare_sced(data, dvar, pvar, na_rm=True)

    results = []
    warnings = []
    
    for idx, case in enumerate(data):
        # Extract phases A and B
        try:
            phase_a = case[case[pvar] == phases[0]][dvar].values
            phase_b = case[case[pvar] == phases[1]][dvar].values
        except KeyError:
            warnings.append(f"Missing phase {phases} in case {idx + 1}. Skipping case.")
            continue
        
        # Check for empty phases
        if len(phase_a) == 0 or len(phase_b) == 0:
            warnings.append(f"Empty phase A or B in case {idx + 1}. Skipping case.")
            continue
        
        # Calculate PND
        n_b = len(phase_b)
        if decreasing:
            exceeds = np.sum(phase_b < np.min(phase_a))
        else:
            exceeds = np.sum(phase_b > np.max(phase_a))
        
        pnd_value = (exceeds / n_b) * 100 if n_b > 0 else 0
        results.append({"Case": f"Case{idx + 1}", "PND (%)": pnd_value, "Total B": n_b, "Exceeds": exceeds})
    
    # Convert results to DataFrame
    results_df = pd.DataFrame(results)
    
    # Add mean row
    if not results_df.empty:
        mean_row = {
            "Case": "Mean",
            "PND (%)": results_df["PND (%)"].mean(),
            "Total B": results_df["Total B"].sum(),
            "Exceeds": results_df["Exceeds"].sum(),
        }
        results_df = pd.concat([results_df, pd.DataFrame([mean_row])], ignore_index=True)
    
    # Print warnings
    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"  - {warning}")
    
    return results_df