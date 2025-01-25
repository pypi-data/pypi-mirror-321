import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):
    # Load the input file
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    # Check if the input file has at least 3 columns
    if data.shape[1] < 3:
        print("Error: Input file must have at least three columns.")
        sys.exit(1)

    # Extract weights and impacts
    try:
        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')
    except ValueError:
        print("Error: Weights and impacts must be comma-separated and properly formatted.")
        sys.exit(1)

    # Validate weights and impacts
    if len(weights) != (data.shape[1] - 1) or len(impacts) != (data.shape[1] - 1):
        print("Error: Number of weights and impacts must match the number of criteria (columns excluding the first).")
        sys.exit(1)

    if not all(impact in ['+', '-'] for impact in impacts):
        print("Error: Impacts must be '+' or '-'.")
        sys.exit(1)

    # Normalize the decision matrix
    decision_matrix = data.iloc[:, 1:].values
    norm_matrix = decision_matrix / np.sqrt((decision_matrix**2).sum(axis=0))

    # Apply weights
    weighted_matrix = norm_matrix * weights

    # Determine ideal best and ideal worst
    ideal_best = np.max(weighted_matrix, axis=0) if impacts[0] == '+' else np.min(weighted_matrix, axis=0)
    ideal_worst = np.min(weighted_matrix, axis=0) if impacts[0] == '+' else np.max(weighted_matrix, axis=0)

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best[i] = np.max(weighted_matrix[:, i])
            ideal_worst[i] = np.min(weighted_matrix[:, i])
        else:
            ideal_best[i] = np.min(weighted_matrix[:, i])
            ideal_worst[i] = np.max(weighted_matrix[:, i])

    # Calculate separation measures
    separation_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
    separation_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))

    # Calculate TOPSIS scores
    topsis_scores = separation_worst / (separation_best + separation_worst)

    # Rank the scores
    ranks = topsis_scores.argsort()[::-1] + 1

    # Append scores and ranks to the dataframe
    data['Topsis Score'] = topsis_scores
    data['Rank'] = ranks

    # Save the result to the output file
    try:
        data.to_csv(output_file, index=False)
        print(f"Results saved to '{output_file}'.")
    except Exception as e:
        print(f"Error saving results: {e}")
        sys.exit(1)

# Main program execution
def main():
    if len(sys.argv) != 5:
        print("Usage: python -m topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    topsis(input_file, weights, impacts, output_file)

if __name__ == '__main__':
    main()