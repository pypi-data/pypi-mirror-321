import pandas as pd
import numpy as np
import sys


def process_inputs(dataframe, weight_str, impact_str):
    if dataframe.shape[1] < 3:
        raise ValueError("The input file must contain at least three columns.")
    try:
        weight_list = [float(w) for w in weight_str.split(',')]
        impact_list = impact_str.split(',')
    except ValueError:
        raise ValueError("Weights must be numbers, separated by commas.")
    if len(weight_list) != len(impact_list) or len(weight_list) != dataframe.shape[1] - 1:
        raise ValueError("Mismatch in the number of weights, impacts, and numeric columns.")
    if not all(impact in ['+', '-'] for impact in impact_list):
        raise ValueError("Impacts can only be '+' or '-'.")
    return weight_list, impact_list


def compute_topsis(dataframe, weights, impacts):
    numeric_data = dataframe.iloc[:, 1:].to_numpy()
    normalization_factors = np.sqrt((numeric_data ** 2).sum(axis=0))
    normalized_data = numeric_data / normalization_factors
    weighted_data = normalized_data * weights
    ideal_best = [np.max(weighted_data[:, i]) if impacts[i] == '+' else np.min(weighted_data[:, i])
                  for i in range(len(impacts))]
    ideal_worst = [np.min(weighted_data[:, i]) if impacts[i] == '+' else np.max(weighted_data[:, i])
                   for i in range(len(impacts))]
    distance_to_best = np.sqrt(np.sum((weighted_data - ideal_best) ** 2, axis=1))
    distance_to_worst = np.sqrt(np.sum((weighted_data - ideal_worst) ** 2, axis=1))
    topsis_scores = distance_to_worst / (distance_to_best + distance_to_worst)
    dataframe['Topsis Score'] = topsis_scores
    dataframe['Rank'] = pd.Series(topsis_scores).rank(ascending=False).astype(int)
    return dataframe


def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        print("Example: python 101556.py 101556-data.csv \"1,1,1,2\" \"+,+,-,+\" 101556-result.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    try:
        data = pd.read_csv(input_file)
        processed_weights, processed_impacts = process_inputs(data, weights, impacts)
        result_data = compute_topsis(data, processed_weights, processed_impacts)
        result_data.to_csv(output_file, index=False)
        print(f"Results saved to '{output_file}'.")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
