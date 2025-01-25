import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):

    data = pd.read_csv(input_file)

    if data.shape[1] < 3:
        raise ValueError("Input file must have at least 3 columns.")
    
    for col in data.columns[1:]:
        if not np.issubdtype(data[col].dtype, np.number):
            raise ValueError("Column must contain numeric values.")
    
    weights = [float(w) for w in weights.split(",")]
    # print("Weights : ", weights)
    impacts = impacts.split(",")
    # print("Impacts : ", impacts)
    
    if len(weights) != len(impacts) or len(weights) != data.shape[1] - 1:
        raise ValueError("Error: The number of weights, impacts, and criteria must match.")
    
    for impact in impacts:
        if impact not in ['+', '-']:
            raise ValueError("Error: Impacts must be '+' or '-' only.")
    
    numeric_data = data.iloc[:, 1:]
    # print(numeric_data)
    normalized = numeric_data / np.sqrt((numeric_data ** 2).sum())
    
    weighted = normalized * weights
    
    # Calculations
    ideal_best = []
    ideal_worst = []

    for i, impact in enumerate(impacts):
        if impact == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())
    
    # Distances
    distances_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    distances_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))
    
    # TOPSIS score
    scores = distances_worst / (distances_best + distances_worst)
    data['Topsis Score'] = scores
    data['Rank'] = scores.rank(ascending=False).astype(int)
    
    # Save
    data.to_csv(output_file, index=False)
    print(f"Result saved to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <script> <input_file> <weights> <impacts> <output_file>")
    else:
        _, input_file, weights, impacts, output_file = sys.argv
        topsis(input_file, weights, impacts, output_file)