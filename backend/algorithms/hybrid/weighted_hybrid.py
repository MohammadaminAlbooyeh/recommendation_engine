import numpy as np
import pandas as pd

class WeightedHybrid:
    def __init__(self, models=None, weights=None):
        self.models = models or []
        self.weights = weights or []
        self.item_mapping = {}
        self.reverse_item_mapping = {}
        self.all_items = None
        self.ratings = None

    def fit(self, df):
        self.ratings = df.copy()
        self.all_items = df['item_id'].unique()
        self.item_mapping = {iid: i for i, iid in enumerate(self.all_items)}
        self.reverse_item_mapping = {i: iid for iid, i in self.item_mapping.items()}

        for model in self.models:
            model.fit(df)

        if not self.weights:
            self.weights = [1.0 / len(self.models)] * len(self.models)

    def recommend(self, user_id, n=10):
        if len(self.models) == 0:
            return []

        n_items = len(self.all_items)
        combined_scores = np.zeros(n_items)

        for i, model in enumerate(self.models):
            try:
                recs = model.recommend(user_id, n=n_items)
                for rank, item_id in enumerate(recs):
                    if item_id in self.item_mapping:
                        idx = self.item_mapping[item_id]
                        combined_scores[idx] += self.weights[i] * (1.0 / (rank + 1))
            except Exception:
                continue

        user_data = self.ratings[self.ratings['user_id'] == user_id]
        rated_indices = [self.item_mapping[row['item_id']] for _, row in user_data.iterrows() if row['item_id'] in self.item_mapping]
        combined_scores[rated_indices] = -1

        top_indices = np.argsort(combined_scores)[::-1][:n]
        return [self.reverse_item_mapping[idx] for idx in top_indices if combined_scores[idx] > 0]
