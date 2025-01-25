import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts):
    try:
        data = pd.read_csv(input_file, encoding='ISO-8859-1')

        if data.shape[1] < 3:
            raise ValueError("Input file must have at least 3 columns.")

        # Process weights and impacts
        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')

        if len(weights) != len(impacts) or len(weights) != data.shape[1] - 1:
            raise ValueError("Number of weights and impacts must match the number of criteria.")
        
        if not all(impact in ['+', '-'] for impact in impacts):
            raise ValueError("Impacts must be '+' or '-'.")
        
        # Implement the rest of your TOPSIS code...

        print("TOPSIS Scores and Ranks:")
        for index, row in data.iterrows():
            print(f"Object: {row[0]}, Topsis Score: {row['Topsis Score']}, Rank: {row['Rank']}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")
