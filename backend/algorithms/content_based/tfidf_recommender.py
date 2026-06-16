import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TfidfRecommender:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None
        self.item_mapping = {}
        self.reverse_item_mapping = {}
        self.item_ids = None
        self.ratings = None

    def fit(self, df):
        self.ratings = df.copy()
        unique_items = df['item_id'].unique()
        self.item_ids = unique_items
        self.item_mapping = {iid: i for i, iid in enumerate(unique_items)}
        self.reverse_item_mapping = {i: iid for iid, i in self.item_mapping.items()}

        if 'description' in df.columns:
            text_col = 'description'
        elif 'genre' in df.columns:
            text_col = 'genre'
        else:
            text_col = None

        if text_col:
            item_texts = df[['item_id', text_col]].drop_duplicates('item_id').set_index('item_id')
            missing = set(unique_items) - set(item_texts.index)
            for m in missing:
                item_texts.loc[m] = ''
            texts = item_texts.loc[unique_items][text_col].fillna('').values
        else:
            texts = np.array([f'item_{i}' for i in range(len(unique_items))])

        self.tfidf_matrix = self.vectorizer.fit_transform(texts)

    def recommend(self, user_id, n=10):
        user_data = self.ratings[self.ratings['user_id'] == user_id]
        if len(user_data) == 0:
            return []

        n_features = self.tfidf_matrix.shape[1]
        user_vector = np.zeros(n_features)
        total_weight = 0.0

        for _, row in user_data.iterrows():
            if row['item_id'] in self.item_mapping:
                idx = self.item_mapping[row['item_id']]
                user_vector += row['rating'] * self.tfidf_matrix[idx].toarray().flatten()
                total_weight += row['rating']

        if total_weight == 0:
            return []

        user_profile = user_vector / total_weight

        scores = cosine_similarity(self.tfidf_matrix, user_profile.reshape(1, -1)).flatten()

        rated_indices = [self.item_mapping[row['item_id']] for _, row in user_data.iterrows() if row['item_id'] in self.item_mapping]
        scores[rated_indices] = -1

        top_indices = np.argsort(scores)[::-1][:n]
        return [self.reverse_item_mapping[idx] for idx in top_indices if scores[idx] > 0]
