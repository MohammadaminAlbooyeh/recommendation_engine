import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

class ItemBasedCF:
    def __init__(self):
        self.user_item_matrix = None
        self.item_similarity_matrix = None
        self.user_mapping = {}
        self.item_mapping = {}
        self.reverse_item_mapping = {}

    def fit(self, df):
        unique_users = df['user_id'].unique()
        unique_items = df['item_id'].unique()

        self.user_mapping = {uid: i for i, uid in enumerate(unique_users)}
        self.item_mapping = {iid: j for j, iid in enumerate(unique_items)}
        self.reverse_item_mapping = {j: iid for iid, j in self.item_mapping.items()}

        rows = df['user_id'].map(self.user_mapping).values
        cols = df['item_id'].map(self.item_mapping).values
        values = df['rating'].values

        n_users = len(unique_users)
        n_items = len(unique_items)

        self.user_item_matrix = csr_matrix((values, (rows, cols)), shape=(n_users, n_items))

        self.item_similarity_matrix = cosine_similarity(self.user_item_matrix.T, dense_output=False)

    def recommend(self, user_id, n=10):
        if user_id not in self.user_mapping:
            return []

        user_idx = self.user_mapping[user_id]
        user_ratings = self.user_item_matrix[user_idx].toarray().flatten()

        scores = self.item_similarity_matrix.dot(user_ratings)

        already_rated = np.where(user_ratings > 0)[0]
        scores[already_rated] = -1

        top_indices = np.argsort(scores)[::-1][:n]
        return [self.reverse_item_mapping[idx] for idx in top_indices if scores[idx] > 0]
