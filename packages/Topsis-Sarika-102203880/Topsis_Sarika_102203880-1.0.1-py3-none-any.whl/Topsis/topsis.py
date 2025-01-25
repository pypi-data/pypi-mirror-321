import sys
import pandas as pd
import numpy as np

def normalize_data(data):
    """Normalize the decision matrix."""
    normalized = data / np.sqrt((data**2).sum(axis=0))
    return normalized

def calculate_ideal_solutions(normalized_data, impacts):
    """Calculate ideal best and ideal worst solutions."""
    ideal_best = []
    ideal_worst = []
    for i, impact in enumerate(impacts):
        if impact == '+':
            ideal_best.append(normalized_data[:, i].max())
            ideal_worst.append(normalized_data[:, i].min())
        elif impact == '-':
            ideal_best.append(normalized_data[:, i].min())
            ideal_worst.append(normalized_data[:, i].max())
    return np.array(ideal_best), np.array(ideal_worst)

def topsis(data, weights, impacts):
    """Perform the TOPSIS calculation."""
    decision_matrix = data.iloc[:, 1:].values  # Exclude the first column (e.g., Fund Name)
    weights = np.array(weights)

    # Normalize the decision matrix
    normalized_data = normalize_data(decision_matrix)

    # Apply weights
    weighted_data = normalized_data * weights

    # Calculate ideal best and ideal worst solutions
    ideal_best, ideal_worst = calculate_ideal_solutions(weighted_data, impacts)

    # Calculate distances to ideal solutions
    distance_to_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    distance_to_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    # Calculate Topsis score
    scores = distance_to_worst / (distance_to_best + distance_to_worst)
    return scores

def main():
    # Step 1: Validate command-line arguments
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = list(map(float, sys.argv[2].split(',')))
    impacts = sys.argv[3].split(',')
    result_file = sys.argv[4]

    # Step 2: Read input data
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
        sys.exit(1)

    # Step 3: Validate input data
    if data.shape[1] < 3:
        print("Error: Input file must contain at least three columns.")
        sys.exit(1)

    if len(weights) != data.shape[1] - 1:
        print("Error: Number of weights must match the number of criteria.")
        sys.exit(1)

    if len(impacts) != data.shape[1] - 1:
        print("Error: Number of impacts must match the number of criteria.")
        sys.exit(1)

    if any(impact not in ['+', '-'] for impact in impacts):
        print("Error: Impacts should only be '+' or '-'.")
        sys.exit(1)

    try:
        # Ensure numeric values in the criteria columns
        data.iloc[:, 1:] = data.iloc[:, 1:].astype(float)
    except ValueError:
        print("Error: All criteria values must be numeric.")
        sys.exit(1)

    # Step 4: Calculate Topsis score
    scores = topsis(data, weights, impacts)

    # Step 5: Add scores and ranks to the data
    data['Topsis Score'] = scores
    data['Rank'] = data['Topsis Score'].rank(ascending=False, method='min')

    # Step 6: Save results to a CSV file
    try:
        data.to_csv(result_file, index=False)
        print(f"Results saved to {result_file}")
    except Exception as e:
        print(f"Error: Unable to save results to {result_file}. {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
