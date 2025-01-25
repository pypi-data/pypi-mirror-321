import sys
import pandas as pd
import numpy as np

def validate_inputs(input_file, weights, impacts, result_file):
    try:
        # Check if file exists and is readable
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Error: Input file not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)
    
    # Check for minimum column requirements
    if data.shape[1] < 3:
        print("Error: Input file must have at least 3 columns.")
        sys.exit(1)

    # Check for numeric values in all columns except the first
    if not np.all(data.iloc[:, 1:].applymap(np.isreal)):
        print("Error: From 2nd to last columns, all values must be numeric.")
        sys.exit(1)

    # Validate weights and impacts
    weights = weights.split(",")
    impacts = impacts.split(",")

    if len(weights) != (data.shape[1] - 1) or len(impacts) != (data.shape[1] - 1):
        print("Error: Number of weights and impacts must match the number of criteria (columns from 2nd to last).")
        sys.exit(1)
    
    try:
        weights = [float(w) for w in weights]
    except ValueError:
        print("Error: Weights must be numeric values separated by commas.")
        sys.exit(1)

    if not all(impact in ["+", "-"] for impact in impacts):
        print("Error: Impacts must be '+' or '-' separated by commas.")
        sys.exit(1)

    return data, weights, impacts

def topsis(input_file, weights, impacts, result_file):
    # Validate inputs
    data, weights, impacts = validate_inputs(input_file, weights, impacts, result_file)
    
    # Normalize the decision matrix
    matrix = data.iloc[:, 1:].values
    norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))
    
    # Apply weights
    weighted_matrix = norm_matrix * weights

    # Calculate ideal best and worst
    ideal_best = np.max(weighted_matrix, axis=0) if impacts[0] == "+" else np.min(weighted_matrix, axis=0)
    ideal_worst = np.min(weighted_matrix, axis=0) if impacts[0] == "+" else np.max(weighted_matrix, axis=0)
    
    for i, impact in enumerate(impacts):
        if impact == "+":
            ideal_best[i] = np.max(weighted_matrix[:, i])
            ideal_worst[i] = np.min(weighted_matrix[:, i])
        else:
            ideal_best[i] = np.min(weighted_matrix[:, i])
            ideal_worst[i] = np.max(weighted_matrix[:, i])

    # Calculate distances from ideal best and worst
    dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Calculate TOPSIS score
    scores = dist_worst / (dist_best + dist_worst)
    data["Topsis Score"] = scores

    # Assign ranks
    data["Rank"] = pd.Series(scores).rank(ascending=False).astype(int)

    # Save to result file
    try:
        data.to_csv(r"C:\Users\hp\OneDrive\Desktop\TOPSIS\result.csv", index=False)
        print(f"Results saved to {result_file}")
    except Exception as e:
        print(f"Error saving results to file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result_file = sys.argv[4]

    print(f"Input File: {input_file}")
    print(f"Weights: {weights}")
    print(f"Impacts: {impacts}")
    print(f"Result File: {result_file}")

    topsis(input_file, weights, impacts, result_file)
