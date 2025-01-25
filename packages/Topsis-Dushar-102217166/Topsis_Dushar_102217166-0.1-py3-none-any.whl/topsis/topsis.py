import sys
import os
import pandas as pd
import numpy as np

def run_topsis(input_file, weights, impacts, output_file):
    
    if len(sys.argv) != 5:
        print("Error: Incorrect number of parameters!")
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found!")
        sys.exit(1)

    
    weights_list = weights.split(',')
    try:
        weights_list = [float(w) for w in weights_list]
    except ValueError:
        print("Error: Weights must be numeric and separated by commas.")
        sys.exit(1)

    
    impacts_list = impacts.split(',')
    if not all(impact in ['+', '-'] for impact in impacts_list):
        print("Error: Impacts must be '+' or '-' and separated by commas.")
        sys.exit(1)

    
    try:
        data = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error: Unable to read file '{input_file}'. {e}")
        sys.exit(1)

    
    if data.shape[1] < 3:
        print("Error: Input file must have at least 3 columns.")
        sys.exit(1)

    
    if not all(data.iloc[:, 1:].applymap(lambda x: isinstance(x, (int, float))).all()):
        print("Error: All columns except the first must contain numeric values.")
        sys.exit(1)

    
    normalized_data = data.iloc[:, 1:].apply(lambda col: col / np.sqrt(sum(col**2)), axis=0)

    
    weighted_data = normalized_data * weights_list

    
    pis = []
    nis = []
    for i in range(len(impacts_list)):
        if impacts_list[i] == '+':
            pis.append(weighted_data.iloc[:, i].max())
            nis.append(weighted_data.iloc[:, i].min())
        else:
            pis.append(weighted_data.iloc[:, i].min())
            nis.append(weighted_data.iloc[:, i].max())

    
    s_plus = np.sqrt(((weighted_data - pis) ** 2).sum(axis=1))
    s_minus = np.sqrt(((weighted_data - nis) ** 2).sum(axis=1))
    topsis_score = s_minus / (s_plus + s_minus)

    
    data['Topsis Score'] = topsis_score
    data['Rank'] = topsis_score.rank(ascending=False).astype(int)

    
    data.to_csv(output_file, index=False)
    print(f"Results saved to '{output_file}'.")

