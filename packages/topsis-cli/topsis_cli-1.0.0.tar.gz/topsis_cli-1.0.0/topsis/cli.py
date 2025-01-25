import argparse
import pandas as pd
import numpy as np
from topsis.topsis import calculate_topsis

def main():
    parser = argparse.ArgumentParser(description="TOPSIS CLI tool")
    parser.add_argument("input_file", help="Path to input CSV file")
    parser.add_argument("weights", help="Comma-separated weights for criteria")
    parser.add_argument("impacts", help="Comma-separated impacts (+/-)")
    parser.add_argument("output_file", help="Path to save output CSV file")

    args = parser.parse_args()

    # Load input data
    data = pd.read_csv(args.input_file)
    weights = np.array([float(w) for w in args.weights.split(",")])
    impacts = [1 if i == "+" else -1 for i in args.impacts.split(",")]

    # Validate data
    if data.shape[1] < 3:
        raise ValueError("Input file must have at least 3 columns: 'Name', 'Criteria1', ...")

    # Extract criteria data
    scores = calculate_topsis(data.iloc[:, 1:].values, weights, impacts)
    data["Score"] = scores
    data["Rank"] = data["Score"].rank(ascending=False)

    # Save output
    data.to_csv(args.output_file, index=False)
    print(f"Results saved to {args.output_file}")

if __name__ == "__main__":
    main()
