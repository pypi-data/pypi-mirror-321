# TOPSIS Package

A Python package for ranking alternatives using the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) method.

## Installation

Install the package via pip:

```bash
pip install TopsisPackage_102216017
```

## Usage

### Command-Line Interface (CLI)

Run the TOPSIS method from the command line:

```bash
topsis <input_file.csv> [weights] [impacts]
```

#### Parameters:
- **`<input_file.csv>`**: Path to the CSV file containing the data.
- **`[weights]`**: List of weights for criteria, e.g., `[0.4,0.3,0.3]`.
- **`[impacts]`**: List of impacts, where `+` is for beneficial criteria and `-` is for non-beneficial criteria.

#### Example:
```bash
topsis data.csv [0.5,0.3,0.2] [+, -, +]
```

### Using in Python Code

You can use the package programmatically in Python:

```python
from TopsisPackage_102216017 import Topsis

# Input data: rows = alternatives, columns = criteria
data = [
    [250, 16, 12],
    [200, 16, 8],
    [300, 32, 16]
]
weights = [0.4, 0.3, 0.3]  # Criteria weights
impacts = ['+', '-', '+']   # '+' = beneficial, '-' = non-beneficial

# Create a Topsis object and calculate scores and ranks
topsis = Topsis(data, weights, impacts)
scores, ranks = topsis.rank()

print("Scores:", scores)  # Performance scores
print("Ranks:", ranks)    # Rankings
```

## Input File Format

The input CSV file should have the following structure:

| Alternative | Criterion1 | Criterion2 | Criterion3 |
|-------------|------------|------------|------------|
| A1          | 250        | 16         | 12         |
| A2          | 200        | 16         | 8          |
| A3          | 300        | 32         | 16         |

### Notes:
- **First column**: Names of alternatives (e.g., A1, A2).
- **Remaining columns**: Numerical values for each criterion.

## License

This project is licensed under the MIT License.
```