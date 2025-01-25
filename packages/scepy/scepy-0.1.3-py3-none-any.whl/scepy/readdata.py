import pandas as pd
from .sced import sced  # Ensure compatibility with the updated sced class

def readdata(file, cvar="case", pvar="phase", dvar="values", mvar="mt", 
             sort_cases=False, phase_names=None, sep=",", dec="."):
    """
    Imports a single-case data file and converts it into an sced instance for analysis.
    
    Parameters:
    - file (str): Path to the file (CSV or Excel) containing the data.
    - cvar (str): Column name for the case variable. Default is "case".
    - pvar (str): Column name for the phase variable. Default is "phase".
    - dvar (str): Column name for the dependent variable. Default is "values".
    - mvar (str): Column name for the measurement time variable. If not in file, it's generated.
    - sort_cases (bool): Whether to sort the data by cases. Default is False.
    - phase_names (list): Optional list to rename phases, e.g., ["A", "B"].
    - sep (str): Column separator for CSV files. Default is ",".
    - dec (str): Decimal point character. Default is ".".
    
    Returns:
    - sced instance: An sced object with the loaded data.
    """
    
    # Determine file type and read data accordingly
    if file.endswith('.csv'):
        df = pd.read_csv(file, sep=sep, decimal=dec)
    elif file.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")

    # Check for essential columns and rename them if present
    required_columns = {pvar: 'phase', dvar: 'values'}
    if mvar in df.columns:
        required_columns[mvar] = 'mt'
    
    for original_name, new_name in required_columns.items():
        if original_name not in df.columns:
            raise ValueError(f"CSV/Excel file must contain '{original_name}' column.")
        df = df.rename(columns={original_name: new_name})

    # Add default 'case' column if missing
    if cvar not in df.columns:
        df['case'] = "Case1"  # Default case name for single-case data
    else:
        df = df.rename(columns={cvar: 'case'})
    
    # Add 'mt' column if missing
    if 'mt' not in df.columns:
        df['mt'] = range(1, len(df) + 1)

    # Assign phase names if provided
    if phase_names:
        phase_mapping = dict(zip(df['phase'].unique(), phase_names))
        df['phase'] = df['phase'].map(phase_mapping)

    # Sort by case if requested
    if sort_cases:
        df = df.sort_values(by=['case', 'mt']).reset_index(drop=True)
    
    # Convert to sced instance
    sced_instance = sced(data=df)
    
    return sced_instance
