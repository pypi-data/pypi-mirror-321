import pandas as pd
import numpy as np
import sys

def fateh(input_file, weights, impacts, output_file):
    # Load data
    df = pd.read_csv(input_file)
    
    # Separate object/variable names and numeric data
    object_names = df.iloc[:, 0]  # First column
    data = df.iloc[:, 1:]  # Numeric columns only
    
    # Validate inputs
    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        raise ValueError("Number of weights and impacts must match the number of columns in the data")
    
    # Normalize data
    norm_data = data / np.sqrt((data**2).sum(axis=0))
    
    # Weighted normalized decision matrix
    weights = np.array(weights, dtype=float)
    weighted_data = norm_data * weights
    
    # Calculate ideal best and worst
    impacts = np.array(impacts)
    ideal_best = np.where(impacts == '+', weighted_data.max(axis=0), weighted_data.min(axis=0))
    ideal_worst = np.where(impacts == '+', weighted_data.min(axis=0), weighted_data.max(axis=0))
    
    # Calculate distances
    distance_best = np.sqrt(((weighted_data - ideal_best)**2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_data - ideal_worst)**2).sum(axis=1))
    
    # Calculate TOPSIS scores
    topsis_score = distance_worst / (distance_best + distance_worst)
    
    # Add scores and rankings
    df['Topsis Score'] = topsis_score
    df['Rank'] = topsis_score.rank(ascending=False).astype(int)
    
    # Save results to output file
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

def main():
    if len(sys.argv) != 5:
        print("Usage: fateh <input_file> <weights> <impacts> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    weights = list(map(float, sys.argv[2].split(',')))
    impacts = list(sys.argv[3])
    output_file = sys.argv[4]
    
    fateh(input_file, weights, impacts, output_file)

if __name__ == "__main__":
    main()
