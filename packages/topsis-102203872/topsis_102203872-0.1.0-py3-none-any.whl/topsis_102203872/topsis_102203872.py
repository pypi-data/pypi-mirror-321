import sys
import pandas as pd
import numpy as np
import openpyxl

def read_input_file(file_path):
    """Reads the input file and returns a dataframe."""
    try:
        if file_path.lower().endswith('.xlsx'):
            return pd.read_excel(file_path, engine='openpyxl')
        elif file_path.lower().endswith('.csv'):
            return pd.read_csv(file_path)
        else:
            print("Error: Unsupported file format. Please provide a .csv or .xlsx file.")
            sys.exit(1)
    except Exception as e:
        print(f"Error: Unable to read input file. {e}")
        sys.exit(1)

def validate_inputs(df, weights, impacts):
    """Validates the inputs for TOPSIS."""
    if len(weights) != len(impacts):
        print("Error: The number of weights and impacts must be the same.")
        sys.exit(1)

    if len(df.columns) - 1 != len(weights):
        print("Error: The number of weights and impacts must match the number of criteria (columns - 1).")
        sys.exit(1)

    if not all(isinstance(val, (int, float)) for val in df.iloc[:, 1:].values.flatten()):
        print("Error: All criteria values must be numeric.")
        sys.exit(1)

def calculate_topsis(df, weights, impacts):
    """Performs TOPSIS calculation and returns the updated dataframe."""
    data = df.iloc[:, 1:].values
    rows, cols = data.shape

    # Step 1: Normalize the decision matrix
    norm_matrix = data / np.sqrt((data ** 2).sum(axis=0))

    # Step 2: Multiply by weights
    weighted_matrix = norm_matrix * weights

    # Step 3: Determine ideal and negative ideal solutions
    ideal_solution = []
    negative_ideal_solution = []
    for j in range(cols):
        if impacts[j] == '+':
            ideal_solution.append(weighted_matrix[:, j].max())
            negative_ideal_solution.append(weighted_matrix[:, j].min())
        else:
            ideal_solution.append(weighted_matrix[:, j].min())
            negative_ideal_solution.append(weighted_matrix[:, j].max())

    # Step 4: Calculate separation measures
    separation_ideal = np.sqrt(((weighted_matrix - ideal_solution) ** 2).sum(axis=1))
    separation_negative = np.sqrt(((weighted_matrix - negative_ideal_solution) ** 2).sum(axis=1))

    # Step 5: Calculate performance scores
    scores = separation_negative / (separation_ideal + separation_negative)
    df['Topsis Score'] = scores
    df['Rank'] = scores.argsort()[::-1].argsort() + 1

    return df

def main():
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <input_file> <weights> <impacts> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = list(map(float, sys.argv[2].split(',')))
    impacts = sys.argv[3].split(',')
    output_file = sys.argv[4]

    # Read and validate input
    df = read_input_file(input_file)
    validate_inputs(df, weights, impacts)

    # Perform TOPSIS
    result_df = calculate_topsis(df, weights, impacts)

    # Save the result to the output file
    try:
        if output_file.lower().endswith('.xlsx'):
            result_df.to_excel(output_file, index=False, engine='openpyxl')
        elif output_file.lower().endswith('.csv'):
            result_df.to_csv(output_file, index=False)
        else:
            print("Error: Unsupported output file format. Please provide a .csv or .xlsx file.")
            sys.exit(1)
        print(f" Output saved to {output_file}")
    except Exception as e:
        print(f"Error: Unable to save output file. {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
