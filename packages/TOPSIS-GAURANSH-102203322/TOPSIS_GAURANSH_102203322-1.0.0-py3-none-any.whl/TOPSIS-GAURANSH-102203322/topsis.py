import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, result_file):
    try:
        # Load the input file
        data = pd.read_csv(input_file)
        
        # Validation checks
        if data.shape[1] < 3:
            raise Exception("Input file must contain at least three columns.")
        if not np.issubdtype(data.iloc[:, 1:].dtypes.values[0], np.number):
            raise Exception("From 2nd to last columns, all values must be numeric.")

        # Extract weights and impacts
        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')
        if len(weights) != len(impacts) or len(weights) != data.shape[1] - 1:
            raise Exception("Number of weights, impacts, and numeric columns must match.")
        if not all(i in ['+', '-'] for i in impacts):
            raise Exception("Impacts must be either '+' or '-'.")

        # Normalize the data
        numeric_data = data.iloc[:, 1:].values
        norm_data = numeric_data / np.sqrt((numeric_data**2).sum(axis=0))

        # Apply weights
        weighted_data = norm_data * weights

        # Identify ideal and negative-ideal solutions
        ideal_solution = np.max(weighted_data, axis=0) * (np.array(impacts) == '+') + \
                         np.min(weighted_data, axis=0) * (np.array(impacts) == '-')
        negative_ideal_solution = np.min(weighted_data, axis=0) * (np.array(impacts) == '+') + \
                                  np.max(weighted_data, axis=0) * (np.array(impacts) == '-')

        # Calculate distances
        distance_to_ideal = np.sqrt(((weighted_data - ideal_solution)**2).sum(axis=1))
        distance_to_negative = np.sqrt(((weighted_data - negative_ideal_solution)**2).sum(axis=1))

        # Calculate TOPSIS score and rank
        topsis_score = distance_to_negative / (distance_to_ideal + distance_to_negative)
        data['Topsis Score'] = topsis_score
        data['Rank'] = pd.Series(topsis_score).rank(ascending=False).astype(int)

        # Save the result
        data.to_csv(result_file, index=False)
        print(f"Results saved to {result_file}")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python 102203322.py <InputDataFile> <Weights> <Impacts> <ResultFileName>")
    else:
        input_file, weights, impacts, result_file = sys.argv[1:]
        topsis(input_file, weights, impacts, result_file)
