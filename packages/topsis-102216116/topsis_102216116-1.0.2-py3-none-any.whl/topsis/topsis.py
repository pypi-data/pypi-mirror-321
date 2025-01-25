import numpy as np

def calculate_topsis(data, weights, impacts):
    # Normalize data
    norm_data = data / np.sqrt((data ** 2).sum(axis=0))
    weighted_data = norm_data * weights

    # Calculate ideal best and ideal worst
    ideal_best = np.max(weighted_data * np.array(impacts), axis=0)
    ideal_worst = np.min(weighted_data * np.array(impacts), axis=0)

    # Calculate distances
    dist_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    # Calculate scores
    scores = dist_worst / (dist_best + dist_worst)
    return scores
