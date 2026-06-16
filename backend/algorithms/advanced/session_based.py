import numpy as np
import pandas as pd
from collections import defaultdict

class SessionBasedRecommender:
    def __init__(self, window_size=3):
        self.window_size = window_size
        self.cooccurrence = defaultdict(lambda: defaultdict(float))
        self.item_mapping = {}
        self.reverse_item_mapping = {}
        self.item_popularity = defaultdict(float)
        self.ratings = None

    def fit(self, df):
        self.ratings = df.copy()
        unique_items = df['item_id'].unique()

        self.item_mapping = {iid: i for i, iid in enumerate(unique_items)}
        self.reverse_item_mapping = {i: iid for iid, i in self.item_mapping.items()}

        for uuid in self.item_mapping:
            self.item_popularity[uuid] = 0.0

        if 'timestamp' in df.columns:
            df_sorted = df.sort_values(['user_id', 'timestamp'])
        else:
            df_sorted = df.sort_values('user_id')

        for user_id, group in df_sorted.groupby('user_id'):
            items = group['item_id'].tolist()
            for i, item in enumerate(items):
                self.item_popularity[item] += 1.0
                window_start = max(0, i - self.window_size)
                for j in range(window_start, i):
                    neighbor = items[j]
                    if neighbor != item:
                        self.cooccurrence[item][neighbor] += 1.0

        for item in self.item_mapping:
            total = sum(self.cooccurrence[item].values())
            if total > 0:
                for neighbor in self.cooccurrence[item]:
                    self.cooccurrence[item][neighbor] /= total

        if not any(self.item_popularity.values()):
            for item in unique_items:
                self.item_popularity[item] = 1.0

    def recommend(self, user_id, n=10):
        if user_id not in self.ratings['user_id'].values:
            return []
        user_data = self.ratings[self.ratings['user_id'] == user_id]
        if len(user_data) == 0:
            popular = sorted(self.item_popularity.items(), key=lambda x: x[1], reverse=True)
            return [item_id for item_id, _ in popular[:n]]

        user_items = user_data['item_id'].tolist()
        scores = defaultdict(float)

        for item in user_items:
            if item in self.cooccurrence:
                for neighbor, prob in self.cooccurrence[item].items():
                    scores[neighbor] += prob

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        result = []
        seen = set(user_items)
        for item_id, score in ranked:
            if item_id not in seen:
                result.append(item_id)
                seen.add(item_id)
            if len(result) >= n:
                break

        if len(result) < n:
            popular = sorted(self.item_popularity.items(), key=lambda x: x[1], reverse=True)
            for item_id, _ in popular:
                if item_id not in seen:
                    result.append(item_id)
                    seen.add(item_id)
                if len(result) >= n:
                    break

        return result[:n]
