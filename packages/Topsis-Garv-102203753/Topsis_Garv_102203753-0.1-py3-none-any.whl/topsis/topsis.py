import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):
    try:
        # Load and validate input data
        data = pd.read_csv(input_file)
        if data.shape[1] < 3:
            raise ValueError("Input file must have at least three columns.")

        weights = [float(w) for w in weights.split(',')]
        impacts = impacts.split(',')

        if len(weights) != len(impacts) or len(weights) != (data.shape[1] - 1):
            raise ValueError("Number of weights, impacts, and criteria must match.")

        if not all(impact in ['+', '-'] for impact in impacts):
            raise ValueError("Impacts must be '+' or '-'.")

        # Normalize the decision matrix
        decision_matrix = data.iloc[:, 1:].values
        norm_matrix = decision_matrix / np.sqrt((decision_matrix ** 2).sum(axis=0))

        # Weight the normalized matrix
        weighted_matrix = norm_matrix * weights

        # Determine ideal best and worst
        ideal_best = [np.max(weighted_matrix[:, i]) if impacts[i] == '+' else np.min(weighted_matrix[:, i])
                      for i in range(len(impacts))]
        ideal_worst = [np.min(weighted_matrix[:, i]) if impacts[i] == '+' else np.max(weighted_matrix[:, i])
                       for i in range(len(impacts))]

        # Calculate distances to ideal best and worst
        distances_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
        distances_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

        # Calculate TOPSIS score and rank
        scores = distances_worst / (distances_best + distances_worst)
        data['Topsis Score'] = scores
        data['Rank'] = scores.rank(ascending=False).astype(int)

        # Save the results
        data.to_csv(output_file, index=False)
        print(f"Output saved to {output_file}")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
    else:
        _, input_file, weights, impacts, output_file = sys.argv
        topsis(input_file, weights, impacts, output_file)
