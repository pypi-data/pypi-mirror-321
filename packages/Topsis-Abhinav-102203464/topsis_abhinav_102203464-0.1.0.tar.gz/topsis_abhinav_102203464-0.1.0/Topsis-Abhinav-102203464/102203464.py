import sys
import numpy as np
import pandas as pd


class Topsis:
    def __init__(self, input_file, weights, impacts, result_file):
        self.input_file = input_file
        self.weights = weights
        self.impacts = impacts
        self.result_file = result_file
        self.data = None
        self.normalized_matrix = None
        self.weighted_matrix = None
        self.ideal_best = None
        self.ideal_worst = None
        self.scores = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.input_file)
            if self.data.shape[1] < 3:
                raise ValueError("The file must have at least three columns.")
        except FileNotFoundError:
            print(f"Error: The file '{self.input_file}' was not found.")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def validate_inputs(self):
        try:
            self.weights = list(map(float, self.weights.split(',')))
            self.impacts = self.impacts.split(',')
            if len(self.weights) != self.data.shape[1] - 1 or len(self.impacts) != self.data.shape[1] - 1:
                raise ValueError("Mismatch in the number of weights and impacts with the criteria.")
            if not all(impact in ['+', '-'] for impact in self.impacts):
                raise ValueError("Impacts must be '+' or '-'.")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def normalize_data(self):
        matrix = self.data.iloc[:, 1:].values
        self.normalized_matrix = matrix / np.sqrt((matrix ** 2).sum(axis=0))

    def calculate_weighted_matrix(self):
        self.weighted_matrix = self.normalized_matrix * self.weights

    def compute_ideal_values(self):
        self.ideal_best = []
        self.ideal_worst = []
        for i, impact in enumerate(self.impacts):
            if impact == '+':
                self.ideal_best.append(self.weighted_matrix[:, i].max())
                self.ideal_worst.append(self.weighted_matrix[:, i].min())
            else:
                self.ideal_best.append(self.weighted_matrix[:, i].min())
                self.ideal_worst.append(self.weighted_matrix[:, i].max())
        self.ideal_best = np.array(self.ideal_best)
        self.ideal_worst = np.array(self.ideal_worst)

    def calculate_scores(self):
        distance_to_best = np.sqrt(((self.weighted_matrix - self.ideal_best) ** 2).sum(axis=1))
        distance_to_worst = np.sqrt(((self.weighted_matrix - self.ideal_worst) ** 2).sum(axis=1))
        self.scores = distance_to_worst / (distance_to_best + distance_to_worst)

    def rank_alternatives(self):
        self.data['Topsis Score'] = self.scores
        self.data['Rank'] = self.scores.argsort()[::-1].argsort() + 1

    def save_to_file(self):
        self.data.to_csv(self.result_file, index=False)
        print(f"Results saved in '{self.result_file}'.")

    def execute(self):
        self.load_data()
        self.validate_inputs()
        self.normalize_data()
        self.calculate_weighted_matrix()
        self.compute_ideal_values()
        self.calculate_scores()
        self.rank_alternatives()
        self.save_to_file()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <InputFile> <Weights> <Impacts> <ResultFile>")
        sys.exit(1)

    topsis = Topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    topsis.execute()
