import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from joblib import Parallel, delayed

# Enhanced function for filling missing data
def fill_missing_data(df, strategy='mean'):
    """
    Fill missing data in the DataFrame using the specified strategy.
    Args:
    df (pandas.DataFrame): The DataFrame with missing values.
    strategy (str): The strategy to use for filling missing data. Options are:
                    'mean', 'median', 'mode', 'ffill', 'bfill', 'interpolate_linear', 'interpolate_polynomial'. Default is 'mean'.
    Returns:
    pandas.DataFrame: The DataFrame with missing values filled.
    """
    if strategy == 'mean':
        return df.fillna(df.mean())
    elif strategy == 'median':
        return df.fillna(df.median())
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    elif strategy == 'ffill':
        return df.fillna(method='ffill')
    elif strategy == 'bfill':
        return df.fillna(method='bfill')
    elif strategy == 'interpolate_linear':
        return df.interpolate(method='linear')
    elif strategy == 'interpolate_polynomial':
        return df.interpolate(method='polynomial', order=2)  # You can change the order as needed
    else:
        raise ValueError(f"Unknown missing data strategy: {strategy}")

# Enhanced TOPSIS function
def topsis(df, weights, impacts, distance_metric='euclidean', missing_data_strategy='mean'):
    """
    Function to calculate TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)
    
    Args:
    df (pandas.DataFrame): Decision matrix where rows are alternatives and columns are criteria
    weights (list): List of weights for the criteria
    impacts (list): List of impacts for the criteria (+ or -)
    distance_metric (str): The distance metric to use. Default is 'euclidean'. Options are:
                           'euclidean', 'manhattan', 'chebyshev', 'minkowski', 'cosine'
    missing_data_strategy (str): The strategy for filling missing data. Default is 'mean'.
    
    Returns:
    pandas.DataFrame: Ranked alternatives based on TOPSIS
    """

    # Handle missing data according to the selected strategy
    df = fill_missing_data(df, strategy=missing_data_strategy)
    
    # Normalize the decision matrix
    norm_df = df.apply(lambda x: (x / np.sqrt((x**2).sum())) * weights, axis=0)
    
    # Initialize ideal and negative ideal solutions
    ideal_solution = norm_df.max()
    negative_ideal_solution = norm_df.min()

    # Adjust ideal and negative ideal for 'impact' of criteria
    for i, impact in enumerate(impacts):
        if impact == '-':
            ideal_solution[i], negative_ideal_solution[i] = negative_ideal_solution[i], ideal_solution[i]
    
    # Calculate the selected distance metric
    def calculate_distance(df, solution, metric):
        if metric == 'euclidean':
            return np.sqrt(((df - solution) ** 2).sum(axis=1))
        elif metric == 'manhattan':
            return np.abs(df - solution).sum(axis=1)
        elif metric == 'chebyshev':
            return np.max(np.abs(df - solution), axis=1)
        elif metric == 'minkowski':
            return np.power(((df - solution) ** 2).sum(axis=1), 1/3)  # Default p=3
        elif metric == 'cosine':
            return 1 - np.sum(df * solution, axis=1) / (np.sqrt(np.sum(df**2, axis=1)) * np.sqrt(np.sum(solution**2)))
        else:
            raise ValueError(f"Unknown distance metric: {metric}")
    
    # Calculate distances in parallel
    distance_ideal = Parallel(n_jobs=-1)(delayed(calculate_distance)(norm_df, ideal_solution, distance_metric))
    distance_negative_ideal = Parallel(n_jobs=-1)(delayed(calculate_distance)(norm_df, negative_ideal_solution, distance_metric))
    
    # Calculate the performance score
    scores = distance_negative_ideal / (distance_ideal + distance_negative_ideal)
    
    # Rank the alternatives
    ranked_alternatives = pd.DataFrame({
        'Alternative': df.index,
        'Score': scores
    }).sort_values(by='Score', ascending=False)
    
    # Visualization of the results
    plt.bar(ranked_alternatives['Alternative'], ranked_alternatives['Score'])
    plt.xlabel('Alternatives')
    plt.ylabel('Scores')
    plt.title('TOPSIS Ranking')
    plt.show()

    return ranked_alternatives
