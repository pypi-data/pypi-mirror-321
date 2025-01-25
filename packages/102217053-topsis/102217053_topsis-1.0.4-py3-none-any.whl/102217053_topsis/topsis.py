import pandas as pd
import sys
from scipy.stats import rankdata


def main():
    if len(sys.argv) != 5:
        print("Error: Incorrect number of arguments passed.")
        print("Usage: python topsis.py <input_file> <weights> <impacts> <output_file>")
        return

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    try:
        # Load the data
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if len(data.columns) < 3:
        print("Error: Input file must have at least three columns.")
        return

    # Extract numeric data
    criteria_data = data.iloc[:, 1:].values
    alternatives = data.iloc[:, 0]

    # Parse weights and impacts
    try:
        weights = [float(w) for w in weights.split(",")]
    except ValueError:
        print("Error: Weights must be a comma-separated list of numbers.")
        return

    impacts = impacts.split(",")
    if len(weights) != criteria_data.shape[1] or len(impacts) != criteria_data.shape[1]:
        print("Error: Number of weights/impacts does not match the number of criteria.")
        return

    if not all(impact in ['+', '-'] for impact in impacts):
        print("Error: Impacts must only contain '+' or '-'.")
        return

    try:
        # Normalize the data
        norm_data = criteria_data / (criteria_data**2).sum(axis=0)**0.5

        # Apply weights
        weighted_data = norm_data * weights

        # Identify ideal best and worst
        ideal_best = [max(weighted_data[:, j]) if impacts[j] == '+' else min(weighted_data[:, j]) for j in range(len(weights))]
        ideal_worst = [min(weighted_data[:, j]) if impacts[j] == '+' else max(weighted_data[:, j]) for j in range(len(weights))]

        # Calculate distances and scores
        distances_to_best = ((weighted_data - ideal_best)**2).sum(axis=1)**0.5
        distances_to_worst = ((weighted_data - ideal_worst)**2).sum(axis=1)**0.5
        scores = distances_to_worst / (distances_to_best + distances_to_worst)

        # Prepare output
        data['Topsis Score'] = scores
        data['Rank'] = rankdata(-scores, method='ordinal').astype(int)
        data.to_csv(output_file, index=False)
        print(f"Output saved to '{output_file}'.")
    except Exception as e:
        print(f"An error occurred during computation: {e}")


if __name__ == "__main__":
    main()
