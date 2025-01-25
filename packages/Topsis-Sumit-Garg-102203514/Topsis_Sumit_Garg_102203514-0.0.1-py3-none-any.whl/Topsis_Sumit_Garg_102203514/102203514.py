import numpy as np

def topsis(matrix, weights, impacts):
    """
    Perform TOPSIS calculation.

    :param matrix: Decision matrix (2D list or np.array)
    :param weights: List of weights
    :param impacts: List of '+' or '-' for each criterion
    :return: List of rankings
    """
    matrix = np.array(matrix, dtype=float)
    weights = np.array(weights, dtype=float)

    # Step 1: Normalize matrix
    norm_matrix = matrix / np.sqrt((matrix ** 2).sum(axis=0))

    # Step 2: Apply weights
    weighted_matrix = norm_matrix * weights

    # Step 3: Determine ideal best and worst
    ideal_best = []
    ideal_worst = []
    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted_matrix[:, i].max())
            ideal_worst.append(weighted_matrix[:, i].min())
        else:
            ideal_best.append(weighted_matrix[:, i].min())
            ideal_worst.append(weighted_matrix[:, i].max())

    # Step 4: Calculate distances
    best_dist = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    worst_dist = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Calculate scores and rank
    scores = worst_dist / (best_dist + worst_dist)
    return scores.argsort()[::-1] + 1
