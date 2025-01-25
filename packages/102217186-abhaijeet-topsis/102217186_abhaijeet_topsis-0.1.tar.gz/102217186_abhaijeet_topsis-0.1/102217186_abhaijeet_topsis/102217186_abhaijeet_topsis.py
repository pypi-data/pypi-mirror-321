import pandas as pd
import numpy as np
import argparse

def topsis(input_file, weights, impacts, output_file):
    # Load data
    df = pd.read_csv(input_file)
    
    # Separate object/variable names and numeric data
    object_names = df.iloc[:, 0]  # First column
    data = df.iloc[:, 1:]  # Numeric columns only
    
    # Check if weights and impacts match the number of columns
    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        raise ValueError("Number of weights and impacts must match the number of columns")
    
    # Normalize data
    norm_data = data / np.sqrt((data**2).sum(axis=0))
    
    # Weighted normalized decision matrix
    weighted_data = norm_data * weights
    
    # Calculate ideal best and worst
    ideal_best = np.where(np.array(impacts) == '+', weighted_data.max(axis=0), weighted_data.min(axis=0))
    ideal_worst = np.where(np.array(impacts) == '+', weighted_data.min(axis=0), weighted_data.max(axis=0))
    
    # Calculate distances from ideal best and worst
    distance_best = np.sqrt(((weighted_data - ideal_best)**2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_data - ideal_worst)**2).sum(axis=1))
    
    # Calculate TOPSIS score
    topsis_score = distance_worst / (distance_best + distance_worst)
    
    # Add scores and ranks to the DataFrame
    df['Topsis Score'] = topsis_score
    df['Rank'] = topsis_score.rank(ascending=False).astype(int)
    
    # Save to output file
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="TOPSIS: A method for multi-criteria decision making.")
    parser.add_argument("input_file", type=str, help="Path to the input CSV file")
    parser.add_argument("weights", type=str, help="Comma-separated weights for the criteria")
    parser.add_argument("impacts", type=str, help="Comma-separated impacts for the criteria (e.g., '+,-,+,-')")
    parser.add_argument("output_file", type=str, help="Path to the output CSV file")

    args = parser.parse_args()

    weights = [float(w) for w in args.weights.split(",")]
    impacts = args.impacts.split(",")

    topsis(args.input_file, weights, impacts, args.output_file)

if __name__ == "__main__":
    main()
