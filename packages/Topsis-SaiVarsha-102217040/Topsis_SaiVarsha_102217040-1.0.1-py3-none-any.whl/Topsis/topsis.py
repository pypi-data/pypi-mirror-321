import pandas as pd
import numpy as np
import sys

def topsis(input_file, weights, impacts, result_file):
    try:
        # Step 1: Read the input file
        data = pd.read_csv(input_file)
        
        # Check for minimum required columns
        if data.shape[1] < 3:
            raise ValueError("Input file must have at least 3 columns.")
        
        # Extract criteria matrix and validate numeric columns
        criteria = data.iloc[:, 1:].values
        if not np.issubdtype(criteria.dtype, np.number):
            raise ValueError("From the 2nd to last columns, all values must be numeric.")
        
        # Step 2: Normalize the decision matrix
        norm_matrix = criteria / np.sqrt((criteria**2).sum(axis=0))
        
        # Step 3: Apply weights
        weights = [float(w) for w in weights.split(",")]
        if len(weights) != norm_matrix.shape[1]:
            raise ValueError("Number of weights must match the number of criteria columns.")
        weighted_matrix = norm_matrix * weights
        
        # Step 4: Identify positive and negative ideal solutions
        impacts = impacts.split(",")
        if len(impacts) != norm_matrix.shape[1] or not all(i in ['+', '-'] for i in impacts):
            raise ValueError("Impacts must be '+' or '-' for each criterion.")
        
        pis = [max(weighted_matrix[:, i]) if impacts[i] == '+' else min(weighted_matrix[:, i]) for i in range(len(impacts))]
        nis = [min(weighted_matrix[:, i]) if impacts[i] == '+' else max(weighted_matrix[:, i]) for i in range(len(impacts))]
        
        # Step 5: Calculate distances and scores
        dist_pis = np.sqrt(((weighted_matrix - pis)**2).sum(axis=1))
        dist_nis = np.sqrt(((weighted_matrix - nis)**2).sum(axis=1))
        scores = dist_nis / (dist_pis + dist_nis)
        
        # Step 6: Add scores and ranks to the dataframe
        data['Topsis Score'] = scores
        data['Rank'] = scores.argsort()[::-1] + 1
        
        # Step 7: Save to result file
        data.to_csv(result_file, index=False)
        print(f"Results saved to {result_file}")
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
    else:
        _, input_file, weights, impacts, result_file = sys.argv
        topsis(input_file, weights, impacts, result_file)
