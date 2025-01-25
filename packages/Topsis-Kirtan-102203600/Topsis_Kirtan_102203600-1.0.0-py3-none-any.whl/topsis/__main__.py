import sys
import os
import pandas as pd
import numpy as np

def validate_inputs(args):
    if len(args) != 5:
        raise ValueError("Error: Incorrect number of parameters. Expected 4 parameters: inputFileName, Weights, Impacts, resultFileName.")

    input_file, weights, impacts, result_file = args[1], args[2], args[3], args[4]

    # Check if file exists
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"Error: File '{input_file}' not found.")

    # Convert and rename Excel file if necessary
    if input_file.endswith('.xlsx'):
        try:
            roll_number = os.path.splitext(os.path.basename(input_file))[0]
            csv_file = f"{roll_number}-data.csv"
            data = pd.read_excel(input_file)
            data.to_csv(csv_file, index=False)
            print(f"Converted '{input_file}' to '{csv_file}'")
            input_file = csv_file
        except Exception as e:
            raise ValueError(f"Error: Failed to convert Excel file. {e}")

    # Check weights and impacts format
    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    if len(set(impacts) - {'+', '-'}) > 0:
        raise ValueError("Error: Impacts must be either '+' or '-'.")

    return input_file, weights, impacts, result_file

def topsis(input_file, weights, impacts, result_file):
    # Read the input file with explicit encoding
    try:
        data = pd.read_csv(input_file, encoding='utf-8')
    except UnicodeDecodeError:
        data = pd.read_csv(input_file, encoding='latin1')  # Fallback for non-UTF-8 files

    # Validate input file
    if data.shape[1] < 3:
        raise ValueError("Error: Input file must contain three or more columns.")

    # Check for non-numeric values in criteria columns
    numeric_data = data.iloc[:, 1:]
    if not all([np.issubdtype(dtype, np.number) for dtype in numeric_data.dtypes]):
        raise ValueError("Error: From 2nd to last columns must contain numeric values only.")

    if len(weights) != numeric_data.shape[1] or len(impacts) != numeric_data.shape[1]:
        raise ValueError("Error: Number of weights, impacts, and criteria columns must be the same.")

    # Normalize the decision matrix
    norm_matrix = numeric_data / np.sqrt((numeric_data**2).sum())

    # Weighted normalized decision matrix
    weighted_matrix = norm_matrix * weights

    # Identify ideal best and ideal worst
    ideal_best = []
    ideal_worst = []
    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted_matrix.iloc[:, i].max())
            ideal_worst.append(weighted_matrix.iloc[:, i].min())
        else:
            ideal_best.append(weighted_matrix.iloc[:, i].min())
            ideal_worst.append(weighted_matrix.iloc[:, i].max())

    # Calculate the separation measures
    separation_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    separation_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Calculate TOPSIS score
    topsis_score = separation_worst / (separation_best + separation_worst)

    # Rank alternatives
    data['TOPSIS Score'] = topsis_score
    data['Rank'] = topsis_score.rank(ascending=False).astype(int)

    # Save the result to a CSV file
    data.to_csv(result_file, index=False)
    print(f"Results saved to '{result_file}'")

if __name__ == "__main__":
    try:
        input_file, weights, impacts, result_file = validate_inputs(sys.argv)
        topsis(input_file, weights, impacts, result_file)
    except Exception as e:
        print(e)
