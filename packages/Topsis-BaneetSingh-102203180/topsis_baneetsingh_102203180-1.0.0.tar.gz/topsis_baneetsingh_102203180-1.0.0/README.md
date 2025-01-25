# Topsis-Baneet-102203180

A Python package for implementing the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method.

## Installation

```bash
pip install Topsis-Baneet-102203180
```

## Usage

You can use this package either through command line or as a Python module.

### Command Line Usage

```bash
python -m topsis_baneet_102203180 input.csv "1,1,1,2" "+,+,-,+" result.csv
```

### Python Module Usage

```python
from topsis_baneet_102203180 import topsis

# Process TOPSIS
result = topsis("input.csv", "1,1,1,2", "+,+,-,+", "result.csv")
```

## Input Format

1. Input file (CSV):
   - First column: Object/Variable names
   - Subsequent columns: Numeric values only

2. Weights: Comma-separated numeric values
   - Example: "1,1,1,2"

3. Impacts: Comma-separated '+' or '-' values
   - Example: "+,+,-,+"

## Output

The program will generate a CSV file with:
- All original columns
- Additional 'Topsis Score' column
- Additional 'Rank' column

## License

MIT License

## Author

Baneet Singh
