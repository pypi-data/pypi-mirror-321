import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from joblib import Parallel, delayed
import os
import speech_recognition as sr
from concurrent.futures import ThreadPoolExecutor
import threading

# Lock to prevent race conditions in multi-threaded environment
lock = threading.Lock()

def fill_missing_data(df, strategy='mean'):
    # Apply missing data strategy only to numeric columns
    numeric_cols = df.select_dtypes(include=['number'])
    if strategy == 'mean':
        df[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.mean())
    elif strategy == 'median':
        df[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.median())
    elif strategy == 'mode':
        df[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.mode().iloc[0])
    elif strategy == 'ffill':
        df = df.fillna(method='ffill')
    elif strategy == 'bfill':
        df = df.fillna(method='bfill')
    elif strategy == 'interpolate_linear':
        df[numeric_cols.columns] = numeric_cols.interpolate(method='linear')
    elif strategy == 'interpolate_polynomial':
        df[numeric_cols.columns] = numeric_cols.interpolate(method='polynomial', order=2)
    else:
        raise ValueError(f"Unknown missing data strategy: {strategy}")
    return df

# Enhanced TOPSIS class
class Topsis:
    def __init__(self, df, weights, impacts, distance_metric='euclidean', missing_data_strategy='mean', show_para=False, reverse_rank=False):
        """
        Initialize TOPSIS analysis with extra parameters for displaying results.
        
        Args:
        df (pandas.DataFrame): Decision matrix where rows are alternatives and columns are criteria
        weights (list): List of weights for the criteria
        impacts (list): List of impacts for the criteria (+ or -)
        distance_metric (str): The distance metric to use. Default is 'euclidean'.
        missing_data_strategy (str): The strategy for filling missing data. Default is 'mean'.
        show_para (bool): Whether to show parameters (True/False).
        reverse_rank (bool): Whether to reverse the ranking order (True/False).
        """
        self.df = fill_missing_data(df, strategy=missing_data_strategy)
        self.weights = weights
        self.impacts = impacts
        self.distance_metric = distance_metric
        self.show_para = show_para
        self.reverse_rank = reverse_rank

    def calculate(self):
    
    
    # Select only numeric columns to avoid errors
        numeric_cols = self.df.select_dtypes(include=['number'])
        norm_df = numeric_cols.apply(lambda x: x / np.sqrt((x**2).sum()), axis=0)

        # Apply weights to the normalized DataFrame
        norm_df = norm_df * self.weights

        # Initialize ideal and negative ideal solutions
        ideal_solution = norm_df.max()
        negative_ideal_solution = norm_df.min()

        # Adjust ideal and negative ideal for 'impact' of criteria
        for i, impact in enumerate(self.impacts):
            if impact == '-':
                ideal_solution[i], negative_ideal_solution[i] = negative_ideal_solution[i], ideal_solution[i]

        # Calculate distances
        def calculate_distance(df, solution, metric):
            if metric == 'euclidean':
                return np.sqrt(((df - solution) ** 2).sum(axis=1))
            elif metric == 'manhattan':
                return np.abs(df - solution).sum(axis=1)
            elif metric == 'chebyshev':
                return np.max(np.abs(df - solution), axis=1)
            elif metric == 'minkowski':
                return np.power(((df - solution) ** 2).sum(axis=1), 1/3)
            elif metric == 'cosine':
                return 1 - np.sum(df * solution, axis=1) / (np.sqrt(np.sum(df**2, axis=1)) * np.sqrt(np.sum(solution**2)))
            else:
                raise ValueError(f"Unknown distance metric: {metric}")

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

        # Rank based on scores
        result_df['Rank'] = result_df['Topsis Score'].rank(ascending=not self.reverse_rank, method='max')

        # Sort the DataFrame based on rank
        result_df = result_df.sort_values(by='Rank', ascending=not self.reverse_rank)

        if self.show_para:
            # Display the full dataframe with parameters, Topsis Score, and Rank
            return result_df[['Alternative'] + [col for col in numeric_cols.columns] + ['Topsis Score', 'Rank']]
        else:
            # Display only Topsis Score and Rank
            return result_df[['Alternative', 'Topsis Score', 'Rank']]

    def plot_graph(self, ranked_results):
        """Plot the bar graph for the TOPSIS results."""
        plt.bar(ranked_results['Alternative'], ranked_results['Topsis Score'])
        plt.xlabel('Alternatives')
        plt.ylabel('Topsis Score')
        plt.title('TOPSIS Ranking')
        plt.show()


# VoiceControl class for enabling voice commands
class VoiceControl:

    def __init__(self, dataframe, weights, impacts):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.dataframe = dataframe
        self.weights = weights
        self.impacts = impacts
        self.topsis = Topsis(self.dataframe, self.weights, self.impacts, show_para=False)

    def listen_for_command(self):
        with self.microphone as source:
            print("Listening for command...")
            audio = self.recognizer.listen(source)

        try:
            print("Command received...")
            command = self.recognizer.recognize_google(audio).lower()
            print(f"Command received: {command}")

            # Map the commands to appropriate actions
            if "start" in command:
                return "start"
            elif "fill missing" in command:
                return "fill missing"
            elif "graph" in command:
                return "graph"
            elif "exit" in command:
                return "exit"
            elif "help" in command:
                return "help"
            else:
                return "unknown"
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "error"
        except sr.RequestError:
            print("Sorry, there was an error with the request.")
            return "error"
        
    def start_topsis_analysis(self):
        print("Starting TOPSIS analysis...")
        filled_df = fill_missing_data(self.dataframe, strategy='mean')  # Handle missing data
        self.topsis.dataframe = filled_df  # Update dataframe after filling missing values
        results = self.topsis.calculate()  # Perform TOPSIS calculation
        print("\nTOPSIS analysis results:")
        print(results)


    def plot_graph(self):
        print("Plotting graph...")
        results = self.topsis.calculate()
        self.topsis.plot_graph(results)  # Use your existing plotting function here
  
    def run(self):
        while True:
            command = self.listen_for_command()

            if command == "start":
                self.start_topsis_analysis()
            elif command == "fill missing":
                print("Filling missing data...")
                filled_df = fill_missing_data(self.dataframe, strategy='mean')
                print("Filled DataFrame:")
                print(filled_df)
            elif command == "graph":
                self.plot_graph()
            elif command== "help":
                self.show_help()
            elif command == "exit":
                print("Exiting application...")
                break
            else:
                print(f"Unknown command: {command}")

    def show_help(self):
        """Show basic help about the package and commands."""
        print("Voice-Controlled TOPSIS commands:")
        print("1. 'start topsis' to begin, and save results in data frame")
        print("2. 'exit' to quit the application.")
        print("3. 'help' for help.")
        print("4. 'graph' to see a graph of the results.")
        print("5. For package documentation, visit PyPi and search topsis102203633Danishsharma.")
