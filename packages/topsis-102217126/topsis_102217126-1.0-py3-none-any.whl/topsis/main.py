import sys
import pandas as pd
import numpy as np
import os

def validate_inputs(input_data, weights, impacts):
    if not os.path.isfile(input_data):
        raise FileNotFoundError(f"Input file not found")
    weights = weights.split(',')
    impacts = impacts.split(',')
    if len(weights) != len(impacts):
        raise ValueError("No. of weights and impacts are unequal")
    for impact in impacts:
        if impact not in ['+', '-']:
            raise ValueError("Impacts must be either '+' or '-'")
    df = pd.read_csv(input_data)
    return df, [float(w) for w in weights], impacts

def topsis(input_data, weights, impacts, outputt):
    try:
        df, weights, impacts = validate_inputs(input_data, weights, impacts)
        params = df.iloc[:, 1:].values
        params01 = params / np.sqrt((params**2).sum(axis=0))
        params02 = params01 * weights
        ideal_b = np.where(np.array(impacts) == '+', params02.max(axis=0), params02.min(axis=0))
        ideal_w = np.where(np.array(impacts) == '+', params02.min(axis=0), params02.max(axis=0))
        dist_b = np.sqrt(((params02 - ideal_b)**2).sum(axis=1))
        dist_w = np.sqrt(((params02 - ideal_w)**2).sum(axis=1))
        scores = dist_w / (dist_b + dist_w)
        resultss = df.copy()
        resultss['Score'] = scores
        resultss['Ranks'] = resultss['Score'].rank(method='min', ascending=False).astype(int)
        resultss.to_csv(outputt, index=False)
    except Exception as e:
        print(e)

def main():
    if len(sys.argv) != 5:
        print("Missing Parameters")
        print("Use: topsis <inputFileName> <Weights> <Impacts> <resultFileName>")
    else:
        topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == "__main__":
    main()