# Describe Function

The `describe` function computes descriptive statistics for single-case experimental data. It provides detailed summaries of each case and phase, including measures such as mean, median, standard deviation, and trend.

## Function Overview

### Parameters
- `data`: A `SingleCaseData` instance or a pandas DataFrame containing the data.

### Returns
- A pandas DataFrame containing descriptive statistics for each case and phase.

## Descriptive Statistics
The function calculates the following metrics for each phase:
- `n`: Number of observations.
- `mis`: Number of missing values.
- `m`: Mean of the phase data.
- `md`: Median of the phase data.
- `sd`: Standard deviation of the phase data.
- `mad`: Median absolute deviation.
- `min`: Minimum value in the phase data.
- `max`: Maximum value in the phase data.
- `trend`: Trend in the phase data over time.

## Example Usage

### Example 1: Compute Descriptive Statistics for SingleCaseData
```python
import pandas as pd
from scepy import describe, SingleCaseData

data = pd.DataFrame({
    "case": ["Case1", "Case1", "Case2", "Case2", "Case2"],
    "phase": ["A", "A", "A", "B", "B"],
    "values": [10, 15, 20, 25, 30],
    "mt": [1, 2, 3, 4, 5]
})

scd = SingleCaseData(data=data)
stats = describe(scd)
print(stats)
```

### Example 2: Compute Descriptive Statistics for DataFrame
```python
from scepy import describe

data = pd.DataFrame({
    "case": ["Case1", "Case1", "Case2", "Case2", "Case2"],
    "phase": ["A", "A", "A", "B", "B"],
    "values": [10, 15, 20, 25, 30],
    "mt": [1, 2, 3, 4, 5]
})

stats = describe(data)
print(stats)
```

### Example Output
```
                   n  mis     m    md    sd   mad   min   max  trend
case   phase                                                        
Case1  A       2    0  12.5  12.5   3.54   2.5    10    15   2.0
Case2  A       1    0  20.0  20.0    NaN    0.0    20    20   NaN
       B       2    0  27.5  27.5   3.54   2.5    25    30   2.5
```

### Notes
- If no `case` column is present, the function treats the data as a single case.
- The `trend` metric depends on the relationship between measurement time and values.