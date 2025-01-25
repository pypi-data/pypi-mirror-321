# TOPSIS Package

## Overview
This project implements a Python package for performing the **Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)** method. TOPSIS is a multi-criteria decision-making (MCDM) approach used to rank and select among various alternatives based on their distances from an ideal and a negative-ideal solution.

---

## Features
- Accepts CSV input files with multi-criteria data.
- Supports user-defined weights and impacts for each criterion.
- Outputs a ranked list based on the TOPSIS evaluation.
- Error handling for invalid input files, weights, and impacts.

---

## Installation
```bash
pip install 102203551-topsis
```

---

## Usage
Run the package from the command line:

### Syntax
```bash
python -m topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

### Example
```bash
python -m topsis 102203551-data.csv "1,1,1,2,3" "+,+,-,+,+" 102203551-result.csv
```

### Parameters

- `<InputDataFile>`: Path to the CSV file containing the decision matrix.
- `<Weights>`: Comma-separated weights for each criterion (e.g., `1,2,1,1`).
- `<Impacts>`: Comma-separated impacts for each criterion (`+` for benefit, `-` for cost).
- `<ResultFileName>`: Name of the output file where results will be saved.
