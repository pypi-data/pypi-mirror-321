import numpy as np
import pandas as pd
import sys
import os

class Topsis:
    def __init__(self, data, weights, impacts):
        self.data = np.array(data, dtype=float)
        self.weights = np.array(weights, dtype=float)
        self.impacts = impacts
        self.num_rows, self.num_cols = self.data.shape

        if len(weights) != self.num_cols or len(impacts) != self.num_cols:
            raise ValueError("The number of weights and impacts must match the number of criteria.")
        if not all(i in ['+', '-'] for i in impacts):
            raise ValueError("Impacts must be '+' for beneficial or '-' for non-beneficial criteria.")

    def normalize(self):
        return self.data / np.sqrt(np.sum(self.data**2, axis=0))

    def apply_weights(self, normalized_matrix):
        return normalized_matrix * self.weights

    def calculate_ideal_values(self, weighted_matrix):
        ideal_best = []
        ideal_worst = []

        for i in range(self.num_cols):
            if self.impacts[i] == '+':
                ideal_best.append(np.max(weighted_matrix[:, i]))
                ideal_worst.append(np.min(weighted_matrix[:, i]))
            else:
                ideal_best.append(np.min(weighted_matrix[:, i]))
                ideal_worst.append(np.max(weighted_matrix[:, i]))

        return np.array(ideal_best), np.array(ideal_worst)

    def calculate_distances(self, weighted_matrix, ideal_best, ideal_worst):
        dist_best = np.sqrt(np.sum((weighted_matrix - ideal_best)**2, axis=1))
        dist_worst = np.sqrt(np.sum((weighted_matrix - ideal_worst)**2, axis=1))
        return dist_best, dist_worst

    def calculate_scores(self, dist_best, dist_worst):
        return dist_worst / (dist_best + dist_worst)

    def rank(self):
        normalized_matrix = self.normalize()
        weighted_matrix = self.apply_weights(normalized_matrix)
        ideal_best, ideal_worst = self.calculate_ideal_values(weighted_matrix)
        dist_best, dist_worst = self.calculate_distances(weighted_matrix, ideal_best, ideal_worst)
        scores = self.calculate_scores(dist_best, dist_worst)
        rankings = np.argsort(scores)[::-1] + 1
        return scores, rankings


def run_topsis():
    if len(sys.argv) != 4:
        print("Usage: python -m topsis <csv_file> <weights> <impacts>")
        sys.exit(1)

    file_path = sys.argv[1]
    weights = list(map(float, sys.argv[2].strip('[]').split(',')))
    impacts = sys.argv[3].strip('[]').split(',')

    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found.")
        sys.exit(1)

    try:
        data = pd.read_csv(file_path).iloc[:, 1:].values
        topsis = Topsis(data, weights, impacts)
        scores, ranks = topsis.rank()
        print("\nPerformance Scores:")
        print(scores)
        print("\nRankings:")
        print(ranks)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    run_topsis()
