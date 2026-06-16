import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPRegressor

class NeuralCF:
    def __init__(self):
        self.user_encoder = LabelEncoder()
        self.item_encoder = LabelEncoder()
        self.gmf_model = None
        self.mlp_model = None
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

        user_encoded = self.user_encoder.fit_transform(df['user_id'])
        item_encoded = self.item_encoder.fit_transform(df['item_id'])

        n_users = len(self.unique_users)
        n_items = len(self.unique_items)

        user_norm = user_encoded / max(1, n_users - 1)
        item_norm = item_encoded / max(1, n_items - 1)

        X_gmf = np.column_stack([user_norm, item_norm])
        X_mlp = np.column_stack([user_norm, item_norm, user_norm * item_norm])
        y = df['rating'].values

        self.gmf_model = MLPRegressor(
            hidden_layer_sizes=(16, 8),
            activation='relu',
            solver='adam',
            max_iter=200,
            random_state=42
        )
        self.gmf_model.fit(X_gmf, y)

        self.mlp_model = MLPRegressor(
            hidden_layer_sizes=(64, 32, 16),
            activation='relu',
            solver='adam',
            max_iter=200,
            random_state=42
        )
        self.mlp_model.fit(X_mlp, y)

    def recommend(self, user_id, n=10):
        if user_id not in self.user_mapping:
            return []

        user_idx = self.user_mapping[user_id]
        user_enc = self.user_encoder.transform([user_id])[0]
        n_users = len(self.unique_users)
        n_items = len(self.unique_items)

        user_norm = user_enc / max(1, n_users - 1)
        item_norms = self.item_encoder.transform(self.unique_items) / max(1, n_items - 1)

        predictions = np.zeros(len(self.unique_items))
        for i, item_norm in enumerate(item_norms):
            X_g = np.array([[user_norm, item_norm]])
            X_m = np.array([[user_norm, item_norm, user_norm * item_norm]])
            pred_g = self.gmf_model.predict(X_g)[0]
            pred_m = self.mlp_model.predict(X_m)[0]
            predictions[i] = 0.5 * pred_g + 0.5 * pred_m

        item_score_pairs = list(zip(self.unique_items, predictions))
        item_score_pairs.sort(key=lambda x: x[1], reverse=True)

        return [item_id for item_id, score in item_score_pairs[:n]]
