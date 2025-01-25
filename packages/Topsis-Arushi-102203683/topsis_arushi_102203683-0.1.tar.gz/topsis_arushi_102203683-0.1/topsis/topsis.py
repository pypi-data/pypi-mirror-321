import pandas as pd
import numpy as np
import sys
import os
from typing import List

def verify_inputs(input_file: str, weights: str, impacts: str, result_file: str) -> None:
    """Verify all input parameters and raise appropriate exceptions."""
    # Check if input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' does not exist")
    
    # Read input file
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        raise Exception(f"Error reading input file: {str(e)}")
    
    # Check minimum columns
    if len(df.columns) < 3:
        raise ValueError("Input file must contain three or more columns")
    
    # Check numeric values
    for col in df.columns[1:]:
        if not pd.to_numeric(df[col], errors='coerce').notnull().all():
            raise ValueError(f"Column '{col}' contains non-numeric values")
    
    # Parse weights and impacts
    try:
        weights_list = [float(w) for w in weights.split(',')]
        impacts_list = impacts.split(',')
    except:
        raise ValueError("Error in parsing weights or impacts")
    
    # Check weights and impacts length
    if len(weights_list) != len(df.columns) - 1:
        raise ValueError("Number of weights must match number of criteria columns")
    if len(impacts_list) != len(df.columns) - 1:
        raise ValueError("Number of impacts must match number of criteria columns")
    
    # Validate impacts
    for impact in impacts_list:
        if impact not in ['+', '-']:
            raise ValueError("Impacts must be either '+' or '-'")

def normalize_decision_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize the decision matrix."""
    normalized_df = df.copy()
    
    for col in df.columns[1:]:
        squared_sum = np.sqrt(sum(df[col] ** 2))
        normalized_df[col] = df[col] / squared_sum
    
    return normalized_df

def calculate_topsis(input_file: str, weights: str, impacts: str, result_file: str) -> None:
    """Calculate TOPSIS scores and ranks."""
    # Verify inputs
    verify_inputs(input_file, weights, impacts, result_file)
    
    # Read input file
    df = pd.read_csv(input_file)
    
    # Convert weights to list of floats
    weights_list = [float(w) for w in weights.split(',')]
    impacts_list = impacts.split(',')
    
    # Step 1: Normalize the decision matrix
    normalized_df = normalize_decision_matrix(df.iloc[:, 1:])
    
    # Step 2: Calculate weighted normalized decision matrix
    weighted_normalized = normalized_df * weights_list
    
    # Step 3: Determine ideal best and worst solutions
    ideal_best = []
    ideal_worst = []
    
    for col, impact in zip(weighted_normalized.columns, impacts_list):
        if impact == '+':
            ideal_best.append(weighted_normalized[col].max())
            ideal_worst.append(weighted_normalized[col].min())
        else:
            ideal_best.append(weighted_normalized[col].min())
            ideal_worst.append(weighted_normalized[col].max())
    
    # Step 4: Calculate separation measures
    s_best = np.sqrt(((weighted_normalized - ideal_best) ** 2).sum(axis=1))
    s_worst = np.sqrt(((weighted_normalized - ideal_worst) ** 2).sum(axis=1))
    
    # Step 5: Calculate TOPSIS score
    topsis_score = s_worst / (s_best + s_worst)
    
    # Add score and rank to original dataframe
    result_df = df.copy()
    result_df['Topsis Score'] = topsis_score
    result_df['Rank'] = result_df['Topsis Score'].rank(ascending=False)
    
    # Save results
    result_df.to_csv(result_file, index=False)

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) != 5:
        print("Incorrect number of arguments.")
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        print("Example: python 102203683.py 102203683-data.csv \"1,1,1,2\" \"+,+,-,+\" 102203683-result.csv")
        sys.exit(1)
    
    try:
        calculate_topsis(*sys.argv[1:])
        print(f"Results saved to {sys.argv[4]}")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()