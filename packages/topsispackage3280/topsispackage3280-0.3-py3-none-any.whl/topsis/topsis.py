import os
import sys
import pandas as pd
import numpy as np

class Topsis:
    def __init__(self, filename):
        """
        Initializes the Topsis object by reading the input CSV file.
        """
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"File '{filename}' not found.")

        self.data = pd.read_csv(filename)
        self.features = self.data.shape[1] - 1  # Excluding the first column (assumed to be names/identifiers)
        self.samples = self.data.shape[0]
        self.matrix = self.data.iloc[:, 1:].values.astype(float)  # Converting to numerical values

    def evaluate(self, weights=None, impacts=None):
        """
        Evaluate the dataset using TOPSIS methodology.

        :param weights: List of weights for the criteria.
        :param impacts: List of impacts for the criteria ('+' for benefit, '-' for cost).
        :return: A list of rankings for each sample.
        """
        if weights is None:
            weights = [1] * self.features
        if impacts is None:
            impacts = ['+'] * self.features

        if len(weights) != self.features or len(impacts) != self.features:
            raise ValueError("Weights and impacts must match the number of criteria.")

        # Normalize the matrix
        norm_matrix = self.matrix / np.sqrt((self.matrix ** 2).sum(axis=0))

        # Apply weights
        weighted_matrix = norm_matrix * weights

        # Determine ideal best and worst values
        ideal_best = []
        ideal_worst = []
        for i in range(self.features):
            if impacts[i] == '+':
                ideal_best.append(np.max(weighted_matrix[:, i]))
                ideal_worst.append(np.min(weighted_matrix[:, i]))
            else:
                ideal_best.append(np.min(weighted_matrix[:, i]))
                ideal_worst.append(np.max(weighted_matrix[:, i]))

        # Calculate distances to ideal best and worst
        distances_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
        distances_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

        # Calculate performance scores
        scores = distances_worst / (distances_best + distances_worst)

        # Rank the scores
        rankings = np.argsort(scores)[::-1] + 1  # Higher scores get better ranks

        # Combine results
        results = pd.DataFrame({
            'Sample': self.data.iloc[:, 0],
            'Score': scores,
            'Rank': rankings
        })
        return results.sort_values(by='Rank')


def main():
    if len(sys.argv) != 4:
        print("Usage: python topsis.py <filename> <weights> <impacts>")
        print("Example: python topsis.py data.csv 1,2,3 +,-,+")
        return

    filename = sys.argv[1]
    weights = list(map(float, sys.argv[2].split(',')))
    impacts = sys.argv[3].split(',')

    try:
        topsis = Topsis(filename)
        results = topsis.evaluate(weights, impacts)
        print(results)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
