import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, result_file):

    if input_file.endswith('.csv'):
        data = pd.read_csv(input_file)
    elif input_file.endswith('.xlsx'):
        data = pd.read_excel(input_file, engine='openpyxl')
    else:
        print("Invalid file format. Only CSV and Excel are supported.")
        return

    if data.shape[1] < 3:
        print("Input file must have at least three columns.")
        return

    if not all(data.iloc[:, 1:].apply(lambda x: np.isreal(x)).all(axis=0)):
        print("All columns except the first one must contain numeric values.")
        return

    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    if len(weights) != len(impacts) or len(weights) != data.shape[1] - 1:
        print("Number of weights and impacts must match the number of numeric columns.")
        return
    

    if not all(i in ['+', '-'] for i in impacts):
        print("Impacts must be either '+' or '-'.")
        return


    decision_matrix = data.iloc[:, 1:].values
    norm_matrix = np.zeros_like(decision_matrix, dtype=float)

    for col in range(decision_matrix.shape[1]):
        column_sum = 0
        for row in range(decision_matrix.shape[0]):
            column_sum += decision_matrix[row, col] ** 2
        column_sqrt = column_sum ** 0.5
        for row in range(decision_matrix.shape[0]):
            norm_matrix[row, col] = decision_matrix[row, col] / column_sqrt

    weighted_matrix = np.zeros_like(norm_matrix, dtype=float)

    for i in range(norm_matrix.shape[1]):
        for j in range(norm_matrix.shape[0]):
            weighted_matrix[j, i] = norm_matrix[j, i] * weights[i]

    ideal_best = []
    ideal_worst = []

    for i, impact in enumerate(impacts):
        if impact == '+':
            best = max(weighted_matrix[:, i])
            worst = min(weighted_matrix[:, i])
        else:
            best = min(weighted_matrix[:, i])
            worst = max(weighted_matrix[:, i])

        ideal_best.append(best)
        ideal_worst.append(worst)

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = []
    dist_worst = []

    for i in range(weighted_matrix.shape[0]):
        best_dist = 0
        worst_dist = 0
        for j in range(weighted_matrix.shape[1]):
            best_dist += (weighted_matrix[i, j] - ideal_best[j]) ** 2
            worst_dist += (weighted_matrix[i, j] - ideal_worst[j]) ** 2
        dist_best.append(best_dist ** 0.5)
        dist_worst.append(worst_dist ** 0.5)

    scores = []
    for i in range(len(dist_best)):
        score = dist_worst[i] / (dist_best[i] + dist_worst[i])
        scores.append(score)

    ranks = sorted(range(len(scores)), key=lambda x: scores[x], reverse=True)
    ranks = [ranks.index(i) + 1 for i in range(len(scores))]


    data['Topsis Score'] = scores
    data['Rank'] = ranks

    data.to_excel(result_file, index=False)
    print(f"Results saved to {result_file}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Format: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
    else:
        _, input_file, weights, impacts, result_file = sys.argv
        topsis(input_file, weights, impacts, result_file)
