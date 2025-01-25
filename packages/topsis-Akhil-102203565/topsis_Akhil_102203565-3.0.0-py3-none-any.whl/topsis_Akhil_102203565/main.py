import numpy as np
import pandas as pd
import argparse
import sys

def topsis(data_file, weights, impacts, result_file):
    try:
        # Read CSV File
        df = pd.read_csv(data_file)

        # Validate input file
        if df.shape[1] < 3:
            raise ValueError("Input file must contain at least three columns.")
        
        if not df.iloc[:, 1:].applymap(lambda x: isinstance(x, (int, float))).all().all():
            raise ValueError("All columns except the first must contain numeric values.")

        # Convert weights and impacts
        weights = list(map(float, weights.split(",")))
        impacts = impacts.split(",")

        if len(weights) != len(impacts) or len(weights) != df.shape[1] - 1:
            raise ValueError("Number of weights, impacts, and criteria columns must be the same.")

        if any(i not in ["+", "-"] for i in impacts):
            raise ValueError("Impacts must be either '+' or '-'.")

        # Normalize the data
        data = df.iloc[:, 1:].values
        norm_data = data / np.sqrt((data ** 2).sum(axis=0))

        # Multiply with weights
        weighted_data = norm_data * weights

        # Find ideal best and worst
        ideal_best = np.where(np.array(impacts) == "+", weighted_data.max(axis=0), weighted_data.min(axis=0))
        ideal_worst = np.where(np.array(impacts) == "+", weighted_data.min(axis=0), weighted_data.max(axis=0))

        # Calculate distances
        dist_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
        dist_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

        # Compute TOPSIS Score
        topsis_score = dist_worst / (dist_best + dist_worst)

        # Rank alternatives
        df["Topsis Score"] = topsis_score
        df["Rank"] = topsis_score.argsort()[::-1] + 1

        # Save result as Excel file
        df.to_excel(result_file, index=False)
        print(f"Results saved to {result_file}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="TOPSIS implementation in Python")
    parser.add_argument("data_file", help="Path to input CSV file")
    parser.add_argument("weights", help="Comma-separated list of weights")
    parser.add_argument("impacts", help="Comma-separated list of impacts")
    parser.add_argument("result_file", help="Path to save the results (Excel file)")
    args = parser.parse_args()

    topsis(args.data_file, args.weights, args.impacts, args.result_file)

if __name__ == "__main__":
    main()
