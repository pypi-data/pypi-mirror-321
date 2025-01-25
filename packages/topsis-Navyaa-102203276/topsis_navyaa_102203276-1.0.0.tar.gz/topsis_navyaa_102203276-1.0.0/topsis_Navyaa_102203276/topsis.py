import sys
import pandas as pd
import numpy as np
import os

def topsis(matrix, weights, impacts):
    matrix = np.array(matrix, dtype=float)
    norm_matrix = matrix / np.sqrt(np.sum(matrix**2, axis=0))
    weighted_matrix = norm_matrix * weights

    ideal_best = np.where(impacts == 1, np.max(weighted_matrix, axis=0), np.min(weighted_matrix, axis=0))
    ideal_worst = np.where(impacts == 1, np.min(weighted_matrix, axis=0), np.max(weighted_matrix, axis=0))

    dist_best = np.sqrt(np.sum((weighted_matrix - ideal_best)**2, axis=1))
    dist_worst = np.sqrt(np.sum((weighted_matrix - ideal_worst)**2, axis=1))

    performance_scores = dist_worst / (dist_best + dist_worst)
    rankings = performance_scores.argsort()[::-1] + 1

    return performance_scores, rankings

def validate_input(data, weights, impacts):
    if data.shape[1] < 3:
        raise ValueError("Input dataset must have at least three columns.")

    if len(weights) != data.shape[1] - 1 or len(impacts) != data.shape[1] - 1:
        raise ValueError("Weights and impacts must match the number of criteria.")

    if not all(impact in [1, -1] for impact in impacts):
        raise ValueError("Impacts must be 1 (benefit) or -1 (cost).")

    if not np.issubdtype(data.iloc[:, 1:].dtypes.values[0], np.number):
        raise ValueError("All criteria columns must contain numeric values only.")

def main():
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <InputDataSet.csv> <Weights> <Impacts> <Result.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    weight_string = sys.argv[2]
    impact_string = sys.argv[3]
    output_file = sys.argv[4]

    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        sys.exit(1)

    try:
        dataset = pd.read_csv(input_file)
        criteria_matrix = dataset.iloc[:, 1:].values
    except Exception as e:
        print(f"Error reading the input file: {e}")
        sys.exit(1)

    try:
        weights = np.array(list(map(float, weight_string.split(','))))
        impacts = np.array(list(map(int, impact_string.split(','))))
    except ValueError:
        print("Error: Weights must be numeric, and impacts must be 1 or -1.")
        sys.exit(1)

    try:
        validate_input(dataset, weights, impacts)
    except ValueError as e:
        print(f"Input validation error: {e}")
        sys.exit(1)

    scores, rankings = topsis(criteria_matrix, weights, impacts)

    try:
        dataset["Score"] = scores
        dataset["Rank"] = rankings
        dataset.to_csv(output_file, index=False)
        print(f"Results successfully saved to {output_file}.")
    except Exception as e:
        print(f"Error saving the results: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
