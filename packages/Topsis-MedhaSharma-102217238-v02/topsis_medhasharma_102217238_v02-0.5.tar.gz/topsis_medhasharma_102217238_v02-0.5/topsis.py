
import numpy as np
import pandas as pd

def topsis(data, weights, impacts):
    # Step 1: Normalize the decision matrix
    norm_data = data / np.sqrt((data**2).sum(axis=0))

    # Step 2: Apply the weights
    weighted_data = norm_data * weights

    # Step 3: Calculate ideal and negative ideal solutions
    ideal_solution = np.max(weighted_data, axis=0) * (np.array(impacts) == '+') + np.min(weighted_data, axis=0) * (np.array(impacts) == '-')
    negative_ideal_solution = np.min(weighted_data, axis=0) * (np.array(impacts) == '+') + np.max(weighted_data, axis=0) * (np.array(impacts) == '-')

    # Step 4: Calculate the distances to the ideal and negative ideal solutions
    positive_distance = np.sqrt(((weighted_data - ideal_solution)**2).sum(axis=1))
    negative_distance = np.sqrt(((weighted_data - negative_ideal_solution)**2).sum(axis=1))

    # Step 5: Calculate the TOPSIS score and rank
    topsis_score = negative_distance / (positive_distance + negative_distance)
    rank = topsis_score.argsort() + 1  # Ranks are 1-indexed

    return topsis_score, rank
