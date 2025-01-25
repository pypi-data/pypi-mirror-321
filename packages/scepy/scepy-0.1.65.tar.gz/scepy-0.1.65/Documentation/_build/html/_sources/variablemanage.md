# variable management

The `variable_management` module in the SCEPY package provides utility functions to update and manage variable names in single-case experimental data frames (`scdf`). These functions allow users to rename key variables like dependent variable (`dvar`), measurement-time variable (`mvar`), and phase variable (`pvar`) to suit their analysis needs.

## Functions Overview

### **1. `set_vars`**

```python
set_vars(data, dvar, mvar, pvar)
```

#### Description:
Sets the analysis variables (`dvar`, `mvar`, `pvar`) in a single-case data frame.

#### Parameters:
- `data` (`DataFrame`): A single-case data frame.
- `dvar` (`str`): Name of the dependent variable.
- `mvar` (`str`): Name of the measurement-time variable.
- `pvar` (`str`): Name of the phase variable.

#### Returns:
- `DataFrame`: The updated data frame with the specified variable names.

#### Example:
```python
from scepy import sced, variable_management

# Original data frame
data = sced(data={"values": [10, 15, 20], "mt": [1, 2, 3], "phase": ["A", "A", "B"]}).df

# Update variable names
updated_data = variable_management.set_vars(data, dvar="observations", mvar="time", pvar="condition")
print(updated_data)
```

**Output:**
```
   observations  time condition
0            10     1        A
1            15     2        A
2            20     3        B
```



### **2. `set_dvar`**

```python
set_dvar(data, dvar)
```

#### Description:
Updates the dependent variable name in the data frame.

#### Parameters:
- `data` (`DataFrame`): A single-case data frame.
- `dvar` (`str`): The new name for the dependent variable.

#### Returns:
- `DataFrame`: The updated data frame with the specified dependent variable name.

#### Example:
```python
updated_data = variable_management.set_dvar(data, dvar="observations")
print(updated_data)
```



### **3. `set_mvar`**

```python
set_mvar(data, mvar)
```

#### Description:
Updates the measurement-time variable name in the data frame.

#### Parameters:
- `data` (`DataFrame`): A single-case data frame.
- `mvar` (`str`): The new name for the measurement-time variable.

#### Returns:
- `DataFrame`: The updated data frame with the specified measurement-time variable name.

#### Example:
```python
updated_data = variable_management.set_mvar(data, mvar="time")
print(updated_data)
```



### **4. `set_pvar`**

```python
set_pvar(data, pvar)
```

#### Description:
Updates the phase variable name in the data frame.

#### Parameters:
- `data` (`DataFrame`): A single-case data frame.
- `pvar` (`str`): The new name for the phase variable.

#### Returns:
- `DataFrame`: The updated data frame with the specified phase variable name.

#### Example:
```python
updated_data = variable_management.set_pvar(data, pvar="condition")
print(updated_data)
```



## Notes

- The original column names (`values`, `mt`, `phase`) are replaced by the specified names.
- Use these utilities to align your data frame's variable names with your analysis or reporting requirements.


## Integration with SCEPY

This module integrates smoothly with the rest of the SCEPY package. For example, when creating a `sced` instance, you can directly use the updated data frame:

```python
from scepy import sced, variable_management

# Original data frame
data = sced(data={"values": [10, 15, 20], "mt": [1, 2, 3], "phase": ["A", "A", "B"]}).df

# Update variable names
updated_data = variable_management.set_vars(data, dvar="observations", mvar="time", pvar="condition")

# Use the updated data in a new sced instance
updated_case = sced(data=updated_data)
print(updated_case.df)
```

**Output:**
```
   observations  time condition
0            10     1        A
1            15     2        A
2            20     3        B
```