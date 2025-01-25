
import pandas as pd
import sys
import os
from topsis import topsis

def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = list(map(float, sys.argv[2].split(',')))
    impacts = sys.argv[3].split(',')
    result_file = sys.argv[4]

    # Step 2: Read the input file
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        sys.exit(1)

    # Check if input file has at least 3 columns
    if data.shape[1] < 3:
        print("The input file must contain at least 3 columns.")
        sys.exit(1)

    # Step 3: Run TOPSIS
    scores, rank = topsis(data.iloc[:, 1:].values, weights, impacts)

    # Step 4: Prepare result
    result = data.copy()
    result['Topsis Score'] = scores
    result['Rank'] = rank

    # Step 5: Save result
    result.to_csv(result_file, index=False)
    print(f"Result saved to {result_file}")

if __name__ == "__main__":
    main()
