 
import numpy as np

def topsis(matrix, weights, impacts):
    if len(matrix[0]) != len(weights) or len(matrix[0]) != len(impacts):
        raise ValueError("Number of weights, impacts, and criteria must match.")

    # Step 1: Normalize the decision matrix
    norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))

    # Step 2: Apply weights
    weighted_matrix = norm_matrix * weights

    # Step 3: Identify ideal best and worst
    ideal_best = [(max if impact == "+" else min)(weighted_matrix[:, j]) for j, impact in enumerate(impacts)]
    ideal_worst = [(min if impact == "+" else max)(weighted_matrix[:, j]) for j, impact in enumerate(impacts)]

    # Step 4: Calculate separation measures
    separation_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
    separation_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))

    # Step 5: Calculate relative closeness
    scores = separation_worst / (separation_best + separation_worst)

    return scores
