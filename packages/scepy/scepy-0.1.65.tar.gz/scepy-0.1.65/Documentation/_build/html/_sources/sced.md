# SCED (Single Case Experiment Data)

The `sced` class is designed to help users create, manage, and analyze data for single-case experimental designs (SCED). This documentation provides an overview of its functionality, methods, and usage examples.


## Installation

To use the `sced` class, include the `sced.py` file in your working directory and import it into your script:

```python
from sced import sced
```

## Class Overview

The `sced` class simplifies the management of SCED data by organizing it into a structured DataFrame. It includes methods for applying phase designs, exporting data, and handling multiple cases.

### Key Features

- Automatically generates phase designs based on input values.
- Exports data in multiple formats (`csv`, `html`, `xlsx`).
- Combines multiple cases into a long-format DataFrame.
- Provides a clean and intuitive interface for data management.

## Creating an Instance of SCED

To initialize the `sced` class, you can provide data in one of two ways:

1. **Directly specify the data through arguments.**
2. **Provide a DataFrame with pre-existing columns.**

### Parameters

| Parameter      | Type        | Description                                                                 |
|----------------|-------------|-----------------------------------------------------------------------------|
| `values`       | list        | Dependent variable values (e.g., observed measurements).                   |
| `phase`        | list        | Phase identifiers (e.g., "A", "B").                                        |
| `case`         | str or list | Case name or list of case identifiers.                                     |
| `B_start`      | int         | Index where the "B" phase begins (alternative to providing `phase`).       |
| `mt`           | list        | Measurement time points (optional).                                        |
| `phase_design` | dict        | Custom phase design dictionary (e.g., `{"A": 5, "B": 10}`).                |
| `phase_starts` | dict        | Starting points for each phase (e.g., `{"A": 1, "B": 6}`).                 |
| `name`         | str         | Name of the case.                                                          |
| `dvar`, `pvar`, `mvar` | str | Column names for dependent variable, phase, and measurement time, respectively. |
| `data`         | DataFrame   | Existing DataFrame with data.                                              |


## Example Usage

### 1. Creating a Basic SCED Object

```python
from sced import sced

# Define data
values = [10, 15, 12, 14, 16, 20, 18, 25]
phase = ["A", "A", "A", "A", "B", "B", "B", "B"]
case = "Case 1"

# Initialize SCED object
case1 = sced(values=values, phase=phase, case=case)

# Print the DataFrame
print(case1.df)
```

**Output:**
```
   values  mt phase    case
0      10   1     A  Case 1
1      15   2     A  Case 1
2      12   3     A  Case 1
3      14   4     A  Case 1
4      16   5     B  Case 1
5      20   6     B  Case 1
6      18   7     B  Case 1
7      25   8     B  Case 1
```



### 2. Using a Phase Design

```python
# Define phase design
phase_design = {"A": 4, "B": 4}

# Initialize SCED object
case2 = sced(values=values, phase_design=phase_design, name="Case 2")

# Print the DataFrame
print(case2.df)
```



### 3. Exporting Data

Export the data to different formats:

```python
# Export as CSV
case1.export(filename="case1.csv", format="csv")

# Export as HTML with caption
html_content = case1.export(format="html", caption="Case 1 Data")
print(html_content)

# Export as Excel
case1.export(filename="case1.xlsx", format="xlsx")
```



### 4. Combining Multiple Cases

```python
# Create additional cases
case3 = sced(values=[5, 7, 6, 8, 10], phase=["A", "A", "B", "B", "B"], case="Case 3")

# Combine cases into a single long DataFrame
combined_df = sced.as_long_dataframe([case1, case3])

# Print combined DataFrame
print(combined_df)
```

**Output:**
```
   values  mt phase    case
0      10   1     A  Case 1
1      15   2     A  Case 1
2      12   3     A  Case 1
...
8       5   1     A  Case 3
9       7   2     A  Case 3
10      6   3     B  Case 3
11      8   4     B  Case 3
12     10   5     B  Case 3
```



### 5. Customizing the Output

To round values or include specific columns during export:

```python
# Export with rounded decimals and specific columns
csv_data = case1.export(format="csv", round_decimals=1, columns=["values", "phase"])
print(csv_data)
```


## Notes

- If no phase design is provided, the class will automatically infer the design based on input values or default to a single "A" phase.
- Ensure column names in the input DataFrame match the default variable labels (`dvar`, `pvar`, `mvar`) or specify custom labels during initialization.