import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):
    data = pd.read_csv(input_file)
    criteria = data.iloc[:, 1:].values
    weights = [float(w) for w in weights.split(',')]
    impacts = impacts.split(',')
    norm_criteria = criteria / np.sqrt((criteria**2).sum(axis=0))
    weighted_criteria = norm_criteria * weights
    ideal_best = np.where(np.array(impacts) == '+', weighted_criteria.max(axis=0), weighted_criteria.min(axis=0))
    ideal_worst = np.where(np.array(impacts) == '+', weighted_criteria.min(axis=0), weighted_criteria.max(axis=0))
    distance_best = np.sqrt(((weighted_criteria - ideal_best)**2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_criteria - ideal_worst)**2).sum(axis=1))
    scores = distance_worst / (distance_best + distance_worst)
    ranks = len(scores) - scores.argsort()
    print(ranks)
    output_data = data.copy()
    output_data['Score'] = scores
    output_data['Rank'] = ranks
    output_data.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Parse CLI arguments
    if len(sys.argv) != 5:
        print("Usage: topsis <input_file> <weights> <impacts> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]
    
    topsis(input_file, weights, impacts, output_file)
