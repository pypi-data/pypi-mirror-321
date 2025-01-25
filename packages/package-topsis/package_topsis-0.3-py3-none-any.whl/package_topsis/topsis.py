"""
topsis.py: A module for performing TOPSIS analysis.

Usage:
    from package_topsis import topsis

    data = [
        [250, 16, 12, 5],
        [200, 16, 8, 3],
        [300, 32, 16, 4],
        [275, 32, 8, 4],
        [225, 16, 16, 2],
    ]
    weights = [0.25, 0.25, 0.25, 0.25]
    impacts = ['+', '+', '-', '+']

    rankings = topsis(data, weights, impacts)
    print(rankings)  # Output: [3, 1, 2, 5, 4]
"""

import numpy as np

def topsis(data, weights, impacts):
    """
    Perform TOPSIS decision-making analysis.

    Parameters:
        data (list of lists): The decision matrix.
        weights (list): The weights for each criterion.
        impacts (list): '+' for benefit and '-' for cost criteria.

    Returns:
        list: A ranking of alternatives, where 1 is the best.
    """
    data = np.array(data)
    weights = np.array(weights)
    
    
    norm_data = data / np.sqrt((data**2).sum(axis=0))

   
    weighted_data = norm_data * weights

    
    ideal_best = np.max(weighted_data, axis=0) if '+' in impacts else np.min(weighted_data, axis=0)
    ideal_worst = np.min(weighted_data, axis=0) if '+' in impacts else np.max(weighted_data, axis=0)

    distances_best = np.sqrt(((weighted_data - ideal_best)**2).sum(axis=1))
    distances_worst = np.sqrt(((weighted_data - ideal_worst)**2).sum(axis=1))


    scores = distances_worst / (distances_best + distances_worst)

    
    rankings = scores.argsort()[::-1] + 1

    return rankings



