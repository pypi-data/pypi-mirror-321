import numpy as np
import pandas as pd
import sys

def topsis(inputFileName, weights, impacts, resultFileName):
    try:
        data = pd.read_csv(inputFileName)
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

    if data.shape[1] < 3:
        print("Error: Input file must contain three or more columns.")
        return

   
    try:
        criteria = data.iloc[:, 1:].values
        criteria = criteria.astype(float)  # Ensure numeric values only
    except ValueError:
        print("Error: From 2nd to last columns must contain numeric values only.")
        return

    if len(weights) != criteria.shape[1] or len(impacts) != criteria.shape[1]:
        print("Error: Number of weights, impacts, and criteria columns must be the same.")
        return

    try:
        weights = np.array(weights, dtype=float)
    except ValueError:
        print("Error: Weights must be numeric values.")
        return

    if not all(impact in ['+', '-'] for impact in impacts):
        print("Error: Impacts must be either '+' (beneficial) or '-' (non-beneficial).")
        return

    beneficial = np.array([1 if impact == '+' else 0 for impact in impacts])

    norm_criteria = criteria / np.sqrt((criteria ** 2).sum(axis=0))

    weighted_criteria = norm_criteria * weights

    ideal_solution = np.max(weighted_criteria, axis=0) * beneficial + np.min(weighted_criteria, axis=0) * (1 - beneficial)
    negative_ideal_solution = np.min(weighted_criteria, axis=0) * beneficial + np.max(weighted_criteria, axis=0) * (1 - beneficial)

    separation_ideal = np.sqrt(((weighted_criteria - ideal_solution) ** 2).sum(axis=1))
    separation_negative = np.sqrt(((weighted_criteria - negative_ideal_solution) ** 2).sum(axis=1))

    topsis_score = separation_negative / (separation_ideal + separation_negative)

    # Add scores and rankings to the dataset
    data['TOPSIS Score'] = topsis_score.astype(np.float16)
    data['Rank'] = data['TOPSIS Score'].rank(ascending=False).astype(int)

    try:
        data.to_csv(resultFileName, index=False)
        print(f"Results successfully saved to {resultFileName}")
    except Exception as e:
        print(f"Error: Could not save results to file. {e}")

if __name__ == "__main__":
    print("Interactive TOPSIS Tool")
    inputFileName = input("Enter the path to the input CSV file: ").strip()
    weights = list(map(float, input("Enter weights (comma-separated): ").strip().split(',')))
    impacts = input("Enter impacts (comma-separated, '+' for beneficial, '-' for non-beneficial): ").strip().split(',')
    resultFileName = input("Enter the path to save the result CSV file: ").strip()
    
    topsis(inputFileName, weights, impacts, resultFileName)