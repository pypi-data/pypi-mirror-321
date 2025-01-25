import numpy as np

class Topsis:
    @staticmethod
    def evaluate(data, weights, impacts):
        """
        Perform TOPSIS evaluation.

        Parameters:
            data (list of list of float): Decision matrix.
            weights (list of float): Weights for each criterion.
            impacts (list of str): '+' for beneficial criteria and '-' for non-beneficial criteria.

        Returns:
            list of int: Rank of each alternative.
        """
        data = np.array(data, dtype=float)
        weights = np.array(weights, dtype=float)

        # Step 1: Normalize the decision matrix
        norm_matrix = data / np.sqrt((data ** 2).sum(axis=0))

        # Step 2: Multiply by weights
        weighted_matrix = norm_matrix * weights

        # Step 3: Determine ideal best and worst
        ideal_best = np.zeros(data.shape[1])
        ideal_worst = np.zeros(data.shape[1])

        for i in range(len(impacts)):
            if impacts[i] == '+':
                ideal_best[i] = weighted_matrix[:, i].max()
                ideal_worst[i] = weighted_matrix[:, i].min()
            else:
                ideal_best[i] = weighted_matrix[:, i].min()
                ideal_worst[i] = weighted_matrix[:, i].max()

        # Step 4: Calculate the distance from ideal best and worst
        dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
        dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

        # Step 5: Calculate the relative closeness to the ideal solution
        scores = dist_worst / (dist_best + dist_worst)

        # Step 6: Rank the alternatives
        ranks = scores.argsort()[::-1] + 1

        return ranks
