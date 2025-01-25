import pandas as pd
import numpy as np
import sys

def read_input_file(file_path):
    return pd.read_csv(file_path)

def validate_input(data, weights, impacts):
    if data.shape[1] < 3:
        raise ValueError("Input file must contain at least three columns.")
    if not np.issubdtype(data.iloc[:, 1:].dtypes.values[0], np.number):
        raise ValueError("Columns from 2nd to last must contain numeric values only.")
    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')
    if len(weights) != len(impacts) or len(weights) != data.shape[1] - 1:
        raise ValueError("Number of weights, impacts, and numeric columns must be the same.")
    if not all(i in ['+', '-'] for i in impacts):
        raise ValueError("Impacts must be either '+' or '-'.")
    return weights, impacts

def normalize_data(values):
    return values / np.sqrt((values ** 2).sum(axis=0))

def calculate_weighted_values(norm_values, weights):
    return norm_values * weights

def calculate_ideal_best_worst(weighted_values, impacts):
    ideal_best = [weighted_values.iloc[:, i].max() if impacts[i] == '+' else weighted_values.iloc[:, i].min() for i in range(weighted_values.shape[1])]
    ideal_worst = [weighted_values.iloc[:, i].min() if impacts[i] == '+' else weighted_values.iloc[:, i].max() for i in range(weighted_values.shape[1])]
    return ideal_best, ideal_worst

def calculate_distances(weighted_values, ideal_best, ideal_worst):
    dist_best = np.sqrt(((weighted_values - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_values - ideal_worst) ** 2).sum(axis=1))
    return dist_best, dist_worst

def calculate_topsis_score(dist_best, dist_worst):
    return dist_worst / (dist_best + dist_worst)

def add_scores_and_rank(data, scores):
    data['Topsis Score'] = scores
    data['Rank'] = scores.rank(ascending=False).astype(int)
    return data

def save_output_file(data, output_file):
    data.to_csv(output_file, index=False)

def topsis(input_file, weights, impacts, output_file):
    try:
        data = read_input_file(input_file)
        names = data.iloc[:, 0]
        values = data.iloc[:, 1:]
        weights, impacts = validate_input(data, weights, impacts)
        norm_values = normalize_data(values)
        weighted_values = calculate_weighted_values(norm_values, weights)
        ideal_best, ideal_worst = calculate_ideal_best_worst(weighted_values, impacts)
        dist_best, dist_worst = calculate_distances(weighted_values, ideal_best, ideal_worst)
        scores = calculate_topsis_score(dist_best, dist_worst)
        result_data = add_scores_and_rank(data, scores)
        save_output_file(result_data, output_file)
        print(f"Output file saved as: {output_file}")
    except FileNotFoundError:
        print("Error: Input file not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
    else:
        _, input_file, weights, impacts, output_file = sys.argv
        topsis(input_file, weights, impacts, output_file)
