# TOPSIS Package

This package implements the **Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)**, a multi-criteria decision analysis (MCDA) method used for ranking and selecting a set of alternatives based on their distance to an ideal solution.

## Features

- **TOPSIS Implementation:** Rank a set of alternatives based on multiple criteria.
- **Ideal and Negative Ideal Solution Calculation:** Automatically calculate the positive and negative ideal solutions.
- **Normalization:** Normalize the decision matrix to make the comparison meaningful.
- **Weighted Sum Model:** Support for weighted decision matrix for each criterion.
- **Distance Calculation:** Use Euclidean distance to calculate closeness to ideal solutions.

## Installation

You can install the package via pip or manually by cloning the repository.

```bash
pip install topsis
```

Alternatively, you can clone the repository and install the package manually:

```bash
git clone https://github.com/yourusername/topsis.git
cd topsis
python setup.py install
```

## Input Format

- **Decision Matrix**: A list of lists where each inner list represents an alternative, and each element within that list represents the value for a particular criterion.
- **Weights**: A list where each value represents the weight for a corresponding criterion. The weights should sum up to 1 or should be proportionally normalized.
- **Impacts**: A list where each value represents the impact for a corresponding criterion. Use `1` for beneficial criteria (higher values are better) and `-1` for non-beneficial criteria (lower values are better).

## Output Format

The output will be a ranking of the alternatives based on their closeness to the ideal solution, starting with the best.

## Requirements

- Python 3.x
- Pandas
- NumPy

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
