import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer as TfidfVec
from sklearn.metrics.pairwise import cosine_similarity

class KnowledgeGraphRecommender:
    def __init__(self):
        self.item_mapping = {}
        self.reverse_item_mapping = {}
        self.item_similarity = None
        self.ratings = None
        self.all_items = None

    def fit(self, df):
        self.ratings = df.copy()
        self.all_items = df['item_id'].unique()
        self.item_mapping = {iid: i for i, iid in enumerate(self.all_items)}
        self.reverse_item_mapping = {i: iid for iid, i in self.item_mapping.items()}

        n_items = len(self.all_items)
        property_matrix = np.zeros((n_items, n_items))

        item_props = {}
        for _, row in df.iterrows():
            iid = row['item_id']
            if iid not in item_props:
                props = []
                if 'genre' in df.columns and pd.notna(row.get('genre')):
                    props.append(str(row['genre']))
                if 'description' in df.columns and pd.notna(row.get('description')):
                    props.append(str(row['description']))
                if 'title' in df.columns and pd.notna(row.get('title')):
                    props.append(str(row['title']))
                item_props[iid] = ' '.join(props) if props else f'item_{iid}'

        item_texts = []
        for iid in self.all_items:
            item_texts.append(item_props.get(iid, f'item_{iid}'))

        if len(set(item_texts)) > 1:
            vec = TfidfVec(stop_words='english', max_features=100)
            tfidf_matrix = vec.fit_transform(item_texts)
            text_sim = cosine_similarity(tfidf_matrix)
        else:
            text_sim = np.eye(n_items)

        genre_sim = np.eye(n_items)
        if 'genre' in df.columns:
            genre_data = df[['item_id', 'genre']].drop_duplicates('item_id').set_index('item_id')
            genre_dummies = genre_data['genre'].fillna('').str.get_dummies(sep=',')
            genre_matrix = np.zeros((n_items, genre_dummies.shape[1]))
            for i, iid in enumerate(self.all_items):
                if iid in genre_dummies.index:
                    genre_matrix[i] = genre_dummies.loc[iid].values
            genre_sim = cosine_similarity(genre_matrix)

        title_sim = np.eye(n_items)
        if 'title' in df.columns:
            title_data = df[['item_id', 'title']].drop_duplicates('item_id').set_index('item_id')
            title_vec = TfidfVec(stop_words='english', analyzer='char_wb', ngram_range=(2, 4), max_features=50)
            titles = []
            for iid in self.all_items:
                if iid in title_data.index:
                    titles.append(str(title_data.loc[iid, 'title']) or '')
                else:
                    titles.append('')
            try:
                title_tfidf = title_vec.fit_transform(titles)
                title_sim = cosine_similarity(title_tfidf)
            except Exception:
                title_sim = np.eye(n_items)

        self.item_similarity = 0.4 * text_sim + 0.3 * genre_sim + 0.3 * title_sim

    def recommend(self, user_id, n=10):
        user_data = self.ratings[self.ratings['user_id'] == user_id]
        if len(user_data) == 0:
            return []

        scores = np.zeros(len(self.all_items))

        for _, row in user_data.iterrows():
            if row['item_id'] in self.item_mapping:
                idx = self.item_mapping[row['item_id']]
                scores += row['rating'] * self.item_similarity[idx]

        rated_indices = [self.item_mapping[row['item_id']] for _, row in user_data.iterrows() if row['item_id'] in self.item_mapping]
        scores[rated_indices] = -1

        top_indices = np.argsort(scores)[::-1][:n]
        return [self.reverse_item_mapping[idx] for idx in top_indices if scores[idx] > 0]
