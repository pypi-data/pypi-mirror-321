import numpy as np

class Topsis:
    def __init__(self, matrix, weights, impacts):
        # Ensure matrix is a NumPy array and contains only numeric values
        self.matrix = np.array(matrix, dtype=float)  # Convert to float
        self.weights = np.array(weights)
        self.impacts = impacts

    def calculate(self):
        # Normalize the decision matrix
        norm_matrix = self.matrix / np.linalg.norm(self.matrix, axis=0)

        # Weighted normalized matrix
        weighted_matrix = norm_matrix * self.weights

        # Calculate ideal and negative ideal solutions
        ideal_solution = np.max(weighted_matrix, axis=0)
        negative_ideal_solution = np.min(weighted_matrix, axis=0)

        # Calculate distances
        distance_ideal = np.sqrt(np.sum((weighted_matrix - ideal_solution) ** 2, axis=1))
        distance_negative_ideal = np.sqrt(np.sum((weighted_matrix - negative_ideal_solution) ** 2, axis=1))

        # Calculate performance score
        score = distance_negative_ideal / (distance_ideal + distance_negative_ideal)

        return score