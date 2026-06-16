import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentSimilarity:
    def __init__(self):
        self.item_features = None
        self.similarity_matrix = None
        self.item_mapping = {}
        self.reverse_item_mapping = {}
        self.ratings = None

    def fit(self, df):
        self.ratings = df.copy()
        unique_items = df['item_id'].unique()

        self.item_mapping = {iid: i for i, iid in enumerate(unique_items)}
        self.reverse_item_mapping = {i: iid for iid, i in self.item_mapping.items()}

        n_items = len(unique_items)
        feature_columns = []

        if 'genre' in df.columns:
            item_genres = df[['item_id', 'genre']].drop_duplicates('item_id').set_index('item_id')
            all_genres = item_genres['genre'].fillna('').str.get_dummies(sep=',')

            genre_matrix = np.zeros((n_items, all_genres.shape[1]))
            for i, iid in enumerate(unique_items):
                if iid in all_genres.index:
                    genre_matrix[i] = all_genres.loc[iid].values

            feature_columns.append(genre_matrix)

        if 'description' in df.columns:
            desc_data = df[['item_id', 'description']].drop_duplicates('item_id').set_index('item_id')
            from sklearn.feature_extraction.text import TfidfVectorizer
            tfidf = TfidfVectorizer(max_features=50, stop_words='english')
            desc_texts = []
            for iid in unique_items:
                if iid in desc_data.index:
                    desc_texts.append(desc_data.loc[iid, 'description'] or '')
                else:
                    desc_texts.append('')
            desc_matrix = tfidf.fit_transform(desc_texts).toarray()
            feature_columns.append(desc_matrix)

        if feature_columns:
            self.item_features = np.hstack(feature_columns)
        else:
            self.item_features = np.eye(n_items)

        self.similarity_matrix = cosine_similarity(self.item_features)

    def recommend(self, user_id, n=10):
        user_data = self.ratings[self.ratings['user_id'] == user_id]
        if len(user_data) == 0:
            return []

        scores = np.zeros(self.similarity_matrix.shape[0])

        for _, row in user_data.iterrows():
            if row['item_id'] in self.item_mapping:
                idx = self.item_mapping[row['item_id']]
                scores += row['rating'] * self.similarity_matrix[idx]

        rated_indices = [self.item_mapping[row['item_id']] for _, row in user_data.iterrows() if row['item_id'] in self.item_mapping]
        scores[rated_indices] = -1

        top_indices = np.argsort(scores)[::-1][:n]
        return [self.reverse_item_mapping[idx] for idx in top_indices if scores[idx] > 0]
