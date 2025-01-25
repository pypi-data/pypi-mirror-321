```markdown
# SingleCaseData Class Documentation

The `SingleCaseData` class from the `scepy` package is designed to handle single-case experimental data, providing a flexible structure for creating, managing, and analyzing datasets. It allows users to define variables, phases, measurement times, and other configurations tailored to single-case research designs.

## Functionality

The `SingleCaseData` class is responsible for:
- Organizing and structuring single-case data into a pandas DataFrame.
- Automatically creating and managing experimental phases (e.g., "A" and "B").
- Supporting various ways to input data, such as raw lists, pandas DataFrames, or predefined experimental designs.
- Providing export functionality for datasets in different formats (e.g., CSV, HTML, Excel).

## Key Parameters

- `values`: A list of dependent variable values (e.g., measurements or observations).
- `phase`: A list indicating the experimental phase for each value (e.g., "A", "B").
- `case`: Identifier for the case or subject.
- `B_start`: Specifies the starting index for phase "B".
- `mt`: Measurement times corresponding to each value.
- `phase_design`: A dictionary defining the number of measurements in each phase (e.g., `{"A": 3, "B": 5}`).
- `phase_starts`: A dictionary specifying the starting index for each phase (e.g., `{"A": 1, "B": 4}`).
- `data`: A pandas DataFrame containing the dataset.

## Examples of Usage

### Create a SingleCaseData Object from Values and Phases
```python
from scepy import SingleCaseData

values = [10, 12, 15, 20, 25, 30]
phases = ["A", "A", "A", "B", "B", "B"]

scd = SingleCaseData(values=values, phase=phases)
print(scd.df)
```

### Create SingleCaseData Using a DataFrame
```python
import pandas as pd
from scepy import SingleCaseData

data = pd.DataFrame({
    "values": [10, 15, 20, 25, 30, 35],
    "phase": ["A", "A", "B", "B", "B", "B"]
})

scd = SingleCaseData(data=data)
print(scd.df)
```

### Create SingleCaseData Using `B_start`
```python
from scepy import SingleCaseData

values = [5, 10, 15, 20, 25]
B_start = 3

scd = SingleCaseData(values=values, B_start=B_start)
print(scd.df)
```

### Create SingleCaseData with Phase Design
```python
from scepy import SingleCaseData

values = [5, 10, 15, 20, 25]
phase_design = {"A": 2, "B": 3}

scd = SingleCaseData(values=values, phase_design=phase_design)
print(scd.df)
```

### Create SingleCaseData with Measurement Times
```python
from scepy import SingleCaseData

values = [10, 15, 20, 25, 30]
phases = ["A", "A", "B", "B", "B"]
mt = [1, 2, 3, 4, 5]

scd = SingleCaseData(values=values, phase=phases, mt=mt)
print(scd.df)
```

### Export the Dataset
You can export the dataset to different formats like HTML, CSV, or Excel:
```python
# Export as HTML
html_content = scd.export(format="html")

# Export as CSV
scd.export(filename="dataset.csv", format="csv")

# Export as Excel
scd.export(filename="dataset.xlsx", format="xlsx")
```

### Combine Multiple Cases into a Long DataFrame
```python
from scepy import SingleCaseData

case1 = SingleCaseData(values=[10, 20, 30], phase=["A", "A", "B"], name="Case1")
case2 = SingleCaseData(values=[15, 25, 35], phase=["A", "B", "B"], name="Case2")

long_df = SingleCaseData.as_long_dataframe([case1, case2])
print(long_df)
```

## Notes
- The `SingleCaseData` class is highly flexible and can handle missing parameters or infer defaults when necessary.
- Use `phase_design` or `B_start` for automatically splitting phases without manually specifying them.