import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

class StackingRecommender:
    def __init__(self, base_models=None):
        self.base_models = base_models or []
        self.meta_model = LogisticRegression(max_iter=500, random_state=42)
        self.item_mapping = {}
        self.reverse_item_mapping = {}
        self.all_items = None
        self.ratings = None
        self.user_encoder = LabelEncoder()
        self.item_encoder = LabelEncoder()

    def fit(self, df):
        self.ratings = df.copy()
        self.all_items = df['item_id'].unique()
        self.item_mapping = {iid: i for i, iid in enumerate(self.all_items)}
        self.reverse_item_mapping = {i: iid for iid, i in self.item_mapping.items()}

        for model in self.base_models:
            model.fit(df)

        self.user_encoder.fit(df['user_id'])
        self.item_encoder.fit(df['item_id'])

        meta_X = []
        meta_y = []
        for _, row in df.iterrows():
            features = []
            for model in self.base_models:
                pred = self._predict_single(model, row['user_id'], row['item_id'])
                features.append(pred)
            meta_X.append(features)
            meta_y.append(int(row['item_id'] in self.item_mapping and self.item_mapping[row['item_id']]))

        if len(np.unique(meta_y)) > 1 and len(meta_X) > 10:
            self.meta_model.fit(meta_X, meta_y)

    def _predict_single(self, model, user_id, item_id):
        try:
            recs = model.recommend(user_id, n=len(self.all_items))
            if item_id in recs:
                return 1.0 / (recs.index(item_id) + 1)
            return 0.0
        except Exception:
            return 0.0

    def recommend(self, user_id, n=10):
        if len(self.base_models) == 0:
            return []
        if user_id not in self.ratings['user_id'].values:
            return []

        n_items = len(self.all_items)
        scores = np.zeros(n_items)

        for idx, item_id in self.reverse_item_mapping.items():
            features = []
            for model in self.base_models:
                pred = self._predict_single(model, user_id, item_id)
                features.append(pred)

            if hasattr(self.meta_model, 'classes_') and len(self.meta_model.classes_) > 1:
                probs = self.meta_model.predict_proba([features])[0]
                if len(probs) > 1:
                    scores[idx] = probs[1]
                else:
                    scores[idx] = np.mean(features)
            else:
                scores[idx] = np.mean(features)

        user_data = self.ratings[self.ratings['user_id'] == user_id]
        rated_indices = [self.item_mapping[row['item_id']] for _, row in user_data.iterrows() if row['item_id'] in self.item_mapping]
        scores[rated_indices] = -1

        top_indices = np.argsort(scores)[::-1][:n]
        return [self.reverse_item_mapping[idx] for idx in top_indices if scores[idx] > 0]
