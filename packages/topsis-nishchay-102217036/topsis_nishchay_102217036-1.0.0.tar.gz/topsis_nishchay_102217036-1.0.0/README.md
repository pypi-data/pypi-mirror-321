# TOPSIS Implementation in Python

---

## Overview
This Python script implements the **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** method for multi-criteria decision-making. It calculates the performance score and rank for given data based on user-defined weights and impacts.

---

## Usage

Run the script with the following command:

```bash
python topsis.py <inputFileName> <weights> <impacts> <resultFileName>
```

- `<inputFileName>`: Path to the CSV file containing the dataset.
- `<weights>`: Comma-separated weights for the criteria (e.g., `1,2,3`).
- `<impacts>`: Comma-separated impacts for the criteria (`+` for benefit, `-` for cost).
- `<resultFileName>`: Name of the output file where results will be saved.

---

## Input File Requirements
1. Must be a `.csv` file with at least **3 columns**.
2. The first column can contain non-numeric values (e.g., IDs).
3. Columns from the 2nd to the last must contain **numeric values only**.

---

## Features
- **Validation**:
  - Ensures correct number of inputs.
  - Validates weights, impacts, and column counts.
  - Handles missing or invalid files.
- **Error Handling**:
  - Displays user-friendly messages for issues like file not found, non-numeric data, or mismatched input parameters.
- **Output**:
  - Adds two new columns: `Topsis Score` and `Rank`.
  - Saves the results in the specified output file.

---

## Dependencies
- Python 3.x
- Required libraries: `pandas`, `math`, `sys`

Install dependencies using:
```bash
pip install pandas
```

---

## License
This project is open-source and free to use under the MIT License.
