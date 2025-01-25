import sys
import pandas as pd
import numpy as np
import os

def validate_inputs(input_file, weights, impacts):
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"input file not found")
    weights = weights.split(',')
    impacts = impacts.split(',')
    if len(weights) != len(impacts):
        raise ValueError("No. of weights and impacts are unequal")
    for impact in impacts:
        if impact not in ['+', '-']:
            raise ValueError("Impacts must be either '+' or '-'")
    df = pd.read_csv(input_file)
    return df, [float(w) for w in weights], impacts

def topsis(input_file, weights, impacts, output_file):
    try:
        df, weights, impacts = validate_inputs(input_file, weights, impacts)
        params = df.iloc[:, 1:].values
        norm_params = params / np.sqrt((params**2).sum(axis=0))
        weight_params = norm_params * weights
        ideal_b = np.where(np.array(impacts) == '+', weight_params.max(axis=0), weight_params.min(axis=0))
        ideal_w = np.where(np.array(impacts) == '+', weight_params.min(axis=0), weight_params.max(axis=0))
        distance_b = np.sqrt(((weight_params - ideal_b)**2).sum(axis=1))
        distance_w = np.sqrt(((weight_params - ideal_w)**2).sum(axis=1))
        scores = distance_w / (distance_b + distance_w)
        ranks = len(scores) - scores.argsort()
        output_df = df.copy()
        output_df['Score'] = scores
        output_df['Rank'] = ranks
        output_df.to_csv(output_file, index=False)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Missing Parameters")
        print("Use: python <fileName> <inputFileName> <Weights> <Impacts> <resultFileName>")
    else:
        topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
