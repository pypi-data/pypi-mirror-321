def select_case(scdf, *cases):
    """
    Selects specified cases from a single-case data frame (scdf).

    Parameters:
    - scdf (DataFrame): The DataFrame containing single-case data.
    - *cases (str): Case names to select.

    Returns:
    - DataFrame: A filtered DataFrame containing only the specified cases.

    Example:
    from scepy import sced, variable_management

    # Example DataFrame
    data = sced(data={"values": [10, 15, 20, 25], 
                      "mt": [1, 2, 3, 4], 
                      "phase": ["A", "A", "B", "B"], 
                      "case": ["Case1", "Case1", "Case2", "Case2"]}).df

    # Select specific cases
    filtered_data = variable_management.select_case(data, "Case1")
    print(filtered_data)
    """
    # Check if any cases are provided
    if not cases:
        raise ValueError("Please specify at least one case to select.")
    
    # Filter the DataFrame based on the specified cases
    selected_df = scdf[scdf['case'].isin(cases)]
    
    return selected_df
