# -*- coding: utf-8 -*-
import math
import pandas as pd
import sys
import os

def topsis(arguments):
    # Ensure the correct number of parameters are provided
    if len(arguments) != 4:
        print("Error: Exactly four parameters are required: inputFileName, Weights, Impacts, resultFileName.")
        sys.exit(1)

    input_filepath, weight_values, impact_values, output_filepath = arguments

    # Verify the existence of the input file
    if not os.path.isfile(input_filepath):
        print(f"Error: The file '{input_filepath}' does not exist.")
        sys.exit(1)

    try:
        # Load the input CSV file
        data = pd.read_csv(input_filepath)
    except Exception as error:
        print(f"Error: Unable to read the input file. {str(error)}")
        sys.exit(1)

    # Validate that the dataset contains at least three columns
    if data.shape[1] < 3:
        print("Error: The dataset must have at least three columns.")
        sys.exit(1)

    # Ensure numeric columns from the second onward
    try:
        data.iloc[:, 1:] = data.iloc[:, 1:].apply(pd.to_numeric)
    except ValueError:
        print("Error: All columns from the 2nd to the last must contain numeric data.")
        sys.exit(1)

    # Parse and validate weights and impacts
    try:
        weights = list(map(float, weight_values.split(',')))
        impacts = impact_values.split(',')
    except Exception:
        print("Error: Weights and impacts must be properly formatted and separated by commas.")
        sys.exit(1)

    # Ensure matching counts for weights, impacts, and dataset columns
    if len(weights) != len(impacts) or len(weights) != (data.shape[1] - 1):
        print("Error: Counts of weights, impacts, and numeric columns must match.")
        sys.exit(1)

    # Validate that impacts are either '+' or '-'
    if not all(impact in ['+', '-'] for impact in impacts):
        print("Error: Impacts must only contain '+' or '-'.")
        sys.exit(1)

    # Normalize the dataset
    numeric_data = data.iloc[:, 1:].copy()
    for col in numeric_data.columns:
        norm_factor = math.sqrt(sum(value ** 2 for value in numeric_data[col]))
        numeric_data[col] = numeric_data[col] / norm_factor

    # Apply weights to the normalized data
    for index, col in enumerate(numeric_data.columns):
        numeric_data[col] *= weights[index]

    # Determine ideal best and worst values
    ideal_best = []
    ideal_worst = []
    for index, col in enumerate(numeric_data.columns):
        if impacts[index] == '+':
            ideal_best.append(numeric_data[col].max())
            ideal_worst.append(numeric_data[col].min())
        else:
            ideal_best.append(numeric_data[col].min())
            ideal_worst.append(numeric_data[col].max())

    # Calculate TOPSIS scores
    scores = []
    for row in numeric_data.itertuples(index=False):
        dist_to_best = math.sqrt(sum((row[idx] - ideal_best[idx]) ** 2 for idx in range(len(ideal_best))))
        dist_to_worst = math.sqrt(sum((row[idx] - ideal_worst[idx]) ** 2 for idx in range(len(ideal_worst))))
        scores.append(dist_to_worst / (dist_to_best + dist_to_worst))

    # Append scores and rankings to the dataset
    data['Topsis Score'] = scores
    data['Rank'] = data['Topsis Score'].rank(ascending=False).astype(int)

    # Save the results to the output file
    try:
        data.to_csv(output_filepath, index=False)
        print(f"Results successfully saved to '{output_filepath}'.")
    except Exception as error:
        print(f"Error: Unable to save the results. {str(error)}")
        sys.exit(1)

if __name__ == "__main__":
    # Exclude the script name from command-line arguments
    args = sys.argv[1:]
    topsis(args)
