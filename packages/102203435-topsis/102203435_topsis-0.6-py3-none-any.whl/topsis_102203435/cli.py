import argparse
import pandas as pd
import numpy as np
from topsis_102383046.topsis import Topsis  # Import your TOPSIS class

def main():
    parser = argparse.ArgumentParser(
        description="Run TOPSIS analysis from the command line."
    )
    
    parser.add_argument(
        "input_file", 
        type=str, 
        help="Path to the input CSV file containing the decision matrix."
    )
    parser.add_argument(
        "weights", 
        type=str, 
        help="Comma-separated weights for the criteria (e.g., '0.2,0.3,0.5')."
    )
    parser.add_argument(
        "impacts", 
        type=str, 
        help="Comma-separated impacts for the criteria ('+/-' e.g., '+,+,-')."
    )
    parser.add_argument(
        "output_file", 
        type=str, 
        help="Path to the output CSV file to save the rankings."
    )

    args = parser.parse_args()

    try:
    
        df = pd.read_csv(args.input_file)
        matrix = df.iloc[:, 1:].values  

        weights = list(map(float, args.weights.split(',')))
        impacts = args.impacts.split(',')
        

        if len(weights) != matrix.shape[1] or len(impacts) != matrix.shape[1]:
            raise ValueError("Number of weights and impacts must match the number of criteria.")

        
        if not all(impact in ['+', '-'] for impact in impacts):
            raise ValueError("Impacts must be '+' or '-'.")

    
        topsis = Topsis(matrix, weights, impacts)
        scores = topsis.calculate()

        
        df['Score'] = scores
        df['Rank'] = scores.argsort()[::-1] + 1

        
        df.to_csv(args.output_file, index=False)
        print(f"TOPSIS results successfully saved to {args.output_file}")

    except Exception as e:
        print(f"Error: {e}")
