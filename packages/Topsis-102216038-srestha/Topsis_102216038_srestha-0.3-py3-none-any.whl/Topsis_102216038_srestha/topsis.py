# Topsis-102216038-srestha/topsis.py

import numpy as np
import pandas as pd

class Topsis:
    def __init__(self, data, weights, impacts):
        self.data = data
        self.weights = weights
        self.impacts = impacts

    def normalize(self):
        norm_data = self.data.copy()
        for column in self.data.columns:
            norm_data[column] = self.data[column] / np.sqrt((self.data[column] ** 2).sum())
        return norm_data

    def calculate_ideal_best_worst(self, norm_data):
        ideal_best = []
        ideal_worst = []

        for i, impact in enumerate(self.impacts):
            if impact == "+":
                ideal_best.append(norm_data.iloc[:, i].max())
                ideal_worst.append(norm_data.iloc[:, i].min())
            elif impact == "-":
                ideal_best.append(norm_data.iloc[:, i].min())
                ideal_worst.append(norm_data.iloc[:, i].max())

        return np.array(ideal_best), np.array(ideal_worst)

    def calculate_scores(self):
        norm_data = self.normalize()
        weighted_data = norm_data * self.weights
        ideal_best, ideal_worst = self.calculate_ideal_best_worst(weighted_data)

        distances_to_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
        distances_to_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

        scores = distances_to_worst / (distances_to_best + distances_to_worst)
        return scores

    def rank(self):
        scores = self.calculate_scores()
        ranks = scores.argsort()[::-1] + 1
        return pd.DataFrame({"Score": scores, "Rank": ranks})

    @staticmethod
    def process(input_file, weights, impacts, output_file):
        # Read the input file
        data = pd.read_csv(input_file)

        if len(data.columns) < 3:
            raise ValueError("Input file must contain at least three columns: Object name and two criteria columns.")

        # Extract criteria and ensure all numeric values from the second column onward
        criteria = data.iloc[:, 1:]
        if not np.issubdtype(criteria.dtypes.values[0], np.number):
            raise ValueError("Criteria columns must contain numeric values only.")

        # Process TOPSIS
        topsis = Topsis(criteria, weights, impacts)
        result = topsis.rank()

        # Include the original data and add Topsis Score and Rank columns
        result = pd.concat([data, result], axis=1)
        result.to_csv(output_file, index=False)
        print(f"Results have been saved to {output_file}")
