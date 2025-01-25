import pandas as pd
import numpy as np
import sys
import os
from sklearn.preprocessing import LabelEncoder

def read_data(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    data = pd.read_csv(file_path, header=0, index_col=0)
    if data.shape[1] < 3:
        print("Error: Input file must contain at least three columns.")
        sys.exit(1)

    return data

def topsis(data, wts, imps):
    n = data.shape[1]
    if len(wts) != n:
        print(f"Error: The number of weights ({len(wts)}) must match the number of numerical columns ({n}).")
        sys.exit(1)
    if len(imps) != n:
        print(f"Error: The number of impacts ({len(imps)}) must match the number of numerical columns ({n}).")
        sys.exit(1)
    if not all(i in ['+', '-'] for i in imps):
        print("Error: Impacts must be '+' or '-'.")
        sys.exit(1)

    rss = np.sqrt((data**2).sum(axis=0))
    norm_data = data / rss
    wtd_data = norm_data * wts

    ideal_sol = []
    neg_sol = []
    for i, col in enumerate(wtd_data.columns):
        if imps[i] == '+':
            ideal_sol.append(wtd_data[col].max())
            neg_sol.append(wtd_data[col].min())
        else:
            ideal_sol.append(wtd_data[col].min())
            neg_sol.append(wtd_data[col].max())

    ideal_sol = np.array(ideal_sol)
    neg_sol = np.array(neg_sol)

    d_ideal = np.sqrt(((wtd_data - ideal_sol)**2).sum(axis=1))
    d_neg_ideal = np.sqrt(((wtd_data - neg_sol)**2).sum(axis=1))
    score = d_neg_ideal / (d_ideal + d_neg_ideal)

    sort_index = np.argsort(score)[::-1]
    rank = np.zeros_like(sort_index)
    rank[sort_index] = np.arange(1, len(score) + 1)
    data['Topsis-Score'] = score
    data['Rank'] = rank

    return data.sort_values(by='Rank')

def main():
    if len(sys.argv) != 5:
        print("Usage: python 102216114.py <InputDataFilePath> <weights> <impacts> <ResultFilePath>")
        sys.exit(1)
    inp_file = sys.argv[1]
    wts_input = sys.argv[2]
    imps_input = sys.argv[3]
    output = sys.argv[4]
    wts = list(map(float, wts_input.split(',')))
    imps = imps_input.split(',')

    data = read_data(inp_file)
    result = topsis(data, wts, imps)
    result.to_csv(output)
    print(f"Results saved to: {output}")

if __name__ == "__main__":
    main()
