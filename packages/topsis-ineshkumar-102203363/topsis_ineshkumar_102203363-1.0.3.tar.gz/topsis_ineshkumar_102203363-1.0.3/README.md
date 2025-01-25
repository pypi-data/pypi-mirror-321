# topsis_ineshkumar_102203363

`topsis_ineshkumar_102203363` is a Python package that implements the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) method for multi-criteria decision analysis.

## Installation

You can install the package using pip:

```bash
pip install topsis_ineshkumar_102203363
```

## Usage

### Input File Format

The input CSV file should have the following structure:

- The first column should contain the names of the models.
- The subsequent columns should contain the criteria values for each alternative.
- The first row should contain the headers for each column.

Example:

| model | Criteria 1 | Criteria 2 | Criteria 3 |
|-------------|------------|------------|------------|
| m1        | 250        | 16         | 12         |
| m2        | 200        | 14         | 8          |
| m3        | 300        | 18         | 15         |

### Command-line Usage

After installation, you can use the `topsis` command in the terminal:

```bash
topsis <input_file> <weights> <impacts> <output_file>
```

- `<input_file>`: Path to the input CSV file.
- `<weights>`: Comma-separated string of weights for the criteria.
- `<impacts>`: Comma-separated string of '+' or '-' indicating the desirability of the criteria.
- `<output_file>`: Path to the output CSV file to save the results.

## Example

```bash
topsis data.csv "0.5,0.3,0.2" "+,-,+" results.csv
```

This command will process the `data.csv` file using the specified weights and impacts and output the results to `results.csv`.

## NOTE

- Ensure that the input file has at least three columns: one for alternatives and at least two for criteria.
- All criteria columns should contain numeric values.
- The number of weights and impacts must match the number of criteria.
- Impacts should only be '+' or '-'.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
