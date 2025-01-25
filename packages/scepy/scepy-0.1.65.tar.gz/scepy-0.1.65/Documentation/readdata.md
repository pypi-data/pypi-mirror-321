Here are all possible ways to use the `readdata` function based on the provided code:

### **1. Reading a CSV File**
The `readdata` function can read data from a CSV file.

```python
from scepy import readdata

# Example CSV file structure:
# case,phase,values,mt
# Case1,A,10,1
# Case1,A,12,2
# Case1,B,15,3

file_path = "data.csv"
scd = readdata(file_path)
print(scd.df)
```

### **2. Reading an Excel File**
You can also use `readdata` to read data from an Excel file.

```python
from scepy import readdata

# Example Excel file structure:
# case | phase | values | mt
# Case1 | A    | 10     | 1
# Case1 | A    | 12     | 2
# Case1 | B    | 15     | 3

file_path = "data.xlsx"
scd = readdata(file_path)
print(scd.df)
```

### **3. Custom Column Names**
If your file uses different column names, you can specify them with `cvar`, `pvar`, `dvar`, and `mvar`.

```python
from scepy import readdata

# Example CSV file structure:
# subject,stage,measurements,time
file_path = "custom_data.csv"
scd = readdata(file_path, cvar="subject", pvar="stage", dvar="measurements", mvar="time")
print(scd.df)
```

### **4. Missing Case Column**
If the file does not include a case column, the function will automatically add a default case named `"Case1"`.

```python
from scepy import readdata

# Example CSV file structure without 'case' column:
# phase,values,mt
# A,10,1
# A,12,2
# B,15,3

file_path = "data_no_case.csv"
scd = readdata(file_path)
print(scd.df)
```

### **5. Assign Phase Names**
You can map existing phase values to new names using the `phase_names` parameter.

```python
from scepy import readdata

# Example CSV file structure:
# case,phase,values,mt
# Case1,X,10,1
# Case1,X,12,2
# Case1,Y,15,3

file_path = "data.csv"
scd = readdata(file_path, phase_names=["Phase A", "Phase B"])
print(scd.df)
```

### **6. Automatic Measurement Times**
If the file does not include a measurement time column, the function will generate one automatically.

```python
from scepy import readdata

# Example CSV file structure without 'mt' column:
# case,phase,values
# Case1,A,10
# Case1,A,12
# Case1,B,15

file_path = "data_no_mt.csv"
scd = readdata(file_path)
print(scd.df)
```

### **7. Sorting Cases**
If your file contains multiple cases and you want them sorted by case and measurement time, set `sort_cases=True`.

```python
from scepy import readdata

# Example CSV file structure:
# case,phase,values,mt
# Case2,A,20,1
# Case1,A,10,1
# Case2,B,25,2
# Case1,B,15,2

file_path = "data_multiple_cases.csv"
scd = readdata(file_path, sort_cases=True)
print(scd.df)
```

### **8. Using a Custom Separator**
You can specify a custom separator for CSV files using the `sep` parameter.

```python
from scepy import readdata

# Example CSV file with semicolon separator:
# case;phase;values;mt
# Case1;A;10;1
# Case1;A;12;2
# Case1;B;15;3

file_path = "data_semicolon.csv"
scd = readdata(file_path, sep=";")
print(scd.df)
```

### **9. Custom Decimal Separator**
If the file uses a custom decimal separator (e.g., `,` instead of `.`), you can specify it using the `dec` parameter.

```python
from scepy import readdata

# Example CSV file with comma decimal separator:
# case,phase,values,mt
# Case1,A,10,1
# Case1,A,12.5,2
# Case1,B,15.3,3

file_path = "data_comma_decimal.csv"
scd = readdata(file_path, dec=",")
print(scd.df)
```

### **10. Phase Data Validation**
If the file does not include valid phase data, the function will still generate a `SingleCaseData` object with an empty `phase_design`.

```python
from scepy import readdata

# Example CSV file with no valid phase data:
# case,values,mt
# Case1,10,1
# Case1,12,2
# Case1,15,3

file_path = "data_no_phase.csv"
scd = readdata(file_path)
print(scd.df)
```

### Notes
1. The function supports both CSV and Excel files.
2. It automatically checks for required columns and fills in missing data if necessary.
3. If the file format or structure is invalid, an error will be raised with a clear message.