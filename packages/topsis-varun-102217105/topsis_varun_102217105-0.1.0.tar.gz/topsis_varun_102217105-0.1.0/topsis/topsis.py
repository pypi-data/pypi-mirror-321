# import numpy as np

# class Topsis:
#     def __init__(self, data, weights, impacts):
#         self.data = data
#         self.weights = weights
#         self.impacts = impacts

#     def normalise(self):
#         total_sum = np.sum(self.data**2, axis=0)
#         norm_mat = self.data / np.sqrt(np.sqrt(total_sum))
#         return norm_mat
    
#     def weighted_normalise(self, norm_mat):
#         weighted_mat = norm_mat * self.weights
#         return weighted_mat

#     def find_ideal_solution(self, weighted_mat):
#         ideal_best = []
#         ideal_worst = []
        
#         for i, impact in enumerate(self.impacts):
#             if impact == "+":
#                 ideal_best.append(np.max(weighted_mat[:, i]))
#                 ideal_worst.append(np.min(weighted_mat[:, i]))
#             else:
#                 ideal_best.append(np.min(weighted_mat[:, i]))
#                 ideal_worst.append(np.max(weighted_mat[:, i]))

#         return np.array(ideal_best), np.array(ideal_worst)
    

#     def calculate_distances(self, weighted_mat, ideal_best, ideal_worst):
#         dist_to_ideal_best = np.sqrt(np.sum((weighted_mat - ideal_best)**2, axis=1))
#         dist_to_ideal_worst = np.sqrt(np.sum((weighted_mat - ideal_worst)**2, axis=1))
#         return dist_to_ideal_best, dist_to_ideal_worst
    
#     def calculate_scores(self, dist_to_ideal_best, dist_to_ideal_worst):
#         scores = dist_to_ideal_worst / (dist_to_ideal_best + dist_to_ideal_worst)
#         return scores
    
#     def rank(self, scores):
#         norm_mat = self.normalise()
#         weighted_mat = self.weighted_normalise(norm_mat)
#         ideal_best, ideal_worst = self.find_ideal_solution(weighted_mat)
#         dist_to_ideal_best, dist_to_ideal_worst = self.calculate_distances(weighted_mat, ideal_best, ideal_worst)
#         scores = self.calculate_scores(dist_to_ideal_best, dist_to_ideal_worst)
#         rankings = np.argsort(-scores) + 1
#         return rankings, scores

import numpy as np
import argparse
import os
import pandas as pd

def topsis(data, weights, impacts):
    """
    Perform TOPSIS analysis on the given data.

    Parameters:
    - data: 2D list or numpy array with the data matrix.
    - weights: List of weights for each criterion.
    - impacts: List of '+' or '-' for each criterion impact.

    Returns:
    - Ranks of the alternatives.
    """

    # Convert input data to numpy array for easy matrix manipulation
    data = np.array(data, dtype=float)

    # Step 1: Normalize the decision matrix
    norm_data = data / np.sqrt((data ** 2).sum(axis=0))

    # Step 2: Apply weights to normalized data
    weighted_data = norm_data * weights

    # Step 3: Calculate ideal best and ideal worst
    ideal_best = np.where(impacts == '+', weighted_data.max(axis=0), weighted_data.min(axis=0))
    ideal_worst = np.where(impacts == '+', weighted_data.min(axis=0), weighted_data.max(axis=0))

    # Step 4: Calculate the distance from the ideal best and worst
    dist_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Calculate the performance score and rank alternatives
    performance_score = dist_worst / (dist_best + dist_worst)
    rank = performance_score.argsort()[::-1] + 1

    return rank

def excel_to_csv(excel_file, csv_output):
    """
    Convert Excel file to CSV.
    
    Parameters:
    - excel_file: The input Excel file (.xlsx or .xls).
    - csv_output: The path to the output CSV file.
    
    Returns:
    - The CSV file path.
    """
    df = pd.read_excel(excel_file)
    df.to_csv(csv_output, index=False)
    return csv_output

def main():
    parser = argparse.ArgumentParser(description="TOPSIS method for decision making")
    parser.add_argument("input_file", help="CSV file containing the decision matrix")
    parser.add_argument("weights", help="Weights for each criterion, separated by commas")
    parser.add_argument("impacts", help="Impacts for each criterion (+/-), separated by commas")
    parser.add_argument("output_file", help="File where results will be saved")

    args = parser.parse_args()

    input_file = args.input_file

    if input_file.endswith(('.xlsx', '.xls')):
        # Convert Excel to CSV
        csv_file = os.path.splitext(input_file)[0] + ".csv"
        input_file = excel_to_csv(args.input_file, csv_file)

    # Read the input CSV file
    data = pd.read_csv(input_file)

    # Convert weights and impacts
    weights = list(map(float, args.weights.split(',')))
    impacts = np.array(args.impacts.split(','))

    # Perform TOPSIS
    rank = topsis(data.iloc[:, 1:].values, weights, impacts)

    # Save results to the output file
    data['Rank'] = rank
    data.to_csv(args.output_file, index=False)
    print("Results saved to", args.output_file)

if __name__ == "__main__":
    main()
