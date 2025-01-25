# Reading Data Function

The `readdata` function is designed to streamline the process of importing single-case experimental design data from CSV or Excel files and converting it into an instance of the `sced` class. This functionality makes it easy to analyze and manage SCED data directly from external files.



## Function Overview

```python
readdata(file, cvar="case", pvar="phase", dvar="values", mvar="mt", 
         sort_cases=False, phase_names=None, sep=",", dec=".")
```

### Parameters

| Parameter     | Type   | Description                                                                                  |
|---------------|--------|----------------------------------------------------------------------------------------------|
| `file`        | `str`  | Path to the file (CSV or Excel) containing the data.                                         |
| `cvar`        | `str`  | Column name for the case variable. Default is `"case"`.                                      |
| `pvar`        | `str`  | Column name for the phase variable. Default is `"phase"`.                                    |
| `dvar`        | `str`  | Column name for the dependent variable. Default is `"values"`.                               |
| `mvar`        | `str`  | Column name for the measurement time variable. If not present in the file, it is generated.  |
| `sort_cases`  | `bool` | Whether to sort the data by cases. Default is `False`.                                       |
| `phase_names` | `list` | Optional list to rename phases, e.g., `["A", "B"]`.                                          |
| `sep`         | `str`  | Column separator for CSV files. Default is `","`.                                            |
| `dec`         | `str`  | Decimal point character. Default is `"."`.                                                   |

### Returns

- An instance of the `sced` class with the loaded data.

## Function Details

### File Type Support

The `readdata` function supports:
- **CSV files**: Read using `pd.read_csv`.
- **Excel files**: Read using `pd.read_excel`.
- If an unsupported file type is provided, the function raises a `ValueError`.

### Data Preparation

1. **Required Columns**:
   - Ensures that the file includes the specified `cvar`, `pvar`, `dvar`, and optionally `mvar` columns.
   - If `mvar` is missing, a default sequence starting from 1 is generated.

2. **Phase Mapping**:
   - If `phase_names` is provided, the unique phase values are mapped to the specified names.

3. **Sorting**:
   - If `sort_cases=True`, the data is sorted by `case` and `mt`.

4. **Conversion**:
   - The prepared data is converted into an `sced` instance using the `data` parameter.



## Example Usage

### 1. Import Data from a CSV File

Suppose you have a CSV file named `data.csv` with the following structure:

| case  | phase | values | mt |
|-|-|--|-|
| Case1 | A     | 10     | 1  |
| Case1 | A     | 15     | 2  |
| Case1 | B     | 20     | 3  |

You can load it as follows:

```python
from scepy import readdata

case_data = readdata("data.csv")

# Access the resulting DataFrame
print(case_data.df)
```

**Output:**

```
   values  mt phase   case
0      10   1     A  Case1
1      15   2     A  Case1
2      20   3     B  Case1
```



### **2. Import Data with Missing Columns**

If the `mt` column is missing from the file, it will be automatically generated:

```python
case_data = readdata("data_without_mt.csv")
print(case_data.df)
```

**Output:**
```
   values  mt phase   case
0      10   1     A  Case1
1      15   2     A  Case1
2      20   3     B  Case1
```



### **3. Assign Custom Phase Names**

```python
# Map phase values to custom names
case_data = readdata("data.csv", phase_names=["Baseline", "Intervention"])
print(case_data.df)
```

**Output:**
```
   values  mt         phase   case
0      10   1     Baseline  Case1
1      15   2     Baseline  Case1
2      20   3  Intervention  Case1
```



### **4. Sort Cases**

If your data includes multiple cases and you want to sort them:

```python
case_data = readdata("multi_case_data.csv", sort_cases=True)
print(case_data.df)
```



## Error Handling

1. **Unsupported File Type**:
   - If the file is not CSV or Excel, the function raises:
     ```
     ValueError: Unsupported file format. Please provide a CSV or Excel file.
     ```

2. **Missing Columns**:
   - If essential columns like `phase` or `values` are missing:
     ```
     ValueError: CSV/Excel file must contain '<column_name>' column.
     ```