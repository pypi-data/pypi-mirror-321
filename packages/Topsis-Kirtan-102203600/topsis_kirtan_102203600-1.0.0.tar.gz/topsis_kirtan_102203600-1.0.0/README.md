# Project Description

# TOPSIS Implementation

This python package is submitted by Kirtan Dwivedi; Roll No.- 102203600

## Overview

TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) is a multi-criteria decision-making (MCDM) method. This Python package implements the TOPSIS method, allowing you to rank alternatives based on multiple criteria.

This implementation is specifically designed to work with a CSV input file and provides results with TOPSIS scores and ranks.

## Features

- Handles multi-criteria decision-making problems
- Accepts CSV input files
- Outputs a CSV file with TOPSIS scores and ranks
- Validates input data and handles common errors
- Command-line interface for ease of use

## Guide Video and Web Service for Topsis.

For a detailed guide, you can watch this [Topsis package in python by Kirtan Dwivedi](#) and check this [Topsis-Kirtan-102203600](#) for direct use.

If you have any questions, suggestions, or issues, feel free to comment.

## OR

## Installation

You can install this package directly from PyPI using pip:

```bash
pip install Topsis-Kirtan-102203600
```

## Usage

### Command-Line Interface

After installing the package, you can use it from the command line. The basic usage is:

```bash
python topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

### Parameters

- **InputDataFile**: The path to the input XLSX file containing the data.
- **Weights**: A string of comma-separated numerical weights (e.g., `"1,1,1,2"`).
- **Impacts**: A string of comma-separated `+` or `-` signs indicating whether each criterion is beneficial (`+`) or non-beneficial (`-`) (e.g., `"+,+,-,+"`).
- **ResultFileName**: The path to the output CSV file where results will be saved.

### Example

Suppose you have an input file named `102203600_data.xlsx` with the following content:

```csv
| Alternative | Criterion1 | Criterion2 | Criterion3 | Criterion4 |
|-------------|------------|------------|------------|------------|
| M1          | 250        | 16         | 12         | 5          |
| M2          | 200        | 6          | 8          | 3          |
| M3          | 300        | 16         | 8          | 4          |
| M4          | 275        | 10         | 10         | 4          |
```

You can run the following command:

```bash
topsis 102203600_data.xlsx "1,1,1,2" "+,+,-,+"  102203600_result.csv
```

This will generate a file `102203600_result.csv` containing the input data along with two additional columns for the TOPSIS score and the rank:

```csv
| Alternative | Criterion1 | Criterion2 | Criterion3 | Criterion4 | TOPSIS Score | Rank |
|-------------|------------|------------|------------|------------|--------------|------|
| M1          | 250        | 16         | 12         | 5          | 0.556        | 2    |
| M2          | 200        | 6          | 8          | 3          | 0.222        | 4    |
| M3          | 300        | 16         | 8          | 4          | 0.778        | 1    |
| M4          | 275        | 10         | 10         | 4          | 0.444        | 3    |

```

## Error Handling

The program includes several checks to handle common errors:

- Correct number of parameters (inputFileName, Weights, Impacts, resultFileName).
- Show the appropriate message for wrong inputs.
- Handling of “File not Found” exception
- Input file must contain three or more columns.
- From 2nd to last columns must contain numeric values only (Handling of non-numeric values)
  -Number of weights, number of impacts and number of columns (from 2nd to last columns) must
  be same.
- Impacts must be either +ve or -ve.
- Impacts and weights must be separated by ‘,’ (comma).

### Examples

#### Example 1: Basic Usage

```bash
python topsis data.xlsx "1,1,1,1" "+,+,+,+" result.csv
```

#### Example 2: Different Weights and Impacts

```bash
python topsis data.xlsx "0.5,1,1.5,2" "+,-,+,-" result.csv
```

#### Example 3: Handling Errors

If the number of weights or impacts does not match the number of criteria:

```bash
python topsis data.xlsx "1,1,1" "+,+" result.csv
```

This will result in an error message indicating the mismatch.

## Testing

To ensure everything works correctly, you can run some tests. If you haven't already, you can clone the repository and run the tests locally.

```bash
# Clone the repository
git clone https://github.com/KirtanDwivedi/Topsis-Kirtan-102203600

# Navigate to the project directory
cd Topsis_Kirtan_102203600

# Install the required dependencies
pip install -r requirements.txt

# Run the tests (assuming you've created test scripts)
python -m unittest discover tests
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Inspired by the original TOPSIS method developed by C.L. Hwang and K. Yoon.
