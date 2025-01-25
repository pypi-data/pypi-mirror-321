import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):
    try:
        # TOPSIS logic (same as before)
        data = pd.read_csv(input_file)
        if data.shape[1] < 3:
            raise Exception("Input file must have at least three columns.")

        # Parsing weights and impacts
        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')

        if len(weights) != len(impacts) or len(weights) != data.shape[1] - 1:
            raise Exception("Number of weights and impacts must match the number of criteria.")

        # Normalizing data
        criteria_data = data.iloc[:, 1:].values
        normalized_data = criteria_data / np.sqrt((criteria_data ** 2).sum(axis=0))

        # Weighted normalized decision matrix
        weighted_data = normalized_data * weights

        # Calculating ideal best and worst
        ideal_best = np.max(weighted_data, axis=0) if impacts[0] == "+" else np.min(weighted_data, axis=0)
        ideal_worst = np.min(weighted_data, axis=0) if impacts[0] == "+" else np.max(weighted_data, axis=0)

        distances_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
        distances_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))
        scores = distances_worst / (distances_best + distances_worst)

        # Adding results to DataFrame
        data['Topsis Score'] = scores
        data['Rank'] = scores.argsort()[::-1] + 1

        # Saving output to a file
        data.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")
