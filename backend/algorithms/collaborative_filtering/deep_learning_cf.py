import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPRegressor

class DeepLearningCF:
    def __init__(self):
        self.user_encoder = LabelEncoder()
        self.item_encoder = LabelEncoder()
        self.model = None
        self.item_mapping = {}
        self.reverse_item_mapping = {}
        self.user_mapping = {}
        self.unique_items = None
        self.unique_users = None

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

        X = np.column_stack([user_encoded / max(1, n_users - 1), item_encoded / max(1, n_items - 1)])
        y = df['rating'].values

        self.model = MLPRegressor(
            hidden_layer_sizes=(64, 32),
            activation='relu',
            solver='adam',
            max_iter=200,
            random_state=42
        )
        self.model.fit(X, y)

    def recommend(self, user_id, n=10):
        if user_id not in self.user_mapping:
            return []

        user_idx = self.user_mapping[user_id]
        user_encoded = self.user_encoder.transform([user_id])[0]
        n_users = len(self.unique_users)
        n_items = len(self.unique_items)

        rated_items = set()
        all_item_encoded = self.item_encoder.transform(self.unique_items)

        user_feat = user_encoded / max(1, n_users - 1)
        item_feats = all_item_encoded / max(1, n_items - 1)

        X_pred = np.column_stack([np.full(len(self.unique_items), user_feat), item_feats])
        predictions = self.model.predict(X_pred)

        item_score_pairs = list(zip(self.unique_items, predictions))
        item_score_pairs.sort(key=lambda x: x[1], reverse=True)

        return [item_id for item_id, score in item_score_pairs[:n]]
