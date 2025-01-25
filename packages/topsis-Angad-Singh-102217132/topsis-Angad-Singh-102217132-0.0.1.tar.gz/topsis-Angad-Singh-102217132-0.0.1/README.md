# TOPSIS Analysis Package

A Python package for performing TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) analysis on numerical datasets. This package provides both a command-line interface and a importable module for performing TOPSIS analysis on datasets containing numerical data (int32, int64, float32, float64).

## Overview

TOPSIS is a multi-criteria decision analysis method that helps identify the best alternative from a set of options based on multiple criteria. The package normalizes the input data, applies weights to different criteria, and considers whether each criterion should be maximized or minimized.

## Installation

```bash
pip install topsis-102217132
```

## Usage

### As a Module

```python
from topsis_analysis import run

# Perform TOPSIS analysis
result_df = run(
    input_df,           # pandas DataFrame with numerical values
    weights,            # List of weights for each criterion
    impacts,            # List of impacts ('+' or '-') for each criterion
)
```

### Command Line Interface

```bash
python -m topsis_analysis <source_csv> <weights> <impacts> <output_csv>
```

### Parameters

#### For Both Module and CLI:

1. Input Data:
   - Must contain only numerical values (int32, int64, float32, float64)
   - First column will be used as index
   - No missing values allowed

2. Weights:
   - Must sum to 1
   - Number of weights must match number of columns (excluding index)
   - Module: List of float values
   - CLI: Comma-separated values (e.g., "0.25,0.25,0.25,0.25")

3. Impacts:
   - Use '+' for criteria to be maximized
   - Use '-' for criteria to be minimized
   - Number of impacts must match number of columns (excluding index)
   - Module: List of strings
   - CLI: Comma-separated signs (e.g., "-,+,+,+")

#### CLI Only:

4. `output_csv`: Path where the result CSV will be stored

### Example Usage

#### As a Module

```python
import pandas as pd
from topsis_analysis import run

# Read input data
df = pd.read_csv('data.csv')

# Define weights and impacts
weights = [0.25, 0.25, 0.25, 0.25]
impacts = ['-', '+', '+', '+']

# Run TOPSIS analysis
result = run(df, weights, impacts)

# Save results if needed
result.to_csv('output.csv', index=False)
```

#### Command Line

```bash
python -m topsis-102217132 data.csv 0.25,0.25,0.25,0.25 -,+,+,+ output.csv
```

### Input CSV Format

```csv
Model,Price,Storage,Battery,Performance
1,799,256,12,85
2,999,512,10,92
3,699,128,15,78
```

- Weights not summing to 1
### Output Format

```csv
Model,Price,Storage,Battery,Performance,TOPSIS Score,Rank
1,799,256,12,85,0.534,2
2,999,512,10,92,0.687,1
3,699,128,15,78,0.423,3
```

## Error Handling

The package provides comprehensive error handling for:
- Invalid number of weights or impacts
- Invalid data types
- Missing values in the dataset
- Invalid file paths (CLI only)
- Non-numeric data in columns
- Invalid impact symbols

## Dependencies

- Python 3.7+
- pandas
- numpy

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.