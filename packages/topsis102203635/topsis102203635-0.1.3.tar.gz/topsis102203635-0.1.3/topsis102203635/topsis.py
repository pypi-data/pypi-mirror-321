import pandas as pd
import numpy as np

# Enhanced TOPSIS class
class Topsis:
    def __init__(self, df, weights, impacts, distance_metric='euclidean', reverse_rank=False):
        """
        Initialize TOPSIS analysis with extra parameters for displaying results.
        
        Args:
        df (pandas.DataFrame): Decision matrix where rows are alternatives and columns are criteria
        weights (list): List of weights for the criteria
        impacts (list): List of impacts for the criteria (+ or -)
        distance_metric (str): The distance metric to use. Default is 'euclidean'.
        reverse_rank (bool): Whether to reverse the ranking order (True/False).
        """

        self.df=df
        self.weights = weights
        self.impacts = impacts
        self.distance_metric = distance_metric
        self.reverse_rank = reverse_rank

    def calculate(self):
        def calculate_distance(df, solution, metric):
            if metric == 'euclidean':
                return np.sqrt(((df - solution) ** 2).sum(axis=1))
            elif metric == 'manhattan':
                return np.abs(df - solution).sum(axis=1)
            else:
                raise ValueError(f"Unknown distance metric: {metric}")
        
        # Select only numeric columns to avoid errors and to normalized DataFrame
        numeric_cols = self.df.select_dtypes(include=['number'])
        norm_df = ((numeric_cols.apply(lambda x: x / np.sqrt((x**2).sum()), axis=0))*self.weights)


        # Initialize ideal and negative ideal solutions
        ideal_solution = norm_df.max()
        negative_ideal_solution = norm_df.min()

        # Adjust ideal and negative ideal for 'impact' of criteria
        for i, impact in enumerate(self.impacts):
            if impact == '-':
                ideal_solution[i], negative_ideal_solution[i] = negative_ideal_solution[i], ideal_solution[i]

        # Calculate distances to ideal and negative ideal solutions
        distance_ideal = calculate_distance(norm_df, ideal_solution, self.distance_metric)
        distance_negative_ideal = calculate_distance(norm_df, negative_ideal_solution, self.distance_metric)

        # Calculate performance scores
        scores = distance_negative_ideal / (distance_ideal + distance_negative_ideal)

        # Prepare the result DataFrame
        result_df = pd.DataFrame({
            'Alternative': self.df.index,
            **numeric_cols.to_dict(orient='list'),
            'Topsis Score': scores
        })

        # Assign ranks based on Topsis Score
        result_df['Rank'] = result_df['Topsis Score'].rank(
            ascending=not self.reverse_rank,  # Ascending ranks if reverse_rank is False
            method='min'  # Rank using the minimum value
        )

        # Sort the DataFrame based on rank
        result_df = result_df.sort_values(by='Rank')

        return result_df[['Model', 'Topsis Score', 'Rank']]