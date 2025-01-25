import sys
import numpy as np
import pandas as pd

def normalize_and_weight(matrix, criteria_weights):
   
    normalized = matrix / np.linalg.norm(matrix, axis=0)
    normalized = np.nan_to_num(normalized)  # Handle NaN values caused by division by zero
    return normalized * criteria_weights

def compute_ideal_values(matrix, criteria_impacts):
   
    ideal_max, ideal_min = [], []
    for idx, impact in enumerate(criteria_impacts):
        if impact == '+':
            ideal_max.append(np.max(matrix[:, idx]))
            ideal_min.append(np.min(matrix[:, idx]))
        elif impact == '-':
            ideal_max.append(np.min(matrix[:, idx]))
            ideal_min.append(np.max(matrix[:, idx]))
    return np.array(ideal_max), np.array(ideal_min)

def calculate_topsis_scores(matrix, criteria_weights, criteria_impacts):
   
    weighted_matrix = normalize_and_weight(matrix, criteria_weights)
    ideal_best, ideal_worst = compute_ideal_values(weighted_matrix, criteria_impacts)
    dist_to_best = np.linalg.norm(weighted_matrix - ideal_best, axis=1)
    dist_to_worst = np.linalg.norm(weighted_matrix - ideal_worst, axis=1)
    return dist_to_worst / (dist_to_best + dist_to_worst)

def validate_inputs(file_data, criteria_weights, criteria_impacts):
    
    
    if file_data.shape[1] < 3:
        raise ValueError("Input file must have at least three columns (ID and at least two criteria).")
    
   
    criteria_matrix = file_data.iloc[:, 1:].values
    if not np.issubdtype(criteria_matrix.dtype, np.number):
        raise ValueError("Criteria columns must contain numeric values.")
    
    
    if len(criteria_weights) != criteria_matrix.shape[1] or len(criteria_impacts) != criteria_matrix.shape[1]:
        raise ValueError("The number of weights and impacts must match the number of criteria.")
    
   
    if not all(impact in ['+', '-'] for impact in criteria_impacts):
        raise ValueError("Impacts must be '+' (beneficial) or '-' (non-beneficial).")
    
    return criteria_matrix

def execute_topsis():
   
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <input_file> <weights> <impacts> <output_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    weight_list = list(map(float, sys.argv[2].split(',')))
    impact_list = sys.argv[3].split(',')
    output_path = sys.argv[4]

    try:
        
        file_data = pd.read_csv(input_path)
        
        
        criteria_matrix = validate_inputs(file_data, weight_list, impact_list)
        
       
        scores = calculate_topsis_scores(criteria_matrix, weight_list, impact_list)
        
        
        file_data['Score'] = scores
        file_data['Rank'] = file_data['Score'].rank(ascending=False).astype(int)
        
        
        file_data.to_csv(output_path, index=False)
        print(f"Results have been successfully saved to '{output_path}'")
    
    except FileNotFoundError:
        print(f"Error: Could not find the file '{input_path}'. Please check the file path.")
    except ValueError as ve:
        print(f"Input Validation Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    execute_topsis()
