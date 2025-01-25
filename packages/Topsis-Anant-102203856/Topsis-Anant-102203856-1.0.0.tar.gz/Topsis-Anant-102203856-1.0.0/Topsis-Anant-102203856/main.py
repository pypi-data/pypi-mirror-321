import pandas as pd
import numpy as np
import sys

def topsis(input_file, weights, impacts, output_file):
    try:
        # Reading input file
        data = pd.read_csv(input_file)

        # Validation checks
        if data.shape[1] < 3:
            raise ValueError("Input file must contain at least three columns.")
        if not all(data.iloc[:, 1:].applymap(lambda x: isinstance(x, (int, float))).all().values):
            raise ValueError("From the second column onwards, all values must be numeric.")

        weights = [float(w) for w in weights.split(',')]
        impacts = impacts.split(',')

        if len(weights) != data.shape[1] - 1 or len(impacts) != data.shape[1] - 1:
            raise ValueError("Number of weights and impacts must match the number of criteria.")
        if not all(i in ['+', '-'] for i in impacts):
            raise ValueError("Impacts must be either '+' or '-'.")

        # Normalize the decision matrix
        matrix = data.iloc[:, 1:].to_numpy()
        norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))

        # Weighted normalized decision matrix
        weights = np.array(weights)
        weighted_matrix = norm_matrix * weights

        # Identify ideal best and worst values
        ideal_best = np.where(np.array(impacts) == '+', weighted_matrix.max(axis=0), weighted_matrix.min(axis=0))
        ideal_worst = np.where(np.array(impacts) == '+', weighted_matrix.min(axis=0), weighted_matrix.max(axis=0))

        # Calculate separation measures
        separation_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
        separation_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))

        # Calculate TOPSIS scores
        topsis_scores = separation_worst / (separation_best + separation_worst)

        # Rank the alternatives
        data['Topsis Score'] = topsis_scores
        data['Rank'] = data['Topsis Score'].rank(ascending=False).astype(int)

        # Write the output file
        data.to_csv(output_file, index=False)
        print(f"Results successfully saved to {output_file}")

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