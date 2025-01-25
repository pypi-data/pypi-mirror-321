import os
import sys
import numpy as np
import pandas as pd

def convert_to_float(data):
    """Convert input array to floats."""
    try:
        return np.array(data, dtype=float)
    except ValueError:
        print("Error: Non-numeric values found in the numeric columns.")
        exit(1)

def normalize_decision_matrix(matrix):
    """Normalize the decision matrix."""
    norm_matrix = matrix / np.sqrt(np.sum(matrix**2, axis=0))
    return norm_matrix

def apply_weights(normalized_matrix, weights):
    """Apply weights to the normalized decision matrix."""
    weighted_matrix = normalized_matrix * weights
    return weighted_matrix

def calculate_ideal_best_worst(weighted_matrix, impacts):
    """Calculate ideal best and worst values based on impacts."""
    ideal_best = []
    ideal_worst = []

    for col, impact in zip(weighted_matrix.T, impacts):
        if impact == 1:  # Positive impact
            ideal_best.append(np.max(col))
            ideal_worst.append(np.min(col))
        else:  # Negative impact
            ideal_best.append(np.min(col))
            ideal_worst.append(np.max(col))

    return np.array(ideal_best), np.array(ideal_worst)

def calculate_distances(weighted_matrix, ideal_best, ideal_worst):
    """Calculate distances from ideal best and worst values."""
    distance_to_best = np.sqrt(np.sum((weighted_matrix - ideal_best)**2, axis=1))
    distance_to_worst = np.sqrt(np.sum((weighted_matrix - ideal_worst)**2, axis=1))
    return distance_to_best, distance_to_worst

def calculate_topsis_scores(distance_to_best, distance_to_worst):
    """Calculate TOPSIS performance scores."""
    scores = distance_to_worst / (distance_to_best + distance_to_worst)
    return scores

def topsis(input_data, weights, impacts):
    """Perform TOPSIS analysis."""
    numeric_data = convert_to_float(input_data)
    normalized_matrix = normalize_decision_matrix(numeric_data)
    weighted_matrix = apply_weights(normalized_matrix, weights)
    ideal_best, ideal_worst = calculate_ideal_best_worst(weighted_matrix, impacts)
    distance_to_best, distance_to_worst = calculate_distances(weighted_matrix, ideal_best, ideal_worst)
    scores = calculate_topsis_scores(distance_to_best, distance_to_worst)
    return scores

def run(df, weights, impact, output):
    """Handle CLI input and perform TOPSIS analysis."""
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        print("Example: python 1015579.py 1015579-data.xlsx \"1,1,1,2\" \"+,+,-,+\" 1015579-result.xlsx")
        exit(1)

    input_file = df
    impacts=impact
    # weights = list(map(float, sys.argv[2].strip('"').split(',')))
    # impacts = [1 if impact == '+' else 0 for impact in sys.argv[3].strip('"').split(',')]
    result_file = output

    # Read input file
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        exit(1)

    try:
        if input_file.endswith('.csv'):
            data = pd.read_csv(input_file)
        elif input_file.endswith('.xlsx'):
            data = pd.read_excel(input_file)
        else:
            print("Error: Unsupported file format. Use CSV or Excel.")
            exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        exit(1)

    # Separate the identifier column and numeric data
    identifiers = data.iloc[:, 0]
    numeric_columns = data.iloc[:, 1:]

    if numeric_columns.select_dtypes(include=[np.number]).empty:
        print("Error: No numeric data found in the file.")
        exit(1)

    # Perform TOPSIS
    scores = topsis(numeric_columns.values, weights, impacts)

    # Add scores and ranks to the dataframe
    data['Topsis Score'] = scores
    data['Rank'] = data['Topsis Score'].rank(ascending=False).astype(int)

    # Save the results
    try:
        if result_file.endswith('.csv'):
            data.to_csv(result_file, index=False)
        elif result_file.endswith('.xlsx'):
            data.to_excel(result_file, index=False)
        else:
            print("Error: Unsupported output file format. Use CSV or Excel.")
            exit(1)
        print(f"Results saved to {result_file}")
    except Exception as e:
        print(f"Error saving results: {e}")
        exit(1)



# if __name__ == '__main__':
    # main()
