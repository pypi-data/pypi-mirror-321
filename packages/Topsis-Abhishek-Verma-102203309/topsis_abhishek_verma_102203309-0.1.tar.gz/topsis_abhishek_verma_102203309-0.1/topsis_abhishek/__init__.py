import pandas as pd
import numpy as np
import sys

def validate_parameters(file_path, priority_weights, effect_signs):
    try:
        dataset = pd.read_csv(file_path)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    
    if dataset.shape[1] < 3:
        print("Error: File must have at least 3 columns.")
        sys.exit(1)
    
    if not all(dataset.iloc[:, 1:].applymap(np.isreal).all(axis=1)):
        print("Error: All columns except the first must contain numeric values.")
        sys.exit(1)
    
    priority_weights = priority_weights.split(",")
    effect_signs = effect_signs.split(",")
    if len(priority_weights) != (dataset.shape[1] - 1) or len(effect_signs) != (dataset.shape[1] - 1):
        print("Error: Mismatch in the number of weights and impacts.")
        sys.exit(1)
    
    if not all(weight.isdigit() for weight in priority_weights):
        print("Error: Weights must be numeric values.")
        sys.exit(1)
    
    if not all(sign in ['+', '-'] for sign in effect_signs):
        print("Error: Impacts must be '+' or '-'.")
        sys.exit(1)
    
    return dataset, list(map(float, priority_weights)), effect_signs

def process_topsis(file_path, priority_weights, effect_signs, output_file):
    dataset, priority_weights, effect_signs = validate_parameters(file_path, priority_weights, effect_signs)
    decision_matrix = dataset.iloc[:, 1:].values
    normalized_matrix = decision_matrix / np.sqrt((decision_matrix**2).sum(axis=0))
    weighted_matrix = normalized_matrix * priority_weights
    best_ideal = []
    worst_ideal = []
    for index, sign in enumerate(effect_signs):
        if sign == '+':
            best_ideal.append(np.max(weighted_matrix[:, index]))
            worst_ideal.append(np.min(weighted_matrix[:, index]))
        elif sign == '-':
            best_ideal.append(np.min(weighted_matrix[:, index]))
            worst_ideal.append(np.max(weighted_matrix[:, index]))
    distance_best = np.sqrt(((weighted_matrix - best_ideal)**2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_matrix - worst_ideal)**2).sum(axis=1))
    preference_score = distance_worst / (distance_best + distance_worst)
    dataset['Performance Score'] = preference_score
    dataset['Position'] = pd.Series(preference_score).rank(ascending=False)
    dataset.to_csv(output_file, index=False)
    print(f"Output file '{output_file}' created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <script_name.py> <file_path> <weights> <impacts> <output_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    priority_weights = sys.argv[2]
    effect_signs = sys.argv[3]
    output_file = sys.argv[4]
    
    process_topsis(file_path, priority_weights, effect_signs, output_file)
