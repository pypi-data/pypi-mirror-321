# Topsis_Tanvi_102213024

`Topsis_Tanvi_102213024`is a Python package for implementing the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS). It is a popular multi-criteria decision-making method used to rank alternatives based on their relative closeness to the ideal solution.

## Installation

You can install the package using pip:

```bash
pip install Topsis_Tanvi_102213024
```

## Usage

### Input File Format

The input CSV file must follow this structure:

- The first column should contain the names of the alternatives (e.g., products, models, or options).
- Subsequent columns should contain the numerical values of the criteria for each alternative.
- The first row should provide headers for all columns.

### Example

Suppose you have an input CSV file named `data.csv` with the following content:

| Model | Price | Battery Life | Performance | Portability |
| ----- | ----- | ------------ | ----------- | ----------- |
| m1    | 300   | 10           | 8           | 6           |
| m2    | 250   | 8            | 7           | 9           |
| m3    | 400   | 9            | 9           | 5           |

You want to apply the TOPSIS method with the following parameters:

- Weights for the criteria: `Price` (0.5), `Battery Life` (0.3), `Performance` (0.2)
- Impacts for the criteria: `Price` (-), `Battery Life` (+), `Performance` (+)

The command would be:

````bash
topsis data.csv "0.5,0.3,0.2" "-,+,+" results.csv


### Command-line Usage

After installation, you can use the `topsis` command in the terminal:

```bash
topsis <input_file> <weights> <impacts> <output_file>
````

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

- Ensure the input file contains at least three columns: one for alternatives and at least two for criteria.
- All criteria values should be numerical.
- The number of weights and impacts should match the number of criteria columns.
- Impacts must only include + (beneficial) or - (non-beneficial).

## License

This project is licensed under the MIT License. See the LICENSE file for details.
