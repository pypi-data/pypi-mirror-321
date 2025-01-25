import numpy as np

def topsis(data, weights, impacts):
    # Normalize the decision matrix
    data = np.array(data)
    norm_data = data / np.sqrt((data ** 2).sum(axis=0))
    
    # Apply weights
    weighted_data = norm_data * weights
    
    # Determine ideal and anti-ideal solutions
    ideal_solution = []
    anti_ideal_solution = []
    for i, impact in enumerate(impacts):
        if impact == '+':
            ideal_solution.append(weighted_data[:, i].max())
            anti_ideal_solution.append(weighted_data[:, i].min())
        elif impact == '-':
            ideal_solution.append(weighted_data[:, i].min())
            anti_ideal_solution.append(weighted_data[:, i].max())
    
    ideal_solution = np.array(ideal_solution)
    anti_ideal_solution = np.array(anti_ideal_solution)
    
    # Calculate distances to ideal and anti-ideal solutions
    distance_to_ideal = np.sqrt(((weighted_data - ideal_solution) ** 2).sum(axis=1))
    distance_to_anti_ideal = np.sqrt(((weighted_data - anti_ideal_solution) ** 2).sum(axis=1))
    
    # Calculate relative closeness and rank
    relative_closeness = distance_to_anti_ideal / (distance_to_ideal + distance_to_anti_ideal)
    rankings = relative_closeness.argsort()[::-1] + 1
    
    return rankings
