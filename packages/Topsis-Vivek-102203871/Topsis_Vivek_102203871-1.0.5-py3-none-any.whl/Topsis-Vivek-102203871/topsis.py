import os
import sys
import pandas as pd
import numpy as np

def validate_inputs(data, weights, impacts):
    if data.shape[1] < 3:
        raise ValueError("Input file must have at least three columns.")

    matrix = data.iloc[:, 1:]  # Exclude the first column (object names)

    # Validate numeric columns
    matrix = matrix.apply(pd.to_numeric, errors='coerce')
    if matrix.isnull().values.any():
        raise ValueError("Non-numeric or invalid values found in the matrix.")

    # Validate weights and impacts
    num_criteria = matrix.shape[1]
    weights = [float(w.strip()) for w in weights.split(",")]
    impacts = [i.strip() for i in impacts.split(",")]

    if len(weights) != num_criteria or len(impacts) != num_criteria:
        raise ValueError("Number of weights and impacts must match the number of criteria (columns 2 to last).")

    if not all(i in ['+', '-'] for i in impacts):
        raise ValueError("Impacts must be '+' or '-'.")

    return matrix, weights, impacts


def topsis(input_file, weights, impacts, output_file):
    try:
        print("Starting Topsis calculation...")
        print(f"Input file: {input_file}")
        print(f"Output file: {output_file}")

        # Check if input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError("Input file not found. Ensure the file path is correct.")

        # Load the file
        file_extension = os.path.splitext(input_file)[-1].lower()
        if file_extension == ".csv":
            data = pd.read_csv(input_file)
        elif file_extension == ".xlsx":
            data = pd.read_excel(input_file, engine="openpyxl")
        else:
            raise ValueError("Unsupported file format. Use .csv or .xlsx.")

        print("Input file loaded successfully.")

        # Validate inputs
        matrix, weights, impacts = validate_inputs(data, weights, impacts)
        print("Inputs validated successfully.")

        # Normalize the matrix
        norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))

        # Apply weights
        weighted_matrix = norm_matrix * weights

        # Calculate ideal and negative-ideal solutions
        ideal_solution = np.where(np.array(impacts) == '+', weighted_matrix.max(axis=0), weighted_matrix.min(axis=0))
        negative_ideal_solution = np.where(np.array(impacts) == '+', weighted_matrix.min(axis=0), weighted_matrix.max(axis=0))

        # Calculate distances
        pos_distance = np.sqrt(((weighted_matrix - ideal_solution)**2).sum(axis=1))
        neg_distance = np.sqrt(((weighted_matrix - negative_ideal_solution)**2).sum(axis=1))

        # Calculate scores and ranks
        scores = neg_distance / (pos_distance + neg_distance)
        ranks = scores.argsort()[::-1] + 1

        # Add results to the original data
        data['Topsis Score'] = scores
        data['Rank'] = ranks

        # Save the result to a file
        data.to_csv(output_file, index=False)
        print(f"Topsis results saved successfully to: {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python 102203871.py <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        print('Example: python 102203871.py 102203871-data.xlsx "1,1,1,2" "+,+,-,+" 102203871-result.csv')
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    topsis(input_file, weights, impacts, output_file)
