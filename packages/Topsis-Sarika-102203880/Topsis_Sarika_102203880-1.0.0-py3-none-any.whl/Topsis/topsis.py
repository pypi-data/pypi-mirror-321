import numpy as np
import pandas as pd

class Topsis:
    def __init__(self, data, weights, impacts):
        self.data = np.array(data, dtype=float)
        self.weights = np.array(weights, dtype=float)
        self.impacts = np.array(impacts)

    def normalize_matrix(self):
        norm_matrix = self.data / np.sqrt((self.data ** 2).sum(axis=0))
        return norm_matrix

    def weighted_normalized_matrix(self):
        norm_matrix = self.normalize_matrix()
        weighted_matrix = norm_matrix * self.weights
        return weighted_matrix

    def ideal_best_worst(self):
        weighted_matrix = self.weighted_normalized_matrix()
        ideal_best = np.where(self.impacts == '+', np.max(weighted_matrix, axis=0), np.min(weighted_matrix, axis=0))
        ideal_worst = np.where(self.impacts == '+', np.min(weighted_matrix, axis=0), np.max(weighted_matrix, axis=0))
        return ideal_best, ideal_worst

    def calculate_topsis_score(self):
        ideal_best, ideal_worst = self.ideal_best_worst()
        weighted_matrix = self.weighted_normalized_matrix()

        dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
        dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

        scores = dist_worst / (dist_best + dist_worst)
        ranks = scores.argsort()[::-1] + 1
        return scores, ranks
