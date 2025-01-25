# TOPSIS Package

The TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) package is a Python library for multi-criteria decision-making. It helps users rank alternatives based on their proximity to the ideal solution and their distance from the worst-case solution.

## Installation

You can install the package using pip:

```bash
pip install topsis
```

## Usage

The package provides a simple interface for applying the TOPSIS method. Follow these steps:

### Import the Package

```python
from topsis import topsis
```

### Prepare Input Data

You need the following inputs:
1. A decision matrix (a 2D list or NumPy array) where each row represents an alternative and each column represents a criterion.
2. A list of weights for each criterion.
3. A list of impacts for each criterion (either `'+'` for positive impact or `'-'` for negative impact).

#### Example Input:

```python
decision_matrix = [
    [250, 16, 12, 5],
    [200, 20, 15, 6],
    [300, 18, 10, 8],
    [275, 25, 16, 7]
]
weights = [0.25, 0.25, 0.25, 0.25]
impacts = ['+', '+', '-', '+']
```

### Run the TOPSIS Method

Call the `topsis` function with the prepared inputs:

```python
rankings = topsis(decision_matrix, weights, impacts)
```

The `rankings` variable will contain the final rankings of the alternatives.

### Full Example

```python
from topsis import topsis

decision_matrix = [
    [250, 16, 12, 5],
    [200, 20, 15, 6],
    [300, 18, 10, 8],
    [275, 25, 16, 7]
]
weights = [0.25, 0.25, 0.25, 0.25]
impacts = ['+', '+', '-', '+']

rankings = topsis(decision_matrix, weights, impacts)
print("Rankings:", rankings)
```

## Output
The output will be a list containing the rankings of the alternatives, with `1` representing the best alternative.

#### Example Output:

```
Rankings: [2, 3, 1, 4]
```

## Features
- Simple interface for applying the TOPSIS method.
- Supports any number of alternatives and criteria.
- Customizable weights and impacts.

## Testing

Run the unit tests to verify the functionality:

```bash
python -m unittest discover tests
```

## License

This package is licensed under the MIT License. See the LICENSE file for details.

