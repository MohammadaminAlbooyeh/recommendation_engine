import numpy as np
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import Optional


def generate_svd_embeddings(df: pd.DataFrame, n_components: int = 20) -> np.ndarray:
    pivot = df.pivot_table(index="user_id", columns="item_id", values="rating").fillna(0)
    svd = TruncatedSVD(n_components=min(n_components, min(pivot.shape) - 1), random_state=42)
    return svd.fit_transform(pivot)


def generate_tfidf_embeddings(texts: list, max_features: int = 100) -> np.ndarray:
    vectorizer = TfidfVectorizer(max_features=max_features, stop_words="english")
    return vectorizer.fit_transform(texts).toarray()


def generate_item_embeddings_from_genres(df: pd.DataFrame, n_components: int = 10) -> np.ndarray:
    genre_dummies = df["genre"].str.get_dummies(sep=",")
    svd = TruncatedSVD(n_components=min(n_components, genre_dummies.shape[1]), random_state=42)
    return svd.fit_transform(genre_dummies)


def normalize_embeddings(embeddings: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    norms = np.maximum(norms, 1e-10)
    return embeddings / norms
