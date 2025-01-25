# Topsis-Manya-102203284

This is a Python package to implement the **Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)** for multi-criteria decision-making problems. 

TOPSIS is a useful method for ranking and selecting alternatives when multiple criteria are involved, such as decision-making problems in business, engineering, and more.

## Features

- **Flexible Input**: Accepts any CSV file with numeric data.
- **Customizable Weights**: Allows users to specify weights for each criterion.
- **Impact Specification**: Supports both beneficial (`+`) and non-beneficial (`-`) criteria.
- **Accurate Ranking**: Calculates TOPSIS scores and ranks the alternatives.
- **Error Handling**: Ensures robust handling of invalid inputs and edge cases.

---

## Installation

You can install this package via pip:
pip install topsis-manya-102203284


## Usage

```python
from topsis_manya.topsis import topsis

# Example usage
topsis('input.csv', [1, 1, 1, 2, 1], ['+', '+', '-', '+', '-'], 'output.csv')

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
