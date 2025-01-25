# TOPSIS Package

A Python package for performing TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) analysis.

## Installation
You can install this package using pip:

```bash
pip install package-topsis

from package_topsis import topsis

data = [
    [250, 16, 12, 5],
    [200, 16, 8, 3],
    [300, 32, 16, 4],
    [275, 32, 8, 4],
    [225, 16, 16, 2],
]
weights = [0.25, 0.25, 0.25, 0.25]
impacts = ['+', '+', '-', '+']

rankings = topsis(data, weights, impacts)
print(rankings)  # Output: [3, 1, 2, 5, 4]
