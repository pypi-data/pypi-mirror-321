import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):
    try:
        # Load input data
        data = pd.read_csv(input_file)

        # Validate the input file structure
        if data.shape[1] < 3:
            raise ValueError("Input file must have at least three columns.")

        # Extract decision matrix
        decision_matrix = data.iloc[:, 1:].values

        # Validate numeric data
        if not np.issubdtype(decision_matrix.dtype, np.number):
            raise ValueError("All columns except the first must contain numeric values.")

        # Validate weights and impacts
        weights = [float(w) for w in weights.split(',')]
        impacts = impacts.split(',')
        if len(weights) != decision_matrix.shape[1] or len(impacts) != decision_matrix.shape[1]:
            raise ValueError("Number of weights and impacts must match the number of criteria.")
        if not all(i in ['+', '-'] for i in impacts):
            raise ValueError("Impacts must be either '+' or '-'.")

        # Step 1: Normalize the decision matrix
        norm_matrix = decision_matrix / np.sqrt((decision_matrix**2).sum(axis=0))

        # Step 2: Weight the normalized matrix
        weighted_matrix = norm_matrix * weights

        # Step 3: Determine ideal best and ideal worst
        ideal_best = np.where(np.array(impacts) == '+', weighted_matrix.max(axis=0), weighted_matrix.min(axis=0))
        ideal_worst = np.where(np.array(impacts) == '+', weighted_matrix.min(axis=0), weighted_matrix.max(axis=0))

        # Step 4: Calculate separation measures
        dist_to_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
        dist_to_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))

        # Step 5: Calculate TOPSIS score
        scores = dist_to_worst / (dist_to_best + dist_to_worst)

        # Step 6: Rank alternatives
        data['Topsis Score'] = scores
        data['Rank'] = scores.argsort()[::-1] + 1

        # Save to output file
        data.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python 102217004.py <InputDataFile> <Weights> <Impacts> <ResultFileName>")
    else:
        _, input_file, weights, impacts, output_file = sys.argv
        topsis(input_file, weights, impacts, output_file)
