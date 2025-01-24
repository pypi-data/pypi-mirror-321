# Topsis-Rohit-102203804

A Python package implementing the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) method for multi-criteria decision making.

## Installation

```bash
pip install Topsis-Rohit-102203804
```

## Usage

### Command Line Interface
```bash
topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

Example:
```bash
topsis data.csv "1,1,1,1,1" "+,+,-,+,-" result.csv
```

### As a Python Package
```python
from topsis_rohit_102203804.topsis import topsis

topsis("input.csv", [1,1,1,1,1], ['+','+','-','+','-'], "output.csv")
```

## Input Format
- Input file must be a CSV file with at least 3 columns
- First column is the object/alternative name
- From 2nd column onwards, there should be numeric values only

## Output
- Creates a CSV file with two additional columns: Topsis Score and Rank

## License
MIT License