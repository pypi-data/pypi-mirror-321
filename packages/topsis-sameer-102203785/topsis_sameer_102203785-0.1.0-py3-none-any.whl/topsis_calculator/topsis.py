import sys
import pandas as pd
import numpy as np
def validate_inputs(weights, impacts, num_data):
    try:
        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')
    except ValueError: 
        print("!!  Weights must be numeric and separated by commas.")
        sys.exit(1)
    
    if len(weights) != num_data or len(impacts) != num_data:
        print("!!  The number of weights, impacts, and criteria columns must be the same.")
        sys.exit(1)
    
    if not all(i in ['+', '-'] for i in impacts):
        print("!!  Impacts must be either '+' or '-'.")
        sys.exit(1)
    
    return weights, impacts

def topsis(input_file, weights, impacts, output_file):
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError: 
        print("!!  Input file not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Can't read the file: {e}")
        sys.exit(1)
    
    if df.shape[1] < 3:
        print("!!  Input file must have at least three columns.")
        sys.exit(1)
    
    try:
        data = df.iloc[:, 1:].astype(float)
    except ValueError: 
        print("!!  All columns except the first one must contain numeric values.")
        sys.exit(1)
    
    num_data = data.shape[1]
    weights, impacts = validate_inputs(weights, impacts, num_data)
    
    # Step 1: Normalize the decision matrix
    normalized_data = data / np.sqrt((data ** 2).sum())
    
    # Step 2: Multiply by weights
    normalized_data *= weights
    
    # Step 3: Determine ideal best and ideal worst
    ideal_best = np.where(np.array(impacts) == '+', normalized_data.max(), normalized_data.min())
    ideal_worst = np.where(np.array(impacts) == '+', normalized_data.min(), normalized_data.max())
    
    # Step 4: Compute distances to ideal best and ideal worst
    dist_best = np.sqrt(((normalized_data - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((normalized_data - ideal_worst) ** 2).sum(axis=1))
    
    # Step 5: Compute Topsis Score
    topsis_score = dist_worst / (dist_best + dist_worst)
    
    # Step 6: Rank alternatives
    df['Topsis Score'] = topsis_score
    df['Rank'] = df['Topsis Score'].rank(method='max', ascending=False).astype(int)
    
    df.to_csv(output_file, index=False)
    print("TOPSIS Score and Rank generated at the directory",output_file)

    
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Format : python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)
    
    _, input_file, weights, impacts, output_file = sys.argv
    print(_,input_file, weights, impacts, output_file)
    topsis(input_file, weights, impacts, output_file)