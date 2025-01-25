import pandas as pd
import numpy as np
import sys

def normalize_data(data):
    """Normalize the data by dividing each element by the column's Euclidean norm."""
    return data / np.sqrt((data**2).sum(axis=0))

def calculate_weighted_matrix(normalized_data, weights):
    """Apply weights to the normalized data."""
    weights = np.array(weights)
    return normalized_data * weights

def calculate_ideal_solutions(weighted_data, impacts):
    """Determine the ideal and negative ideal solutions based on impacts."""
    ideal = []
    negative_ideal = []
    for i, impact in enumerate(impacts):
        column = weighted_data.iloc[:, i]
        if impact == '+':
            ideal.append(column.max())
            negative_ideal.append(column.min())
        elif impact == '-':
            ideal.append(column.min())
            negative_ideal.append(column.max())
        else:
            raise ValueError("Impacts must be '+' or '-' only.")
    return np.array(ideal), np.array(negative_ideal)

def compute_scores(weighted_data, ideal, negative_ideal):
    """Calculate TOPSIS scores based on distances to ideal and negative ideal solutions."""
    distances_to_ideal = np.sqrt(((weighted_data - ideal) ** 2).sum(axis=1))
    distances_to_negative_ideal = np.sqrt(((weighted_data - negative_ideal) ** 2).sum(axis=1))
    return distances_to_negative_ideal / (distances_to_ideal + distances_to_negative_ideal)

def assign_ranks(scores):
    """Rank the alternatives based on the scores (higher score = better rank)."""
    return scores.rank(ascending=False).astype(int)

def main():
    if len(sys.argv) != 5:
        print("Usage: python <script.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file, weights_str, impacts_str, output_file = sys.argv[1:]

    try:
        data = pd.read_csv(input_file)
        criteria_data = data.iloc[:, 1:]

        if criteria_data.shape[1] < 2:
            raise ValueError("Input file must have at least three columns: one for identifiers and two or more for criteria.")

        weights = list(map(float, weights_str.split(',')))
        impacts = impacts_str.split(',')

        if len(weights) != len(impacts) or len(weights) != criteria_data.shape[1]:
            raise ValueError("The number of weights and impacts must match the number of criteria columns.")

        if not criteria_data.apply(pd.to_numeric, errors='coerce').notna().all().all():
            raise ValueError("All criteria columns must contain numeric values only.")

        normalized_data = normalize_data(criteria_data)
        weighted_data = calculate_weighted_matrix(normalized_data, weights)
        ideal, negative_ideal = calculate_ideal_solutions(weighted_data, impacts)
        scores = compute_scores(weighted_data, ideal, negative_ideal)
        data['Topsis Score'] = scores
        data['Rank'] = assign_ranks(pd.Series(scores))

        data.to_csv(output_file, index=False)
        print(f"Results have been saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()

