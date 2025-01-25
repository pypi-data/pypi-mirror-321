import sys
import pandas as pd
import numpy as np


def load_data(input_file):
    try:
        data = pd.read_csv(input_file)
        if data.shape[1] < 3:
            raise ValueError("Input file must contain at least three columns.")
        return data
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def validate_weights_and_impacts(weights, impacts, num_criteria):
    try:
        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')
        if len(weights) != num_criteria or len(impacts) != num_criteria:
            raise ValueError("Invalid number of weights and impacts")
        if not all(impact in ['+', '-'] for impact in impacts):
            raise ValueError("Impacts must be '+' or '-'.")
        return weights, impacts
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def normalize_matrix(data):
    decision_matrix = data.iloc[:, 1:].values
    normalized_matrix = decision_matrix / np.sqrt((decision_matrix**2).sum(axis=0))
    return normalized_matrix


def apply_weights(normalized_matrix, weights):
    return normalized_matrix * weights


def calculate_ideal_values(weighted_matrix, impacts):
    ideal_best = []
    ideal_worst = []
    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted_matrix[:, i].max())
            ideal_worst.append(weighted_matrix[:, i].min())
        else:
            ideal_best.append(weighted_matrix[:, i].min())
            ideal_worst.append(weighted_matrix[:, i].max())
    return np.array(ideal_best), np.array(ideal_worst)


def calculate_distances(weighted_matrix, ideal_best, ideal_worst):
    distances_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    distances_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))
    return distances_best, distances_worst


def calculate_topsis_scores(distances_best, distances_worst):
    scores = distances_worst / (distances_best + distances_worst)
    return scores


def rank_alternatives(data, scores):
    data['Topsis Score'] = scores
    data['Rank'] = scores.argsort()[::-1].argsort() + 1
    return data


def save_results(data, result_file):
    data.to_csv(result_file, index=False)
    print(f"Results saved to '{result_file}'.")


def main():
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <InputFile> <Weights> <Impacts> <ResultFile>")
        sys.exit(1)
    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result_file = sys.argv[4]


    data = load_data(input_file)

    weights, impacts = validate_weights_and_impacts(weights, impacts, data.shape[1] - 1)

    normalized_matrix = normalize_matrix(data)

    weighted_matrix = apply_weights(normalized_matrix, weights)

    ideal_best, ideal_worst = calculate_ideal_values(weighted_matrix, impacts)

    distances_best, distances_worst = calculate_distances(weighted_matrix, ideal_best, ideal_worst)

    scores = calculate_topsis_scores(distances_best, distances_worst)

    result_data = rank_alternatives(data, scores)
    save_results(result_data, result_file)


if __name__ == "__main__":
    main()
