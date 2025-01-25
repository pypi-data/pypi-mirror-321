import os
import sys
import pandas as pd
import numpy as np

def read_and_validate_file(file_path):
    """Validate and read the input CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: Can't find the file {file_path}")
    
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError("Error: Please make sure your input file is a valid CSV file")
    
    if len(data.columns) < 3:
        raise ValueError("Error: Input file must have 3 or more columns")
        
    for col in data.columns[1:]:
        try:
            pd.to_numeric(data[col])
        except:
            raise ValueError(f"Error: Column {col} has non-numeric values")
            
    return data

def process_weights_impacts(weights_str, impacts_str, num_columns):
    """Process and validate weights and impacts strings."""
    try:
        weights = [float(w) for w in weights_str.split(',')]
    except:
        raise ValueError("Error: Weights should be numbers separated by commas")
        
    impacts = impacts_str.split(',')
    if not all(imp in ['+', '-'] for imp in impacts):
        raise ValueError("Error: Impacts should be either + or - separated by commas")
        
    impact_values = [1 if imp == '+' else -1 for imp in impacts]
    
    if not (len(weights) == len(impact_values) == num_columns - 1):
        raise ValueError("Error: Number of weights and impacts should match number of columns (excluding first column)")
        
    return weights, impact_values

def calculate_topsis(data, weights, impacts):
    """Calculate TOPSIS scores and ranks."""
    numbers = data.iloc[:, 1:].values
    
    normalized = numbers / np.sqrt(np.sum(numbers ** 2, axis=0))
    weighted = normalized * weights
    
    best = weighted.max(axis=0) * impacts
    worst = weighted.min(axis=0) * impacts
    
    dist_best = np.sqrt(np.sum((weighted - best) ** 2, axis=1))
    dist_worst = np.sqrt(np.sum((weighted - worst) ** 2, axis=1))
    
    scores = dist_worst / (dist_best + dist_worst)
    ranks = len(scores) - np.argsort(np.argsort(scores))
    
    return scores, ranks

def topsis(input_file, weights, impacts, result_file):
    """Main TOPSIS function that processes input and generates results."""
    # Read and check the data
    data = read_and_validate_file(input_file)
    
    # Process weights and impacts
    weight_values, impact_values = process_weights_impacts(weights, impacts, len(data.columns))
    
    # Calculate TOPSIS
    scores, ranks = calculate_topsis(data, weight_values, impact_values)
    
    # Add results to the data
    data['Topsis Score'] = scores
    data['Rank'] = ranks
    
    # Save the results
    try:
        data.to_csv(result_file, index=False)
    except Exception as e:
        raise IOError(f"Error: Couldn't save to {result_file}")
    
    return data
