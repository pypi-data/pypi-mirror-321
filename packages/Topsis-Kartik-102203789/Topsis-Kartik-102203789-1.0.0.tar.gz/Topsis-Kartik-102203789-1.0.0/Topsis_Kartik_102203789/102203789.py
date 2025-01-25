import sys
import os
import numpy as np
import pandas as pd

def topsis(data, weights, impacts):
    # Normalize the decision matrix
    norm_data = data.iloc[:, 1:] / np.sqrt((data.iloc[:, 1:] ** 2).sum())

    # Apply weights
    weighted_data = norm_data * weights

    # Determine ideal best and worst
    ideal_best = np.where(impacts == '+', weighted_data.max(), weighted_data.min())
    ideal_worst = np.where(impacts == '+', weighted_data.min(), weighted_data.max())

    # Calculate distances from ideal best and worst
    dist_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    # Calculate TOPSIS score
    scores = dist_worst / (dist_best + dist_worst)

    # Add scores to the dataframe and rank them
    data['TOPSIS Score'] = scores
    data['Rank'] = scores.rank(ascending=False)

    return data

def validate_inputs(file_path, weights, impacts):
    # Check if file exists
    if not os.path.isfile(file_path):
        print("Error: File not found.")
        sys.exit(1)

    # Check if weights and impacts are valid
    try:
        weights = np.array([float(w) for w in weights.split(',')])
    except ValueError:
        print("Error: Weights must be numeric and separated by commas.")
        sys.exit(1)

    if not all(i in ['+', '-'] for i in impacts.split(',')):
        print("Error: Impacts must be '+' or '-' and separated by commas.")
        sys.exit(1)

    return weights, np.array(impacts.split(','))

def main():
    # Check the number of command line arguments
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    # Parse command line arguments
    input_file = sys.argv[1]
    weights_input = sys.argv[2]
    impacts_input = sys.argv[3]
    result_file = sys.argv[4]

    # Validate inputs
    weights, impacts = validate_inputs(input_file, weights_input, impacts_input)

    # Load and validate the input file
    try:
        data = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    if data.shape[1] < 3:
        print("Error: Input file must contain at least three columns.")
        sys.exit(1)

    try:
        numeric_data = data.iloc[:, 1:].apply(pd.to_numeric)
    except ValueError:
        print("Error: All values from 2nd to last columns must be numeric.")
        sys.exit(1)

    if len(weights) != numeric_data.shape[1] or len(impacts) != numeric_data.shape[1]:
        print("Error: Number of weights, impacts, and numeric columns must be the same.")
        sys.exit(1)

    # Apply TOPSIS
    result_data = topsis(data, weights, impacts)

    # Save the results
    try:
        result_data.to_csv(result_file, index=False)
        print(f"Results saved to {result_file}")
    except Exception as e:
        print(f"Error: Could not save results. {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
