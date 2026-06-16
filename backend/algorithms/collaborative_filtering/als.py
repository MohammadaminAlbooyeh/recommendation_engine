import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix

class ALS:
    def __init__(self, n_factors=20, regularization=0.1, n_iterations=15):
        self.n_factors = n_factors
        self.regularization = regularization
        self.n_iterations = n_iterations
        self.user_factors = None
        self.item_factors = None
        self.user_mapping = {}
        self.item_mapping = {}
        self.reverse_item_mapping = {}
        self.rating_matrix = None

    def fit(self, df):
        unique_users = df['user_id'].unique()
        unique_items = df['item_id'].unique()

        self.user_mapping = {uid: i for i, uid in enumerate(unique_users)}
        self.item_mapping = {iid: j for j, iid in enumerate(unique_items)}
        self.reverse_item_mapping = {j: iid for iid, j in self.item_mapping.items()}

        n_users = len(unique_users)
        n_items = len(unique_items)

        rows = df['user_id'].map(self.user_mapping).values
        cols = df['item_id'].map(self.item_mapping).values
        values = df['rating'].values

        self.rating_matrix = csr_matrix((values, (rows, cols)), shape=(n_users, n_items))

        rng = np.random.RandomState(42)
        self.user_factors = rng.normal(scale=0.1, size=(n_users, self.n_factors))
        self.item_factors = rng.normal(scale=0.1, size=(n_items, self.n_factors))

        reg_I = self.regularization * np.eye(self.n_factors)
        I_dense = np.eye(self.n_factors)

        for iteration in range(self.n_iterations):
            for u in range(n_users):
                indices = self.rating_matrix[u].indices
                if len(indices) == 0:
                    continue
                values_u = self.rating_matrix[u].data
                item_subset = self.item_factors[indices]
                A = item_subset.T @ item_subset + reg_I
                b = item_subset.T @ values_u
                try:
                    self.user_factors[u] = np.linalg.solve(A, b)
                except np.linalg.LinAlgError:
                    self.user_factors[u] = np.linalg.lstsq(A, b, rcond=None)[0]

            for i in range(n_items):
                indices = self.rating_matrix[:, i].indices
                if len(indices) == 0:
                    continue
                values_i = self.rating_matrix[:, i].data
                user_subset = self.user_factors[indices]
                A = user_subset.T @ user_subset + reg_I
                b = user_subset.T @ values_i
                try:
                    self.item_factors[i] = np.linalg.solve(A, b)
                except np.linalg.LinAlgError:
                    self.item_factors[i] = np.linalg.lstsq(A, b, rcond=None)[0]

    def recommend(self, user_id, n=10):
        if user_id not in self.user_mapping:
            return []

        user_idx = self.user_mapping[user_id]
        user_vec = self.user_factors[user_idx]

        scores = self.item_factors @ user_vec

        rated_indices = self.rating_matrix[user_idx].indices
        scores[rated_indices] = -np.inf

        top_indices = np.argsort(scores)[::-1][:n]
        return [self.reverse_item_mapping[idx] for idx in top_indices if scores[idx] > -np.inf]
