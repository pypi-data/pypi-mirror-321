import pandas as pd
import numpy as np
from scipy.stats import binomtest  # Updated import
from sklearn.linear_model import LinearRegression

def calculate_trend(single_case_data, dvar, mvar, method="OLS"):
    data = single_case_data.df
    
    if method == "OLS":
        model = LinearRegression()
        model.fit(data[[mvar]], data[dvar])
        return model

    elif method == "bisplit":
        mid = len(data) // 2
        first_half = data.iloc[:mid]
        second_half = data.iloc[mid:]
        x_medians = [first_half[mvar].median(), second_half[mvar].median()]
        y_medians = [first_half[dvar].median(), second_half[dvar].median()]
        
        bisplit_df = pd.DataFrame({mvar: x_medians, dvar: y_medians})
        model = LinearRegression()
        model.fit(bisplit_df[[mvar]], bisplit_df[dvar])
        return model

    elif method == "trisplit":
        third = len(data) // 3
        first_part = data.iloc[:third]
        last_part = data.iloc[-third:]
        
        x_medians = [first_part[mvar].median(), last_part[mvar].median()]
        y_medians = [first_part[dvar].median(), last_part[dvar].median()]
        
        trisplit_df = pd.DataFrame({mvar: x_medians, dvar: y_medians})
        model = LinearRegression()
        model.fit(trisplit_df[[mvar]], trisplit_df[dvar])
        return model

    else:
        raise ValueError("Invalid trend method specified. Choose 'OLS', 'bisplit', or 'trisplit'.")

def cdc(single_case_data, dvar="values", pvar="phase", mvar="mt", method="OLS", 
        conservative=0.25, decreasing=False):
    data = single_case_data.df
    
    phase_A = data[data[pvar] == "A"]
    phase_B = data[data[pvar] == "B"]
    
    if len(phase_A) < 5 or len(phase_B) < 5:
        raise ValueError("Each phase must contain at least 5 data points for selected method.")

    trend_model = calculate_trend(single_case_data, dvar, mvar, method)
    
    phase_B_pred = trend_model.predict(phase_B[[mvar]])
    
    sd_A = phase_A[dvar].std()
    mean_A = phase_A[dvar].mean()
    cdc_exc = 0

    if not decreasing:
        for i, actual in enumerate(phase_B[dvar]):
            pred = phase_B_pred[i]
            if actual > pred + (conservative * sd_A) and actual > mean_A + (conservative * sd_A):
                cdc_exc += 1
    else:
        for i, actual in enumerate(phase_B[dvar]):
            pred = phase_B_pred[i]
            if actual < pred - (conservative * sd_A) and actual < mean_A - (conservative * sd_A):
                cdc_exc += 1
    
    p_value = binomtest(cdc_exc, len(phase_B), alternative="greater").pvalue  # Updated function usage
    systematic_change = "systematic change" if p_value < 0.05 else "no change"
    
    results_text = f"""
    Change Detection Criteria (CDC) Analysis
    ----------------------------------------
    Method: {method}
    Conservative Threshold: {conservative}
    Direction of Change: {"Decreasing" if decreasing else "Increasing"}
    
    Phase B Exceedances: {cdc_exc} out of {len(phase_B)}
    CDC P-Value: {p_value:.4f}
    Result: {systematic_change}
    """
    
    return results_text
