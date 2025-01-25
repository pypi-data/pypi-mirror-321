# Fill Missing Function

The `fill_missing` function handles missing data in single-case experimental data by replacing missing values in the dependent variable column. This ensures a complete dataset for analysis.

## Function Overview

### Parameters
- `data`: A pandas DataFrame representing single-case data.
- `dvar`: The name of the dependent variable column where missing values may occur.
- `mvar`: The name of the measurement time variable column used to ensure the data is sorted correctly.
- `na_rm` (bool): If `True`, missing values in the dependent variable column will be filled using linear interpolation. The default value is `True`.

### Returns
- A pandas DataFrame with missing data points in the dependent variable column filled.

## Example Usage

### Example 1: Fill Missing Values with Interpolation
```python
import pandas as pd
import numpy as np
from scepy.data_processing import fill_missing

data = pd.DataFrame({
    "values": [10, np.nan, 20, np.nan, 40],
    "mt": [1, 2, 3, 4, 5]
})

filled_data = fill_missing(data, dvar="values", mvar="mt")
print(filled_data)
```

**Output**:
```
   values  mt
0    10.0   1
1    15.0   2
2    20.0   3
3    30.0   4
4    40.0   5
```

### Example 2: Skip Interpolation
```python
filled_data = fill_missing(data, dvar="values", mvar="mt", na_rm=False)
print(filled_data)
```

**Output**:
```
   values  mt
0    10.0   1
1     NaN   2
2    20.0   3
3     NaN   4
4    40.0   5
```

## Notes
- The data is sorted by the measurement time variable (`mvar`) to ensure proper interpolation of missing values.
- Interpolation is performed using the `linear` method, which estimates missing values based on surrounding data points.
- If `na_rm` is set to `False`, missing values are not replaced and remain as `NaN` in the output.