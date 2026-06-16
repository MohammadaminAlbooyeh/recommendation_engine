import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

class ContextAwareRecommender:
    def __init__(self):
        self.user_item_matrix = None
        self.item_similarity_matrix = None
        self.user_mapping = {}
        self.item_mapping = {}
        self.reverse_item_mapping = {}
        self.time_weights = {}
        self.ratings = None

    def fit(self, df):
        self.ratings = df.copy()
        unique_users = df['user_id'].unique()
        unique_items = df['item_id'].unique()

        self.user_mapping = {uid: i for i, uid in enumerate(unique_users)}
        self.item_mapping = {iid: j for j, iid in enumerate(unique_items)}
        self.reverse_item_mapping = {j: iid for iid, j in self.item_mapping.items()}

        rows = df['user_id'].map(self.user_mapping).values
        cols = df['item_id'].map(self.item_mapping).values
        values = df['rating'].values

        n_users = len(unique_users)
        n_items = len(unique_items)

        self.user_item_matrix = csr_matrix((values, (rows, cols)), shape=(n_users, n_items))
        self.item_similarity_matrix = cosine_similarity(self.user_item_matrix.T, dense_output=False)

        if 'timestamp' in df.columns:
            df_ts = df.copy()
            df_ts['timestamp'] = pd.to_datetime(df_ts['timestamp'])
            df_ts['hour'] = df_ts['timestamp'].dt.hour
            df_ts['day_of_week'] = df_ts['timestamp'].dt.dayofweek

            for _, group in df_ts.groupby('day_of_week'):
                day = group['day_of_week'].iloc[0]
                mean_rating = group['rating'].mean()
                self.time_weights[f'day_{day}'] = mean_rating

            for _, group in df_ts.groupby('hour'):
                hour = group['hour'].iloc[0]
                mean_rating = group['rating'].mean()
                self.time_weights[f'hour_{hour}'] = mean_rating

    def recommend(self, user_id, n=10):
        if user_id not in self.user_mapping:
            return []

        user_idx = self.user_mapping[user_id]
        user_ratings = self.user_item_matrix[user_idx].toarray().flatten()

        scores = self.item_similarity_matrix.dot(user_ratings)

        context_bonus = np.zeros(len(self.item_mapping))
        if self.time_weights:
            avg_time_weight = np.mean(list(self.time_weights.values()))
            for i in range(len(self.item_mapping)):
                context_bonus[i] = avg_time_weight * 0.1

        scores += context_bonus

        already_rated = np.where(user_ratings > 0)[0]
        scores[already_rated] = -1

        top_indices = np.argsort(scores)[::-1][:n]
        return [self.reverse_item_mapping[idx] for idx in top_indices if scores[idx] > 0]
