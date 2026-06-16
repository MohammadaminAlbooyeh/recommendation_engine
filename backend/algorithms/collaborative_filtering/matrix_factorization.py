import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

class MatrixFactorization:
    def __init__(self):
        self.user_item_matrix = None
        self.item_similarity_matrix = None
        self.user_mapping = {}
        self.item_mapping = {}
        self.reverse_item_mapping = {}

    def fit(self, df):
        # Create user and item mappings
        unique_users = df['user_id'].unique()
        unique_items = df['item_id'].unique()
        
        self.user_mapping = {id: i for i, id in enumerate(unique_users)}
        self.item_mapping = {id: i for i, id in enumerate(unique_items)}
        self.reverse_item_mapping = {i: id for id, i in self.item_mapping.items()}
        
        # Create sparse matrix
        rows = df['user_id'].map(self.user_mapping)
        cols = df['item_id'].map(self.item_mapping)
        values = df['rating']
        
        self.user_item_matrix = csr_matrix((values, (rows, cols)), shape=(len(unique_users), len(unique_items)))
        
        # Compute item-item similarity
        self.item_similarity_matrix = cosine_similarity(self.user_item_matrix.T, dense_output=False)

    def recommend(self, user_id, n=10):
        if user_id not in self.user_mapping:
            return []
        
        user_idx = self.user_mapping[user_id]
        user_ratings = self.user_item_matrix[user_idx].toarray().flatten()
        
        # Simple collaborative filtering prediction: Weighted average of similarities
        # scores = similarity_matrix * user_ratings
        scores = self.item_similarity_matrix.dot(user_ratings)
        
        # Filter out already rated items
        already_rated = np.where(user_ratings > 0)[0]
        scores[already_rated] = -1
        
        # Get top N items
        top_indices = np.argsort(scores)[::-1][:n]
        
        return [self.reverse_item_mapping[idx] for idx in top_indices if scores[idx] > 0]
