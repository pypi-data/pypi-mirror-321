import pandas as pd
import numpy as np
import os
import sys

def topsis(input_file, weights, impacts, output_file):
    """
    Calculate TOPSIS scores and ranks for given dataset.
    
    Parameters:
    -----------
    input_file : str
        Path to input CSV file containing the decision matrix
    weights : str
        Comma separated string of weights (e.g. "1,1,1,2")
    impacts : str
        Comma separated string of impacts (e.g. "+,+,-,+")
    output_file : str
        Path where the result CSV will be saved
        
    Returns:
    --------
    None
        Saves the result to specified output file
        
    Raises:
    -------
    Exception
        If there are any validation or calculation errors
    """
    try:
        # Validation checks
        if not os.path.exists(input_file):
            raise Exception(f"Input file '{input_file}' does not exist")
            
        # Read input file
        df = pd.read_csv(input_file)
        
        if len(df.columns) < 3:
            raise Exception("Input file must contain three or more columns")
            
        # Convert weights to list of floats
        weight_list = [float(w) for w in weights.split(',')]
        impact_list = impacts.split(',')
        
        # Validate weights and impacts
        if len(weight_list) != len(df.columns) - 1:
            raise Exception("Number of weights must match number of criteria columns")
            
        if len(impact_list) != len(df.columns) - 1:
            raise Exception("Number of impacts must match number of criteria columns")
            
        if not all(x in ['+', '-'] for x in impact_list):
            raise Exception("Impacts must be either + or -")
            
        # Extract numeric columns
        decision_matrix = df.iloc[:, 1:].values.astype(float)
        
        # Normalize the decision matrix
        normalized_matrix = decision_matrix / np.sqrt(np.sum(decision_matrix**2, axis=0))
        
        # Calculate weighted normalized matrix
        weighted_matrix = normalized_matrix * weight_list
        
        # Find ideal best and worst values
        ideal_best = []
        ideal_worst = []
        
        for idx, impact in enumerate(impact_list):
            if impact == '+':
                ideal_best.append(max(weighted_matrix[:, idx]))
                ideal_worst.append(min(weighted_matrix[:, idx]))
            else:
                ideal_best.append(min(weighted_matrix[:, idx]))
                ideal_worst.append(max(weighted_matrix[:, idx]))
                
        # Calculate separation measures
        s_positive = np.sqrt(np.sum((weighted_matrix - ideal_best)**2, axis=1))
        s_negative = np.sqrt(np.sum((weighted_matrix - ideal_worst)**2, axis=1))
        
        # Calculate performance score
        performance = s_negative / (s_positive + s_negative)
        
        # Add results to dataframe
        df['Topsis Score'] = performance
        df['Rank'] = df['Topsis Score'].rank(ascending=False)
        
        # Save results
        df.to_csv(output_file, index=False)
        
    except Exception as e:
        raise Exception(str(e))