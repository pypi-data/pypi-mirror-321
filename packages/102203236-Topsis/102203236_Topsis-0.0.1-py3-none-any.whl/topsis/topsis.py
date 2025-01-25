import pandas as pd
import numpy as np

class Topsis:
    def __init__(self, filename, impacts, weights):
        self.filename = filename
        self.impacts = impacts
        self.weights = weights
        self.df = pd.read_excel(filename)  # Load data
        
        self.process_topsis()  # Automatically run TOPSIS
    
    def data_eng(self, file):
        return pd.get_dummies(file)

    def normalising(self, file):
        norm_factors = np.sqrt((file**2).sum(axis=0))
        return file / norm_factors

    def apply_weights(self, file):
        return file * self.weights

    def best_worst(self, file):
        s_best, s_worst = [], []
        for i, impact in enumerate(self.impacts):
            if impact == '+':
                s_best.append(file.iloc[:, i].max())
                s_worst.append(file.iloc[:, i].min())
            else:
                s_best.append(file.iloc[:, i].min())
                s_worst.append(file.iloc[:, i].max())
        return s_best, s_worst

    def calculate_distances(self, file, s_best, s_worst):
        best_dist = np.sqrt(((file - s_best) ** 2).sum(axis=1))
        worst_dist = np.sqrt(((file - s_worst) ** 2).sum(axis=1))
        return best_dist, worst_dist

    def performance_score(self, best_dist, worst_dist):
        scores = worst_dist / (best_dist + worst_dist)
        self.df['Score'] = scores
        self.df.sort_values('Score', ascending=False, inplace=True)
        self.df['Rank'] = range(1, len(scores) + 1)

    def process_topsis(self):
        file = self.data_eng(file)
        file = self.normalising(file)
        file = self.apply_weights(file)
        s_best, s_worst = self.best_worst(file)
        best_dist, worst_dist = self.calculate_distances(file, s_best, s_worst)
        self.performance_score(best_dist, worst_dist)  # Store result in self.df

    def get_result(self):
        return self.df  # Retrieve the final ranked DataFrame
