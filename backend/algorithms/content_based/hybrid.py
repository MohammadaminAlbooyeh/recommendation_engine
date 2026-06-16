import numpy as np
from .tfidf_recommender import TfidfRecommender
from .embeddings import EmbeddingRecommender

class ContentBasedHybrid:
    def __init__(self, tfidf_weight=0.5, embed_weight=0.5):
        self.tfidf_weight = tfidf_weight
        self.embed_weight = embed_weight
        self.tfidf_model = TfidfRecommender()
        self.embed_model = EmbeddingRecommender()
        self.ratings = None
        self.item_mapping = {}
        self.reverse_item_mapping = {}
        self.all_items = None

    def fit(self, df):
        self.ratings = df.copy()
        self.all_items = df['item_id'].unique()
        self.item_mapping = {iid: i for i, iid in enumerate(self.all_items)}
        self.reverse_item_mapping = {i: iid for iid, i in self.item_mapping.items()}

        self.tfidf_model.fit(df)
        self.embed_model.fit(df)

    def recommend(self, user_id, n=10):
        user_data = self.ratings[self.ratings['user_id'] == user_id]
        if len(user_data) == 0:
            return []

        tfidf_scores = self._get_scores(self.tfidf_model, user_data)
        embed_scores = self._get_scores(self.embed_model, user_data)

        combined = self.tfidf_weight * tfidf_scores + self.embed_weight * embed_scores

        rated_indices = [self.item_mapping[row['item_id']] for _, row in user_data.iterrows() if row['item_id'] in self.item_mapping]
        combined[rated_indices] = -1

        top_indices = np.argsort(combined)[::-1][:n]
        return [self.reverse_item_mapping[idx] for idx in top_indices if combined[idx] > 0]

    def _get_scores(self, model, user_data):
        n_items = len(self.all_items)
        scores = np.zeros(n_items)

        for _, row in user_data.iterrows():
            if row['item_id'] in self.item_mapping:
                idx = self.item_mapping[row['item_id']]
                if hasattr(model, 'tfidf_matrix') and model.tfidf_matrix is not None:
                    from sklearn.metrics.pairwise import cosine_similarity
                    vec = model.tfidf_matrix[idx].toarray().flatten()
                    sims = cosine_similarity(model.tfidf_matrix, vec.reshape(1, -1)).flatten()
                    scores += row['rating'] * sims
                elif hasattr(model, 'item_embeddings') and model.item_embeddings is not None:
                    from sklearn.metrics.pairwise import cosine_similarity
                    sims = cosine_similarity(model.item_embeddings, model.item_embeddings[idx].reshape(1, -1)).flatten()
                    scores += row['rating'] * sims

        return scores
