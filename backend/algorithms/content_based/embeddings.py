import numpy as np
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

class EmbeddingRecommender:
    def __init__(self, n_components=20):
        self.n_components = n_components
        self.svd = None
        self.item_embeddings = None
        self.item_mapping = {}
        self.reverse_item_mapping = {}
        self.ratings = None

    def fit(self, df):
        self.ratings = df.copy()
        unique_items = df['item_id'].unique()

        self.item_mapping = {iid: i for i, iid in enumerate(unique_items)}
        self.reverse_item_mapping = {i: iid for iid, i in self.item_mapping.items()}

        n_items = len(unique_items)

        if 'genre' in df.columns:
            item_genres = df[['item_id', 'genre']].drop_duplicates('item_id').set_index('item_id')
            all_genres = item_genres['genre'].fillna('').str.get_dummies(sep=',')
            feature_matrix = np.zeros((n_items, all_genres.shape[1]))
            for i, iid in enumerate(unique_items):
                if iid in all_genres.index:
                    feature_matrix[i] = all_genres.loc[iid].values
        else:
            feature_matrix = np.eye(n_items)

        if feature_matrix.shape[1] < 2:
            feature_matrix = np.eye(n_items)

        sim_matrix = cosine_similarity(feature_matrix)

        n_components = min(self.n_components, sim_matrix.shape[0] - 1, sim_matrix.shape[1] - 1)
        n_components = max(1, n_components)

        self.svd = TruncatedSVD(n_components=n_components, random_state=42)
        self.item_embeddings = self.svd.fit_transform(sim_matrix)

    def recommend(self, user_id, n=10):
        user_data = self.ratings[self.ratings['user_id'] == user_id]
        if len(user_data) == 0:
            return []

        user_embedding = np.zeros(self.item_embeddings.shape[1])
        total_weight = 0.0

        for _, row in user_data.iterrows():
            if row['item_id'] in self.item_mapping:
                idx = self.item_mapping[row['item_id']]
                user_embedding += row['rating'] * self.item_embeddings[idx]
                total_weight += abs(row['rating'])

        if total_weight == 0:
            return []

        user_embedding /= total_weight

        scores = cosine_similarity(self.item_embeddings, user_embedding.reshape(1, -1)).flatten()

        rated_indices = [self.item_mapping[row['item_id']] for _, row in user_data.iterrows() if row['item_id'] in self.item_mapping]
        scores[rated_indices] = -1

        top_indices = np.argsort(scores)[::-1][:n]
        return [self.reverse_item_mapping[idx] for idx in top_indices if scores[idx] > 0]
