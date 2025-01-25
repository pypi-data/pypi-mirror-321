import pandas as pd
import sys
from scipy.stats import rankdata
import numpy as np
def main():
    if len(sys.argv) != 5:
        print("Error: Incorrect number of parameters. Expected: <inputFileName> <Weights> <Impacts> <resultFileName>")
        sys.exit(1)
    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    if len(data.columns) < 3:
        print("Error: Input file must contain three or more columns.")
        sys.exit(1)
    try:
        criteria_data = data.iloc[:, 1:].astype(float).values
    except ValueError:
        print("Error: All columns from 2nd to last must contain numeric values only.")
        sys.exit(1)
    try:
        weights = [float(w) for w in weights.split(",")]
    except ValueError:
        print("Error: Weights must be numeric and separated by commas.")
        sys.exit(1)
    impacts = impacts.split(",")
    if not all(impact in ['+', '-'] for impact in impacts):
        print("Error: Impacts must be either '+' or '-' and separated by commas.")
        sys.exit(1)
    if len(weights) != criteria_data.shape[1] or len(impacts) != criteria_data.shape[1]:
        print("Error: Number of weights, impacts, and criteria columns must be the same.")
        sys.exit(1)
    norm_data = criteria_data / np.sqrt((criteria_data ** 2).sum(axis=0))
    weighted_data = norm_data * weights
    ideal_best = [
        max(weighted_data[:, j]) if impacts[j] == '+' else min(weighted_data[:, j])
        for j in range(len(weights))
    ]
    ideal_worst = [
        min(weighted_data[:, j]) if impacts[j] == '+' else max(weighted_data[:, j])
        for j in range(len(weights))
    ]
    distances_to_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    distances_to_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))
    scores = distances_to_worst / (distances_to_best + distances_to_worst)
    data['Topsis Score'] = scores
    data['Rank'] = rankdata(-scores, method='ordinal')
    try:
        data.to_csv(output_file, index=False)
        print(f"Results successfully saved to '{output_file}'.")
    except Exception as e:
        print(f"Error: Could not save results to file. {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
