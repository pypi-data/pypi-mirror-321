import pandas as pd
import sys
from scipy.stats import rankdata


def main():
    if len(sys.argv) != 5:
        return  # Exit if incorrect number of arguments is passed

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    # Load the data
    data = pd.read_csv(input_file)
    if len(data.columns) < 3:
        return  # Exit if less than three columns are present

    # Extract numeric data
    criteria_data = data.iloc[:, 1:].values
    alternatives = data.iloc[:, 0]

    # Parse weights and impacts
    weights = [float(w) for w in weights.split(",")]
    impacts = impacts.split(",")

    if len(weights) != criteria_data.shape[1] or len(impacts) != criteria_data.shape[1]:
        return  # Exit if weights/impacts don't match the number of criteria

    if not all(impact in ['+', '-'] for impact in impacts):
        return  # Exit if impacts are not valid ('+' or '-')

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

    # # Prepare output
    # data['Topsis Score'] = scores
    # data['Rank'] = scores.rank(ascending=False).astype(int)
    # data.to_csv(output_file, index=False)
    # Assuming `scores` is a NumPy array
    data['Topsis Score'] = scores
    data['Rank'] = rankdata(-scores, method='ordinal').astype(int)  # Negative scores for descending rank
    data.to_csv(output_file, index=False)


if __name__ == "__main__":
    main()


