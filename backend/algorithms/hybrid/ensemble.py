import numpy as np
import pandas as pd

class EnsembleRecommender:
    def __init__(self, models=None):
        self.models = models or []
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

    def recommend(self, user_id, n=10):
        if len(self.models) == 0:
            return []

        n_items = len(self.all_items)
        vote_counts = np.zeros(n_items)

        for model in self.models:
            try:
                recs = model.recommend(user_id, n=n)
                for rank, item_id in enumerate(recs):
                    if item_id in self.item_mapping:
                        idx = self.item_mapping[item_id]
                        vote_counts[idx] += 1
            except Exception:
                continue

        user_data = self.ratings[self.ratings['user_id'] == user_id]
        rated_indices = [self.item_mapping[row['item_id']] for _, row in user_data.iterrows() if row['item_id'] in self.item_mapping]
        vote_counts[rated_indices] = -1

        top_indices = np.argsort(vote_counts)[::-1][:n]
        return [self.reverse_item_mapping[idx] for idx in top_indices if vote_counts[idx] > 0]
