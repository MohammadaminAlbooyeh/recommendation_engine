import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPRegressor
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

class TransformerCF:
    def __init__(self):
        self.user_encoder = LabelEncoder()
        self.item_encoder = LabelEncoder()
        self.attention_model = None
        self.user_item_matrix = None
        self.user_similarity = None
        self.user_mapping = {}
        self.item_mapping = {}
        self.reverse_item_mapping = {}
        self.unique_users = None
        self.unique_items = None

    def fit(self, df):
        self.unique_users = df['user_id'].unique()
        self.unique_items = df['item_id'].unique()

        self.user_mapping = {uid: i for i, uid in enumerate(self.unique_users)}
        self.item_mapping = {iid: j for j, iid in enumerate(self.unique_items)}
        self.reverse_item_mapping = {j: iid for iid, j in self.item_mapping.items()}

        rows = df['user_id'].map(self.user_mapping).values
        cols = df['item_id'].map(self.item_mapping).values
        values = df['rating'].values

        n_users = len(self.unique_users)
        n_items = len(self.unique_items)

        self.user_item_matrix = csr_matrix((values, (rows, cols)), shape=(n_users, n_items))
        self.user_similarity = cosine_similarity(self.user_item_matrix, dense_output=False)

        user_encoded = self.user_encoder.fit_transform(df['user_id'])
        item_encoded = self.item_encoder.fit_transform(df['item_id'])

        attention_features = []
        labels = []

        for _, row in df.iterrows():
            uid = row['user_id']
            iid = row['item_id']
            if uid not in self.user_mapping or iid not in self.item_mapping:
                continue

            u_idx = self.user_mapping[uid]
            i_idx = self.item_mapping[iid]

            sim_users = self.user_similarity[u_idx].toarray().flatten()
            top_k = 10
            neighbor_indices = np.argsort(sim_users)[::-1][1:top_k + 1]

            attention_weights = sim_users[neighbor_indices]
            attention_weights = attention_weights / (attention_weights.sum() + 1e-10)

            neighbor_ratings = self.user_item_matrix[neighbor_indices, i_idx].toarray().flatten()
            attended_rating = np.dot(attention_weights, neighbor_ratings)

            user_norm = user_encoded[_] / max(1, n_users - 1)
            item_norm = item_encoded[_] / max(1, n_items - 1)

            attention_features.append([
                user_norm, item_norm, attended_rating,
                sim_users[:5].mean() if len(sim_users) > 1 else 0,
                np.std(neighbor_ratings) if len(neighbor_ratings) > 0 else 0
            ])
            labels.append(row['rating'])

        if len(attention_features) > 10:
            X = np.array(attention_features)
            y = np.array(labels)

            self.attention_model = MLPRegressor(
                hidden_layer_sizes=(32, 16),
                activation='relu',
                solver='adam',
                max_iter=200,
                random_state=42
            )
            self.attention_model.fit(X, y)

    def recommend(self, user_id, n=10):
        if user_id not in self.user_mapping:
            return []

        u_idx = self.user_mapping[user_id]
        n_users = len(self.unique_users)
        n_items = len(self.unique_items)

        sim_users = self.user_similarity[u_idx].toarray().flatten()
        top_k = 10
        neighbor_indices = np.argsort(sim_users)[::-1][1:top_k + 1]
        attention_weights = sim_users[neighbor_indices]
        attention_weights = attention_weights / (attention_weights.sum() + 1e-10)

        if self.attention_model is not None:
            user_enc = self.user_encoder.transform([user_id])[0]
            user_norm = user_enc / max(1, n_users - 1)
            item_norms = self.item_encoder.transform(self.unique_items) / max(1, n_items - 1)

            scores = np.zeros(n_items)
            for i, item_norm in enumerate(item_norms):
                neighbor_ratings = self.user_item_matrix[neighbor_indices, i].toarray().flatten()
                attended_rating = np.dot(attention_weights, neighbor_ratings)
                avg_sim = sim_users[:5].mean() if len(sim_users) > 1 else 0
                std_ratings = np.std(neighbor_ratings) if len(neighbor_ratings) > 0 else 0

                features = np.array([[user_norm, item_norm, attended_rating, avg_sim, std_ratings]])
                scores[i] = self.attention_model.predict(features)[0]
        else:
            user_ratings = self.user_item_matrix[u_idx].toarray().flatten()
            scores = self.user_item_matrix.T.dot(self.user_similarity[u_idx].toarray().flatten())

        already_rated = self.user_item_matrix[u_idx].indices
        scores[already_rated] = -1

        top_indices = np.argsort(scores)[::-1][:n]
        return [self.reverse_item_mapping[idx] for idx in top_indices if scores[idx] > 0]
