import pandas as pd
import numpy as np
import sys


def validate_inputs(data, weights, impacts):
    """
    Validates the input data, weights, and impacts.
    """
    if len(data.columns) < 3:
        raise ValueError("Input file must have at least three columns.")

    if len(weights) != data.shape[1] - 1 or len(impacts) != data.shape[1] - 1:
        raise ValueError("Number of weights and impacts must match the number of criteria.")

    if not all(impact in ['+', '-'] for impact in impacts):
        raise ValueError("Impacts must be '+' or '-'.")


def normalize_data(criteria_data):
    """
    Normalizes the criteria data using the Euclidean norm.
    """
    return criteria_data / np.sqrt((criteria_data**2).sum(axis=0))


def calculate_topsis(data, weights, impacts):
    """
    Performs the TOPSIS calculation.
    """
    criteria_data = data.iloc[:, 1:].values
    weights = np.array(weights)
    impacts = np.array(impacts)

    # Normalize the data
    norm_data = normalize_data(criteria_data)

    # Apply weights
    weighted_data = norm_data * weights

    # Determine ideal best and worst values
    ideal_best = np.where(impacts == '+', weighted_data.max(axis=0), weighted_data.min(axis=0))
    ideal_worst = np.where(impacts == '+', weighted_data.min(axis=0), weighted_data.max(axis=0))

    # Calculate distances to ideal best and worst
    distances_to_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    distances_to_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    # Calculate scores
    scores = distances_to_worst / (distances_to_best + distances_to_worst)

    return scores


def topsis(input_file, weights, impacts, output_file):
    """
    Main function to execute TOPSIS and save results.
    """
    # Load the dataset
    data = pd.read_csv(input_file)

    # Parse weights and impacts
    weights = [float(w) for w in weights.split(",")]
    impacts = impacts.split(",")

    # Validate inputs
    validate_inputs(data, weights, impacts)

    # Perform TOPSIS calculation
    scores = calculate_topsis(data, weights, impacts)

    # Add results to the data
    data['Topsis Score'] = scores
    data['Rank'] = (-scores).argsort().argsort() + 1  # Descending order for ranks

    # Save the output file
    data.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <input_file> <weights> <impacts> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    try:
        topsis(input_file, weights, impacts, output_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
