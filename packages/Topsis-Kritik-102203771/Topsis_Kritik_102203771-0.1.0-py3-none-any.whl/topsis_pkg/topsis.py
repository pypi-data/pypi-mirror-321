import pandas as pd
import numpy as np
from pathlib import Path
import sys

def topsis(input_file, weights, impacts, result_file):
    """
    Calculate TOPSIS score and rank for given dataset
    
    Parameters:
    input_file (str): Path to input CSV file
    weights (str): Comma separated string of weights
    impacts (str): Comma separated string of impacts ('+' or '-')
    result_file (str): Path to save results CSV file
    """
    try:
        # Input validations
        if not Path(input_file).exists():
            raise FileNotFoundError(f"Input file '{input_file}' does not exist")
        
        # Read input file
        df = pd.read_csv(input_file)
        
        if len(df.columns) < 3:
            raise ValueError("Input file must contain three or more columns")
            
        # Convert weights and impacts to lists
        try:
            weights = [float(w.strip()) for w in weights.split(',')]
        except ValueError:
            raise ValueError("Weights must be numeric values separated by commas")
            
        impacts = [i.strip() for i in impacts.split(',')]
        
        # Validate weights and impacts
        if len(weights) != len(impacts):
            raise ValueError("Number of weights and impacts must be equal")
            
        if len(weights) != len(df.columns) - 1:
            raise ValueError("Number of weights/impacts must match number of criteria columns")
            
        if not all(impact in ['+', '-'] for impact in impacts):
            raise ValueError("Impacts must be either '+' or '-'")
            
        # Extract criteria columns (excluding first column)
        criteria_df = df.iloc[:, 1:]
        
        # Check if all values are numeric
        if not criteria_df.applymap(np.isreal).all().all():
            raise ValueError("All criteria values must be numeric")
            
        # Step 1: Normalize the decision matrix
        normalized_df = criteria_df.copy()
        for col in normalized_df.columns:
            normalized_df[col] = normalized_df[col] / np.sqrt((normalized_df[col]**2).sum())
            
        # Step 2: Calculate weighted normalized decision matrix
        weighted_df = normalized_df.copy()
        for col, weight in zip(weighted_df.columns, weights):
            weighted_df[col] = weighted_df[col] * weight
            
        # Step 3: Determine ideal best and worst values
        ideal_best = []
        ideal_worst = []
        
        for col, impact in zip(weighted_df.columns, impacts):
            if impact == '+':
                ideal_best.append(weighted_df[col].max())
                ideal_worst.append(weighted_df[col].min())
            else:
                ideal_best.append(weighted_df[col].min())
                ideal_worst.append(weighted_df[col].max())
                
        # Step 4: Calculate separation measures
        s_best = np.sqrt(((weighted_df - ideal_best)**2).sum(axis=1))
        s_worst = np.sqrt(((weighted_df - ideal_worst)**2).sum(axis=1))
        
        # Step 5: Calculate TOPSIS score
        topsis_score = s_worst / (s_best + s_worst)
        
        # Add score and rank to original dataframe
        df['Topsis Score'] = topsis_score
        df['Rank'] = df['Topsis Score'].rank(ascending=False)
        
        # Save results
        df.to_csv(result_file, index=False)
        print(f"Results saved successfully to {result_file}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

def main():
    """Command line interface for TOPSIS calculation"""
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result_file = sys.argv[4]
    
    topsis(input_file, weights, impacts, result_file)

if __name__ == "__main__":
    main()