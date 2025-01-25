import pandas as pd
import numpy as np

def run_length_encoding(values):
    """
    Computes the run-length encoding of a sequence.
    
    Parameters:
    - values: List or array of values.

    Returns:
    - A dictionary with 'lengths' and 'values'.
    """
    if len(values) == 0:
        return {"lengths": [], "values": []}
    
    diff = np.diff(values)
    changes = np.where(diff != 0)[0] + 1
    indices = np.append([0], changes)
    lengths = np.diff(np.append(indices, len(values)))
    encoded_values = values[indices]
    
    return {"lengths": lengths.tolist(), "values": encoded_values.tolist()}

def combined(data, phases=(1, 2), set_phases=True, phase_names=("A", "B"), pvar=None):
    """
    Combines specified phases from single-case data and reorganizes data for analysis.
    
    Parameters:
    - data: List of Pandas DataFrames (single-case data format).
    - phases: Tuple of phase indices or names to combine (default: (1, 2)).
    - set_phases: Whether to rename phases using `phase_names` (default: True).
    - phase_names: Tuple of names for the combined phases (default: ("A", "B")).
    - pvar: Phase variable name (default: inferred from data).

    Returns:
    - dict: Contains the following keys:
        - 'data': List of updated DataFrames.
        - 'designs': List of phase designs for each case.
        - 'N': Number of cases processed.
        - 'phases_A': Phases corresponding to A.
        - 'phases_B': Phases corresponding to B.
        - 'phases': Dictionary of original and new phases.
        - 'warnings': List of warnings encountered during processing.
    """
    if pvar is None:
        pvar = "phase"  # Default phase variable
    
    warnings = []
    dropped_cases = []
    designs = []
    updated_data = []
    original_phases = []
    new_phases = []
    
    for idx, case in enumerate(data):
        # Run-length encoding of the phase column
        try:
            design = run_length_encoding(case[pvar].values)
        except KeyError:
            warnings.append(f"Phase variable '{pvar}' not found in case {idx + 1}. Case skipped.")
            dropped_cases.append(idx)
            continue
        
        phases_A, phases_B = phases
        phase_values = design["values"]
        
        # Validate phases
        if isinstance(phases, (tuple, list)) and not all(phase in phase_values for phase in phases):
            warnings.append(f"Phases {phases} not found in case {idx + 1}. Case skipped.")
            dropped_cases.append(idx)
            continue
        
        # Compute indices for A and B phases
        A_indices = [i for i, value in enumerate(phase_values) if value in phases_A]
        B_indices = [i for i, value in enumerate(phase_values) if value in phases_B]
        
        if not A_indices or not B_indices:
            warnings.append(f"Phases {phases} not properly defined in case {idx + 1}. Case skipped.")
            dropped_cases.append(idx)
            continue
        
        # Convert run-length indices to row indices
        A_rows = [row for i in A_indices for row in range(design["lengths"][i])]
        B_rows = [row for i in B_indices for row in range(design["lengths"][i])]
        combined_rows = A_rows + B_rows
        
        # Subset data
        subset = case.iloc[combined_rows].copy()
        
        if set_phases:
            subset.loc[A_rows, pvar] = phase_names[0]
            subset.loc[B_rows, pvar] = phase_names[1]
        
        # Update results
        updated_data.append(subset)
        designs.append(design)
        original_phases.append(phase_values)
        new_phases.append([phase_names[0], phase_names[1]])
    
    # Remove dropped cases
    for idx in sorted(dropped_cases, reverse=True):
        del data[idx]
    
    # Prepare output
    output = {
        "data": updated_data,
        "designs": designs,
        "N": len(updated_data),
        "phases_A": phases[0],
        "phases_B": phases[1],
        "phases": {"original": original_phases, "new": new_phases},
        "warnings": warnings,
    }
    
    return output
