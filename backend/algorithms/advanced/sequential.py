import numpy as np
import pandas as pd
from collections import defaultdict

class SequentialRecommender:
    def __init__(self, order=1):
        self.order = order
        self.transition_matrix = defaultdict(lambda: defaultdict(float))
        self.item_mapping = {}
        self.reverse_item_mapping = {}
        self.item_counts = defaultdict(float)
        self.ratings = None
        self.user_sequences = defaultdict(list)

    def fit(self, df):
        self.ratings = df.copy()
        unique_items = df['item_id'].unique()

        self.item_mapping = {iid: i for i, iid in enumerate(unique_items)}
        self.reverse_item_mapping = {i: iid for iid, i in self.item_mapping.items()}

        if 'timestamp' in df.columns:
            df_sorted = df.sort_values(['user_id', 'timestamp'])
        else:
            df_sorted = df.sort_values('user_id')

        for user_id, group in df_sorted.groupby('user_id'):
            sequence = group['item_id'].tolist()
            self.user_sequences[user_id] = sequence

            for i in range(len(sequence)):
                self.item_counts[sequence[i]] += 1.0
                for o in range(1, self.order + 1):
                    if i >= o:
                        prev = tuple(sequence[i - o:i])
                        next_item = sequence[i]
                        self.transition_matrix[prev][next_item] += 1.0

        for prev in self.transition_matrix:
            total = sum(self.transition_matrix[prev].values())
            if total > 0:
                for item in self.transition_matrix[prev]:
                    self.transition_matrix[prev][item] /= total

        if not self.item_counts:
            for item in unique_items:
                self.item_counts[item] = 1.0

    def recommend(self, user_id, n=10):
        sequence = self.user_sequences.get(user_id, [])
        if len(sequence) == 0:
            if self.ratings is not None and user_id not in self.ratings['user_id'].values:
                return []
            popular = sorted(self.item_counts.items(), key=lambda x: x[1], reverse=True)
            return [item_id for item_id, _ in popular[:n]]

        scores = defaultdict(float)

        for o in range(1, self.order + 1):
            if len(sequence) >= o:
                prev = tuple(sequence[-o:])
                if prev in self.transition_matrix:
                    for item, prob in self.transition_matrix[prev].items():
                        scores[item] += prob * (1.0 / o)

        if not scores:
            popular = sorted(self.item_counts.items(), key=lambda x: x[1], reverse=True)
            return [item_id for item_id, _ in popular[:n]]

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        result = []
        seen = set(sequence)
        for item_id, score in ranked:
            if item_id not in seen:
                result.append(item_id)
                seen.add(item_id)
            if len(result) >= n:
                break

        if len(result) < n:
            popular = sorted(self.item_counts.items(), key=lambda x: x[1], reverse=True)
            for item_id, _ in popular:
                if item_id not in seen:
                    result.append(item_id)
                    seen.add(item_id)
                if len(result) >= n:
                    break

        return result[:n]
