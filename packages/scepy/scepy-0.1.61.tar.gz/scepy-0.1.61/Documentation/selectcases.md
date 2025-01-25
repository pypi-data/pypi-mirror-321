
# Select Cases

`select_case` is a function designed to filter a single-case data frame (`scdf`) by selecting specific cases. It helps users focus on a subset of their data by isolating rows that match the specified case names. This is particularly useful in single-case experimental designs where data is often grouped by case identifiers.

## Function Overview

### Parameters
- `scdf` (DataFrame): A pandas DataFrame containing single-case experimental data. It must include a column named `case`.
- `*cases` (str): One or more case names to be selected from the `scdf`.

### Returns
- `DataFrame`: A filtered pandas DataFrame containing only the rows for the specified cases.

### Behavior
- If no case names are provided, the function raises a `ValueError`.
- The filtering is case-sensitive, so the specified case names must match the `case` column exactly.

## Examples

### Example 1: Select a Single Case
This example demonstrates how to select data for a single case.

```python
import pandas as pd
from scepy import select_case

# Example single-case DataFrame
data = pd.DataFrame({
    "case": ["Case1", "Case1", "Case2", "Case3", "Case3"],
    "phase": ["A", "B", "A", "A", "B"],
    "values": [10, 12, 15, 20, 25]
})

# Select a single case
filtered_data = select_case(data, "Case1")
print(filtered_data)
```

**Output**:
```
    case phase  values
0  Case1     A      10
1  Case1     B      12
```

### Example 2: Select Multiple Cases
You can select multiple cases by passing their names as additional arguments.

```python
# Select multiple cases
filtered_data = select_case(data, "Case1", "Case3")
print(filtered_data)
```

**Output**:
```
    case phase  values
0  Case1     A      10
1  Case1     B      12
3  Case3     A      20
4  Case3     B      25
```

### Example 3: Handle Missing Case Names
If no case names are provided, the function raises a `ValueError` to notify the user.

```python
try:
    filtered_data = select_case(data)
except ValueError as e:
    print(e)
```

**Output**:
```
Please specify at least one case to select.
```

### Example 4: Case Sensitivity
The `select_case` function is case-sensitive. If the case name does not match exactly, it will not return any data for that case.

```python
# Attempt to select a case with incorrect capitalization
filtered_data = select_case(data, "case1")
print(filtered_data)
```

**Output**:
```
Empty DataFrame
Columns: [case, phase, values]
Index: []
```

## Notes
- Ensure the `scdf` DataFrame contains a `case` column; otherwise, a `KeyError` will be raised.
- Pass case names as separate arguments, such as `"Case1", "Case2"`. Lists or other collection types are not supported.
- This function is a utility for filtering and isolating specific cases, making it ideal for single-case experimental data analysis.
