
# select_case Function

The `select_case` function is an independent utility in the SCEPY package. It allows users to filter specific cases from a single-case experimental data frame (`scdf`). This function is particularly useful when analyzing subsets of multi-case data.



## Function Overview

```python
select_case(scdf, *cases)
```

### **Description**
Filters and returns the rows in the data frame corresponding to the specified case names.

### **Parameters**

| Parameter | Type        | Description                                                             |
|-----------|-------------|-------------------------------------------------------------------------|
| `scdf`    | `DataFrame` | The data frame containing single-case data.                            |
| `*cases`  | `str`       | One or more case names to select from the data frame.                  |

### **Returns**

- `DataFrame`: A filtered data frame containing only the rows for the specified cases.

### **Raises**
- `ValueError`: If no case names are provided.



## Example Usage

### **Filter Single Case**

Suppose you have a data frame with multiple cases:

| values | mt | phase | case  |
|--|-|-|-|
| 10     | 1  | A     | Case1 |
| 15     | 2  | A     | Case1 |
| 20     | 3  | B     | Case2 |
| 25     | 4  | B     | Case2 |

You can filter a specific case as follows:

```python
from scepy import sced, select_case

# Example data
data = sced(data={"values": [10, 15, 20, 25], 
                  "mt": [1, 2, 3, 4], 
                  "phase": ["A", "A", "B", "B"], 
                  "case": ["Case1", "Case1", "Case2", "Case2"]}).df

# Select "Case1"
filtered_data = select_case(data, "Case1")
print(filtered_data)
```

**Output:**
```
   values  mt phase   case
0      10   1     A  Case1
1      15   2     A  Case1
```



### **Filter Multiple Cases**

You can also filter multiple cases:

```python
filtered_data = select_case(data, "Case1", "Case2")
print(filtered_data)
```

**Output:**
```
   values  mt phase   case
0      10   1     A  Case1
1      15   2     A  Case1
2      20   3     B  Case2
3      25   4     B  Case2
```