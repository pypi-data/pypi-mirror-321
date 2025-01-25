import sys
import pandas as pd
import numpy as np

def check_inputs(args):
    if len(args) != 5:
        print("Error: Required parameters missing")
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file, weights, impacts, result_file = args[1:]

    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)

    if len(df.columns) < 3:
        print("Error: Input file must contain three or more columns")
        sys.exit(1)

    try:
        numeric_data = df.iloc[:, 1:].astype(float)
        if numeric_data.isna().any().any():
            print("Error: Non-numeric values found in data columns")
            sys.exit(1)
    except ValueError:
        print("Error: All columns from second onwards must contain numeric values only")
        sys.exit(1)

    weights = weights.split(',')
    weights = [float(w) for w in weights]
    impacts = impacts.split(',')

    if len(weights) != len(df.columns[1:]) or len(impacts) != len(df.columns[1:]):
        print("Error: Number of weights, impacts and columns must be same")
        sys.exit(1)

    if not all(x in ['+', '-'] for x in impacts):
        print("Error: Impacts must be either +ve or -ve")
        sys.exit(1)

    return df, weights, impacts, result_file

def topsis(df, weights, impacts):

    data = df.iloc[:, 1:].values.astype(float)

    normalized = data / np.sqrt(np.sum(data**2, axis=0))

    weights = np.array(weights).astype(float)
    weighted_normalized = normalized * weights

    impacts = np.array(impacts)
    ideal_best = np.where(impacts == '+', np.max(weighted_normalized, axis=0),
                         np.min(weighted_normalized, axis=0))
    ideal_worst = np.where(impacts == '+', np.min(weighted_normalized, axis=0),
                          np.max(weighted_normalized, axis=0))

    s_plus = np.sqrt(np.sum((weighted_normalized - ideal_best)**2, axis=1))
    s_minus = np.sqrt(np.sum((weighted_normalized - ideal_worst)**2, axis=1))

    performance = s_minus / (s_plus + s_minus)

    return performance


def main():
    if len(sys.argv) != 5:
        print("Error: Invalid number of arguments")
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        return

    df, weights, impacts, result_file = check_inputs(sys.argv)

    performance = topsis(df, weights, impacts)

    df['Topsis Score'] = performance
    df['Rank'] = df['Topsis Score'].rank(ascending=False).astype(int)

    df.to_csv(result_file, index=False)
    print(f"Results saved to {result_file}")

if __name__ == "__main__":
    main()