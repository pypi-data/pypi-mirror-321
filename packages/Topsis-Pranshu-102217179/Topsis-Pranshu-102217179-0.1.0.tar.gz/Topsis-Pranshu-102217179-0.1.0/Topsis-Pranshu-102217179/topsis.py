import pandas as pd
import numpy as np
import sys


def calculate_topsis(input_file, weight_factors, impact_types, result_file):
    try:
        data_frame = pd.read_csv(input_file)

        if data_frame.shape[1] < 3:
            print("Error: The input file should have at least three columns.")
            return

        if not np.issubdtype(data_frame.iloc[:, 1:].dtypes.values[0], np.number):
            print("Error: The columns from the second to the last should contain numeric values.")
            return

        weight_factors = [float(w) for w in weight_factors.split(",")]
        impact_types = impact_types.split(",")

        if len(weight_factors) != (data_frame.shape[1] - 1) or len(impact_types) != (data_frame.shape[1] - 1):
            print("Error: The number of weights or impacts does not match the number of columns.")
            return
        if not all(i in ['+', '-'] for i in impact_types):
            print("Error: The impact types should be either '+' or '-'.")
            return

        decision_matrix = data_frame.iloc[:, 1:].values
        for column in range(decision_matrix.shape[1]):
            norm_value = (sum(decision_matrix[:, column] ** 2)) ** 0.5
            decision_matrix[:, column] /= norm_value

        for column in range(decision_matrix.shape[1]):
            decision_matrix[:, column] *= weight_factors[column]

        ideal_best = [max(decision_matrix[:, column]) if impact_types[column] == '+' else min(decision_matrix[:, column]) for column in
                      range(decision_matrix.shape[1])]
        ideal_worst = [min(decision_matrix[:, column]) if impact_types[column] == '+' else max(decision_matrix[:, column]) for column in
                       range(decision_matrix.shape[1])]

        distance_best = ((decision_matrix - ideal_best) ** 2).sum(axis=1) ** 0.5
        distance_worst = ((decision_matrix - ideal_worst) ** 2).sum(axis=1) ** 0.5

        scores = distance_worst / (distance_best + distance_worst)

        data_frame['Topsis Score'] = scores
        data_frame['Rank'] = pd.Series(scores).rank(ascending=False).astype(int)

        data_frame.to_csv(result_file, index=False)
        print(f"Results saved to {result_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        print("Example: python 102217179.py 102217179-data.csv \"1,1,1,1,1,1\" \"+,+,+,+,+,+\" 102217179-result.csv")
        sys.exit()

    input_file = sys.argv[1]
    weight_factors = sys.argv[2]
    impact_types = sys.argv[3]
    result_file = sys.argv[4]

    calculate_topsis(input_file, weight_factors, impact_types, result_file)
