import sys
import pandas as pd
import numpy as np

def validate_inputs(arguments):
    if len(arguments) != 5:
        raise ValueError("Invalid number of arguments. Expected 4: (InputFile, Weights, Impacts, ResultFile).")

    try:
        weights = [float(w) for w in arguments[2].split(',')]
    except ValueError:
        raise ValueError("Weights must be a comma-separated list of numeric values.")

    impacts = arguments[3].split(',')
    if not all(impact in ['+', '-'] for impact in impacts):
        raise ValueError("Impacts must only contain '+' or '-' values.")

    return weights, impacts

def topsis(input_file, weights, impacts, result_file):
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The input file '{input_file}' was not found.")
    except Exception as e:
        raise Exception(f"Error while reading the input file: {e}")

    if data.shape[1] < 3:
        raise ValueError("The input file must have at least three columns (Object/Variable and numeric values).")

    for col in data.columns[1:]:
        if not pd.api.types.is_numeric_dtype(data[col]):
            raise ValueError(f"Column '{col}' contains non-numeric values, which are not allowed.")

    if len(weights) != len(data.columns[1:]) or len(impacts) != len(data.columns[1:]):
        raise ValueError("The number of weights and impacts must match the number of criteria columns.")

    # Normalize the dataset
    normalized_matrix = data.iloc[:, 1:].div(np.sqrt((data.iloc[:, 1:] ** 2).sum(axis=0)), axis=1)

    # Apply weights to normalized values
    weighted_matrix = normalized_matrix * weights

    # Calculate ideal best and worst values
    ideal_best = []
    ideal_worst = []

    for i, impact in enumerate(impacts):
        if impact == '+':
            ideal_best.append(weighted_matrix.iloc[:, i].max())
            ideal_worst.append(weighted_matrix.iloc[:, i].min())
        else:
            ideal_best.append(weighted_matrix.iloc[:, i].min())
            ideal_worst.append(weighted_matrix.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Compute distances to ideal best and worst
    distance_to_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    distance_to_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Calculate TOPSIS scores
    topsis_scores = distance_to_worst / (distance_to_best + distance_to_worst)
    data['Topsis Score'] = topsis_scores
    data['Rank'] = topsis_scores.rank(ascending=False).astype(int)

    # Save results to the output file
    data.to_csv(result_file, index=False)

if __name__ == "__main__":
    try:
        weights, impacts = validate_inputs(sys.argv)
        topsis(sys.argv[1], weights, impacts, sys.argv[4])
        print(f"The results have been successfully saved to {sys.argv[4]}")
    except Exception as e:
        print(f"An error occurred: {e}")
