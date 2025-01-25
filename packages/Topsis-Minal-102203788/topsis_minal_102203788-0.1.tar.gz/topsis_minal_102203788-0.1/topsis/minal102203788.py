import pandas as pd
import numpy as np
import sys

def validate_inputs(input_file, weights, impacts):
    # Validate input file existence
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Error: Input file not found.")
        sys.exit(1)

    # Validate column count
    if data.shape[1] < 3:
        print("Error: Input file must contain at least three columns.")
        sys.exit(1)

    # Validate numeric columns
    non_numeric_columns = data.iloc[:, 1:].apply(lambda col: pd.to_numeric(col, errors='coerce').isna().any())
    if non_numeric_columns.any():
        print(f"Error: Columns {list(data.iloc[:, 1:].columns[non_numeric_columns])} contain non-numeric values.")
        sys.exit(1)

    # Validate weights and impacts
    weight = list(map(float, weights.split(',')))
    impact = impacts.split(',')

    if len(weight) != len(impact) or len(weight) != data.shape[1] - 1:
        print("Error: Number of weights, impacts, and numeric columns must be the same.")
        sys.exit(1)

    if not all(i in ['+', '-'] for i in impact):
        print("Error: Impacts must be either '+' or '-'.")
        sys.exit(1)

    return data, weight, impact
def topsis(input_file, weights, impacts, output_file):
    # Read and validate the input file
    data, weight, impact_list = validate_inputs(input_file, weights, impacts)

    # Extract numeric data
    matrix = data.iloc[:, 1:].values
    row_names = data.iloc[:, 0].values

    # Step 1: Normalize the matrix
    norm_matrix = matrix / np.sqrt((matrix ** 2).sum(axis=0))

    # Step 2: Weighted normalized decision matrix
    weighted_matrix = norm_matrix * weight

    # Step 3: Determine ideal best and worst values
    ideal_best = np.max(weighted_matrix, axis=0) if impact_list[0] == '+' else np.min(weighted_matrix, axis=0)
    ideal_worst = np.min(weighted_matrix, axis=0) if impact_list[0] == '+' else np.max(weighted_matrix, axis=0)

    # Step 4: Calculate separation measures
    separation_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    separation_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Calculate the Topsis score
    scores = separation_worst / (separation_best + separation_worst)

    # Add Topsis score and rank to the original data
    data['Topsis Score'] = scores
    data['Rank'] = scores.argsort()[::-1].argsort() + 1

    # Save the result
    data.to_csv(output_file, index=False)
    print(f"Result file saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <RollNumber>.py <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]
    topsis(input_file, weights, impacts, output_file)
