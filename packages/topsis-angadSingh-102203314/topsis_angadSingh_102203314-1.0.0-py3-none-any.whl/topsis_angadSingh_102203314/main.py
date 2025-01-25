# -*- coding: utf-8 -*-
import math
import pandas as pd
import sys
import os

def topsis(arglist):
    # Validate the number of arguments
    if len(arglist) != 4:
        print("Error: Incorrect number of parameters. Required: inputFileName, Weights, Impacts, resultFileName.")
        sys.exit(1)

    input_file, weights_str, impacts_str, output_file = arglist

    # Check if the file exists
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    try:
        # Read the dataset
        dataset = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error: Could not read the input file. {str(e)}")
        sys.exit(1)

    # Validate the number of columns
    if dataset.shape[1] < 3:
        print("Error: Input file must contain at least three columns.")
        sys.exit(1)

    # Check for numeric values in the required columns
    try:
        dataset.iloc[:, 1:] = dataset.iloc[:, 1:].apply(pd.to_numeric)
    except ValueError:
        print("Error: Columns from the 2nd to the last must contain numeric values only.")
        sys.exit(1)

    # Parse weights and impacts
    try:
        weights = list(map(float, weights_str.split(',')))
        impacts = impacts_str.split(',')
    except Exception:
        print("Error: Weights and impacts must be separated by commas and formatted correctly.")
        sys.exit(1)

    # Validate weights, impacts, and column counts
    if len(weights) != len(impacts) or len(weights) != (dataset.shape[1] - 1):
        print("Error: The number of weights, impacts, and numeric columns must be the same.")
        sys.exit(1)

    # Validate impacts
    if not all(impact in ['+', '-'] for impact in impacts):
        print("Error: Impacts must be either '+' or '-'.")
        sys.exit(1)

    # Normalize the dataset
    dataset_numeric = dataset.iloc[:, 1:].copy()
    for col in dataset_numeric:
        x_denom = math.sqrt(sum(x * x for x in dataset_numeric[col]))
        dataset_numeric[col] = dataset_numeric[col] / x_denom

    # Apply weights
    for i, col in enumerate(dataset_numeric.columns):
        dataset_numeric[col] = dataset_numeric[col] * weights[i]

    # Calculate ideal best and ideal worst
    vpos = []
    vneg = []
    for i, col in enumerate(dataset_numeric.columns):
        if impacts[i] == "+":
            vpos.append(max(dataset_numeric[col]))
            vneg.append(min(dataset_numeric[col]))
        else:
            vpos.append(min(dataset_numeric[col]))
            vneg.append(max(dataset_numeric[col]))

    # Calculate performance scores
    pscore = []
    for row in dataset_numeric.itertuples(index=False):
        eucdisp = math.sqrt(sum((row[i] - vpos[i]) ** 2 for i in range(len(vpos))))
        eucdisn = math.sqrt(sum((row[i] - vneg[i]) ** 2 for i in range(len(vneg))))
        pscore.append(eucdisn / (eucdisp + eucdisn))

    # Assign ranks
    dataset['Topsis Score'] = pscore
    dataset['Rank'] = dataset['Topsis Score'].rank(ascending=False).astype(int)

    # Save the output
    try:
        dataset.to_csv(output_file, index=False)
        print(f"Output saved to {output_file}")
    except Exception as e:
        print(f"Error: Could not save the output file. {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    sysarglist = sys.argv
    sysarglist.pop(0) 
    topsis(sysarglist)
