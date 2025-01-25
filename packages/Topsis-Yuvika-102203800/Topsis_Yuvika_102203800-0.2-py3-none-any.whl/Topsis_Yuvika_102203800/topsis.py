import sys
import pandas as pd
import numpy as np

def topsis(input, weights, impacts,output):
    try:
        data= pd.read_csv(input)
    except FileNotFoundError:
        print(f"Error: File '{input}' not found.")
        sys.exit(1)
    if len(data.columns) < 3:
        print("Error: Input file must have at least 3 columns.")
        sys.exit(1)
    for dtype in data.dtypes[1:]:  
        if not np.issubdtype(dtype, np.number):
            raise ValueError("All values from the 2nd to last column must be numeric.")

    weights= list(map(float, weights.split(',')))
    impacts= impacts.split(',')
    if len(weights) != len(data.columns) - 1 or len(weights)!=len(impacts):
        print("Error: Number of weights and impacts must match the number of criteria columns.")
        sys.exit(1)

    if not all(i in ['-', '+'] for i in impacts):
        print("Error: Impacts must be '-' or '+'.")
        sys.exit(1)


    mat = data.iloc[:, 1:].values
    norm_mat = mat/ np.sqrt((mat**2).sum(axis=0))
    weighted_mat = norm_mat * weights

    best = np.where(np.array(impacts)== '+', weighted_mat.max(axis=0), weighted_mat.min(axis=0))
    worst = np.where(np.array(impacts)== '+', weighted_mat.min(axis=0), weighted_mat.max(axis=0))

    best_dis = np.sqrt(((weighted_mat -best)**2).sum(axis=1))
    worst_dis = np.sqrt(((weighted_mat-worst)**2).sum(axis=1))
    score = worst_dis / (worst_dis+best_dis)
    data['Topsis Score'] = score
    data['Rank'] = pd.Series(score).rank(ascending=False).astype(int)
    
    data.to_csv(output, index=False)
    print(f"Results saved to '{output}'.")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
    else:
        _, input_file, weights, impacts, output = sys.argv
        topsis(input_file, weights, impacts, output)
