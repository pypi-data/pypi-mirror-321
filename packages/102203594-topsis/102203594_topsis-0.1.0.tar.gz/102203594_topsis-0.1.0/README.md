# TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)

## Overview
TOPSIS - This is a method which we can use to make decisions if we have multiple parameters from which we have to decide which model to choose by giving weights(preference) to those parameters and maximising or minimising them.

## Features
- Supports CSV input files.
- Handles numeric validation for criteria columns.
- Accepts weights and impacts for criteria.
- Detailed error messages for invalid inputs.
- Outputs the TOPSIS score and rank for each alternative.

---

## Installation
```bash
pip install 102203594_topsis
```

---

## Usage
### Input Requirements
1. **Input File**: A CSV file containing the decision matrix.
   - The first column should contain the names of the alternatives.
   - Remaining columns should contain numeric values for the criteria.

2. **Weights**: A list of numeric values representing the weight of each criterion.
   - Must match the number of criteria columns in the dataset.

3. **Impacts**: A list of strings (`'up'` or `'down'`) indicating whether higher or lower values are better for each criterion.
   - Must match the number of criteria columns in the dataset.

### Example Input File
**File: `data.csv`**
```csv
Alternative,Criterion 1,Criterion 2,Criterion 3
Model-1,250,16,12
Model-2,200,16,8
Model-3,300,32,16
Model-4,275,32,8
Model-5,225,16,16
```

### Example Code
```python
from topsis import topsis

# Define weights and impacts
weights = [0.25, 0.25, 0.25]
impacts = ['up', 'up', 'down']

# Perform TOPSIS
try:
    result = topsis("data.csv", weights, impacts)
    print(result)
except Exception as e:
    print(f"Error: {e}")
```

### Output
The output is a DataFrame containing the original data with two additional columns:
- **Topsis Score**: The relative closeness to the ideal solution.
- **Rank**: The rank of each alternative based on the TOPSIS score.

#### Example Output:
```csv
  Alternative  Criterion 1  Criterion 2  Criterion 3  Topsis Score  Rank
0          Model-1          250          16          12      0.534522     3
1          Model-2          200          16           8      0.308607     5
2          Model-3          300          32          16      0.780869     1
3          Model-4          275          32           8      0.612372     2
4          Model-5          225          16          16      0.199736     4
```

---

## Error Handling
The package includes robust error handling for:
1. **File Format**: Ensures the input file is a `.csv` file.
2. **Missing File**: Handles missing or incorrect file paths.
3. **Empty File**: Raises an error if the input file is empty.
4. **Column Validation**:
   - Ensures at least one column for alternatives and one for criteria.
   - Checks that all criteria columns contain numeric values.
5. **Weights and Impacts**:
   - Ensures weights and impacts match the number of criteria.
   - Validates that impacts are either `'up'` or `'down'`.

---

## Authors
- **Your Name** - [Your GitHub Profile](https://github.com/ShauryaJ123)

