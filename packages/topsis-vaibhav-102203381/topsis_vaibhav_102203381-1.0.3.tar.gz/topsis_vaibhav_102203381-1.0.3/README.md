# TOPSIS Method Implementation - Vaibhav Garg (102203381)

This Python package implements the **Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)** method for multi-criteria decision analysis.

## Installation

You can install the package using pip:

```bash
pip install topsis_vaibhav_102203381
```

## Usage

### Input File Format

The input CSV file should have the following structure:

- The first column should contain the names of the models.
- The subsequent columns should contain the criteria values for each alternative.
- The first row should contain the headers for each column.

Example:

| Model | Criteria 1 | Criteria 2 | Criteria 3 | Criteria 4 | Criteria 5 | Criteria 6 |
|-------|------------|------------|------------|------------|------------|------------|
| m1    | 250        | 16         | 12         | 30         | 80         | 7          |
| m2    | 200        | 14         | 8          | 35         | 70         | 5          |
| m3    | 300        | 18         | 15         | 25         | 90         | 6          |

### Weights:

Comma-separated values that indicate the weight of each criterion.

Example:
```
0.2, 0.1, 0.15, 0.1, 0.25, 0.2
```

### Impacts:

Comma-separated string of `+` or `-` that indicate the direction of optimization for each criterion.

Example:
```
+, -, +, -, +, +
```

Where:
- `+` indicates the criterion is to be **maximized**.
- `-` indicates the criterion is to be **minimized**.

### Command-line Usage

After installation, you can use the `topsis` command in the terminal to process the data:

```bash
topsis <input_file> <weights> <impacts> <output_file>
```

- `<input_file>`: Path to the input CSV file.
- `<weights>`: Comma-separated string of weights for the criteria.
- `<impacts>`: Comma-separated string of '+' or '-' indicating the desirability of the criteria.
- `<output_file>`: Path to the output CSV file to save the results.

Example:

```bash
topsis data.csv "0.2,0.1,0.15,0.1,0.25,0.2" "+,-,+,-,+,+" result.csv
```

This command will process the `data.csv` file using the specified weights and impacts and output the results to `result.csv`.

### Example Explanation

#### Input Data (CSV):
| Model | Criteria 1 | Criteria 2 | Criteria 3 | Criteria 4 | Criteria 5 | Criteria 6 |
|-------|------------|------------|------------|------------|------------|------------|
| m1    | 250        | 16         | 12         | 30         | 80         | 7          |
| m2    | 200        | 14         | 8          | 35         | 70         | 5          |
| m3    | 300        | 18         | 15         | 25         | 90         | 6          |

#### Weights:
`0.2, 0.1, 0.15, 0.1, 0.25, 0.2`

#### Impacts:
`+, -, +, -, +, +`

- **Criteria 1** and **Criteria 3** are to be maximized (`+`).
- **Criteria 2** and **Criteria 4** are to be minimized (`-`).
- **Criteria 5** and **Criteria 6** are to be maximized (`+`).

#### Command to Execute:
```bash
topsis data.csv "0.2,0.1,0.15,0.1,0.25,0.2" "+,-,+,-,+,+" result.csv
```

#### Output Example:

| Model | Score | Rank |
|-------|-------|------|
| m1    | 0.78  | 2    |
| m2    | 0.65  | 3    |
| m3    | 0.89  | 1    |

### Notes

- Ensure that the input file has at least three columns: one for alternatives and at least two for criteria.
- All criteria columns should contain numeric values.
- The number of weights and impacts must match the number of criteria.
- Impacts should only be `+` or `-`.
  
## License

This project is licensed under the MIT License. See the LICENSE file for details.
