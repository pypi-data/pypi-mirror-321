import sys
import numpy as np
import pandas as pd

def scale_mat(mat, w):
    mat = mat / np.linalg.norm(mat, axis=0)
    mat = np.nan_to_num(mat)
    return mat * w

def ideal_solutions(mat, impacts):
    best, worst = [], []
    for i, imp in enumerate(impacts):
        if imp == '+':
            best.append(np.max(mat[:, i]))
            worst.append(np.min(mat[:, i]))
        else:
            best.append(np.min(mat[:, i]))
            worst.append(np.max(mat[:, i]))
    return np.array(best), np.array(worst)

def topsis(mat, w, impacts):
    mat = scale_mat(mat, w)
    best, worst = ideal_solutions(mat, impacts)
    d_best = np.linalg.norm(mat - best, axis=1)
    d_worst = np.linalg.norm(mat - worst, axis=1)
    return d_worst / (d_best + d_worst)

def run():
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <input_file> <weights> <impacts> <output_file>")
        sys.exit(1)

    in_file = sys.argv[1]
    w = list(map(float, sys.argv[2].split(',')))
    impacts = sys.argv[3].split(',')
    out_file = sys.argv[4]

    try:
        data = pd.read_csv(in_file)

        if data.shape[1] < 3:
            raise ValueError("Input file must have at least three columns.")

        mat = data.iloc[:, 1:].values
        if not np.issubdtype(mat.dtype, np.number):
            raise ValueError("Criteria columns must contain numeric values.")

        if len(w) != mat.shape[1] or len(impacts) != mat.shape[1]:
            raise ValueError("Weights and impacts must match the number of criteria.")

        if not all(imp in ['+', '-'] for imp in impacts):
            raise ValueError("Impacts must be either '+' or '-'.")
        
        scores = topsis(mat, w, impacts)
        data['Score'] = scores
        data['Rank'] = data['Score'].rank(ascending=False).astype(int)

        data.to_csv(out_file, index=False)
        print(f"Results saved to {out_file}")

    except FileNotFoundError:
        print(f"Error: The file '{in_file}' was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()
