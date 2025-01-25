import pandas as pd
import numpy as np
import sys

def topsis(input_file, weights, impacts, output_file):
    try:
        # Read input file
        data = pd.read_csv(input_file)
        
        # Check if the file has at least 3 columns
        if data.shape[1] < 3:
            raise ValueError("Input file must contain at least 3 columns.")

        # Separate the decision matrix and criteria names
        decision_matrix = data.iloc[:, 1:].values
        criteria = data.columns[1:]
        objects = data.iloc[:, 0]

        # Convert weights and impacts to lists
        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')

        # Validate weights and impacts
        if len(weights) != len(criteria):
            raise ValueError("Number of weights must match the number of criteria.")
        if len(impacts) != len(criteria):
            raise ValueError("Number of impacts must match the number of criteria.")
        if not all(i in ['+', '-'] for i in impacts):
            raise ValueError("Impacts must be '+' or '-'.")

        # Normalize the decision matrix
        norm_matrix = decision_matrix / np.sqrt((decision_matrix**2).sum(axis=0))

        # Weighted normalized matrix
        weighted_matrix = norm_matrix * weights

        # Determine ideal best and ideal worst
        ideal_best = np.max(weighted_matrix, axis=0) * (np.array(impacts) == '+') + \
                     np.min(weighted_matrix, axis=0) * (np.array(impacts) == '-')
        ideal_worst = np.min(weighted_matrix, axis=0) * (np.array(impacts) == '+') + \
                      np.max(weighted_matrix, axis=0) * (np.array(impacts) == '-')

        # Calculate distances to ideal best and worst
        dist_to_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
        dist_to_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

        # Calculate TOPSIS score
        topsis_score = dist_to_worst / (dist_to_best + dist_to_worst)

        # Add scores and ranks to the data
        data['Topsis Score'] = topsis_score
        data['Rank'] = pd.Series(topsis_score).rank(ascending=False, method='min').astype(int)

        # Save results to output file
        data.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <RollNumber>.py <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        print("Example: python 101556.py 101556-data.csv '1,1,1,2' '+,+,-,+' 101556-result.csv")
    else:
        _, input_file, weights, impacts, output_file = sys.argv
        topsis(input_file, weights, impacts, output_file)

