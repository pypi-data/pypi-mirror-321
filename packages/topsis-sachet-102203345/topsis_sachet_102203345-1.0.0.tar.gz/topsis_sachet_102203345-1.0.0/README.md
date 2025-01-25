# TOPSIS Implementation in Python

---

## Overview
This Python script provides an implementation of the **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** method, a widely used technique for multi-criteria decision-making. It calculates performance scores and ranks for a dataset based on specified weights and impacts.

---

## How to Use

Execute the script using the following command:

```bash
python topsis.py <inputFileName> <weights> <impacts> <resultFileName>
```

- `<inputFileName>`: Path to the CSV file containing the dataset.
- `<weights>`: Comma-separated list of weights for the criteria (e.g., `1,2,3`).
- `<impacts>`: Comma-separated list of impacts for the criteria (`+` for benefit, `-` for cost).
- `<resultFileName>`: Name of the output file where the results will be saved.

---

## Input File Guidelines
1. The input file must be a `.csv` format with a minimum of **3 columns**.
2. The first column can contain non-numeric values (e.g., identifiers).
3. All columns from the second onward must contain **numeric values**.

---

## Key Features
- **Validation**:
  - Ensures the correct number of command-line arguments.
  - Validates weights, impacts, and the consistency of column counts.
  - Handles missing or invalid input files.
- **Error Handling**:
  - Provides clear error messages for issues such as missing files, non-numeric data, or mismatched parameters.
- **Output Generation**:
  - Adds two columns to the dataset: `Topsis Score` and `Rank`.
  - Saves the processed results to the specified output file.

---

## Prerequisites
- Python 3.x
- Required libraries: `pandas`, `math`, `sys`

Install dependencies using the command:
```bash
pip install pandas
```

---

## License
This project is open-source and available under the MIT License.
