# Variable Management Functions

The functions in `variable_management.py` allow users to update variable names in single-case experimental data frames. These utilities ensure consistent naming for dependent variables, measurement time, and phase variables, making data preparation and analysis more straightforward.

---

## `set_vars`

### Description
The `set_vars` function updates the variable names in a single-case data frame (`scdf`). It renames the `values`, `mt`, and `phase` columns to the specified dependent variable (`dvar`), measurement time (`mvar`), and phase variable (`pvar`), respectively.

### Parameters
- `data` (DataFrame): A pandas DataFrame containing single-case data.
- `dvar` (str): The name of the dependent variable.
- `mvar` (str): The name of the measurement-time variable.
- `pvar` (str): The name of the phase variable.

### Returns
- `DataFrame`: A new DataFrame with updated column names.

### Example
```python
import pandas as pd
from scepy.variable_management import set_vars

data = pd.DataFrame({
    "values": [10, 15, 20],
    "mt": [1, 2, 3],
    "phase": ["A", "A", "B"]
})

updated_data = set_vars(data, dvar="measurements", mvar="time", pvar="stage")
print(updated_data)
```

**Output**:
```
   measurements  time stage
0            10     1     A
1            15     2     A
2            20     3     B
```

---

## `set_dvar`

### Description
The `set_dvar` function updates the name of the dependent variable (`dvar`) in a single-case data frame.

### Parameters
- `data` (DataFrame): A pandas DataFrame containing single-case data.
- `dvar` (str): The name of the dependent variable.

### Returns
- `DataFrame`: A new DataFrame with the updated dependent variable name.

### Example
```python
from scepy.variable_management import set_dvar

data = pd.DataFrame({
    "values": [10, 15, 20],
    "mt": [1, 2, 3],
    "phase": ["A", "A", "B"]
})

updated_data = set_dvar(data, dvar="measurements")
print(updated_data)
```

**Output**:
```
   measurements  mt phase
0            10   1     A
1            15   2     A
2            20   3     B
```

---

## `set_mvar`

### Description
The `set_mvar` function updates the name of the measurement-time variable (`mvar`) in a single-case data frame.

### Parameters
- `data` (DataFrame): A pandas DataFrame containing single-case data.
- `mvar` (str): The name of the measurement-time variable.

### Returns
- `DataFrame`: A new DataFrame with the updated measurement-time variable name.

### Example
```python
from scepy.variable_management import set_mvar

data = pd.DataFrame({
    "values": [10, 15, 20],
    "mt": [1, 2, 3],
    "phase": ["A", "A", "B"]
})

updated_data = set_mvar(data, mvar="time")
print(updated_data)
```

**Output**:
```
   values  time phase
0      10     1     A
1      15     2     A
2      20     3     B
```

## `set_pvar`

### Description
The `set_pvar` function updates the name of the phase variable (`pvar`) in a single-case data frame.

### Parameters
- `data` (DataFrame): A pandas DataFrame containing single-case data.
- `pvar` (str): The name of the phase variable.

### Returns
- `DataFrame`: A new DataFrame with the updated phase variable name.

### Example
```python
from scepy.variable_management import set_pvar

data = pd.DataFrame({
    "values": [10, 15, 20],
    "mt": [1, 2, 3],
    "phase": ["A", "A", "B"]
})

updated_data = set_pvar(data, pvar="stage")
print(updated_data)
```

**Output**:
```
   values  mt stage
0      10   1     A
1      15   2     A
2      20   3     B
```


## Notes
- All functions create a copy of the input DataFrame and return a modified version, leaving the original DataFrame unchanged.
- Column names are updated only if they match `values`, `mt`, or `phase`. If the DataFrame does not contain these columns, no changes will be made.
- These functions streamline the process of renaming columns in single-case experimental datasets, ensuring consistency across analyses.