import sys
import pandas as pd
import numpy as np
import os

def compute_topsis(matrix, weights, impacts):
    matrix = np.array(matrix)

    # Normalize the decision matrix
    norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))

    # Apply weights to the normalized matrix
    weighted_matrix = norm_matrix * weights

    # Determine the ideal and negative ideal solutions
    ideal_best = np.where(impacts == 1, weighted_matrix.max(axis=0), weighted_matrix.min(axis=0))
    ideal_worst = np.where(impacts == 1, weighted_matrix.min(axis=0), weighted_matrix.max(axis=0))

    # Calculate distances to the ideal and negative ideal solutions
    dist_to_ideal = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
    dist_to_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))

    # Compute the TOPSIS score
    scores = dist_to_worst / (dist_to_ideal + dist_to_worst)

    # Rank alternatives based on scores
    rankings = scores.argsort()[::-1] + 1
    return scores, rankings

def main():
    if len(sys.argv) != 5:
        print("Usage: python topsis_102203677.py <InputDataSet.csv> <Weights> <Impacts> <Result.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights_input = sys.argv[2]
    impacts_input = sys.argv[3]
    output_file = sys.argv[4]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)

    try:
        # Load the input dataset
        data = pd.read_csv(input_file)
        if data.shape[1] < 3:
            print("Error: The dataset must contain at least three columns (ID and criteria).")
            sys.exit(1)

        # Extract criteria values
        matrix = data.iloc[:, 1:].values
    except Exception as e:
        print(f"Error: Unable to read the input file. {e}")
        sys.exit(1)

    try:
        # Parse weights and impacts
        weights = np.array(list(map(float, weights_input.split(','))))
        impacts = np.array([1 if impact == '+' else -1 for impact in impacts_input.split(',')])

        if len(weights) != matrix.shape[1] or len(impacts) != matrix.shape[1]:
            print("Error: The number of weights and impacts must match the number of criteria.")
            sys.exit(1)
    except ValueError:
        print("Error: Weights must be numeric values, and impacts must be '+' or '-'.")
        sys.exit(1)

    if not np.issubdtype(matrix.dtype, np.number):
        print("Error: All criteria columns must contain numeric data.")
        sys.exit(1)

    # Compute TOPSIS scores and rankings
    try:
        scores, rankings = compute_topsis(matrix, weights, impacts)

        # Add scores and rankings to the dataset
        data['Score'] = scores
        data['Rank'] = rankings

        # Save the results to the output file
        data.to_csv(output_file, index=False)
        print(f"Results successfully saved to {output_file}")
    except Exception as e:
        print(f"Error: An error occurred during computation. {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
