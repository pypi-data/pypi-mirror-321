# TOPSIS Package

This is a Python package implementing the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) method.

## Installation

```pip install topsis-Urvi-102203720```

## Usage

```python
from topsis_Urvi_102203720 import topsis

# Example usage
result = topsis(
    '102203720-data.csv',
    '0.1,0.2,0.3,0.2,0.2',
    '+,+,-,+,+',
    '102203720-result.csv'
)