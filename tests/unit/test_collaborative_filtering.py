import pandas as pd
import numpy as np
from backend.algorithms.collaborative_filtering.matrix_factorization import MatrixFactorization

class TestMatrixFactorization:
    def test_fit_creates_matrices(self):
        df = pd.DataFrame({
            "user_id": [1, 1, 2, 2],
            "item_id": [1, 2, 1, 3],
            "rating": [5, 3, 4, 2]
        })
        mf = MatrixFactorization()
        mf.fit(df)
        assert mf.user_item_matrix is not None
        assert mf.item_similarity_matrix is not None
        assert len(mf.user_mapping) == 2
        assert len(mf.item_mapping) == 3

    def test_recommend_returns_list(self):
        df = pd.DataFrame({
            "user_id": [1, 1, 2, 2],
            "item_id": [1, 2, 1, 3],
            "rating": [5, 3, 4, 2]
        })
        mf = MatrixFactorization()
        mf.fit(df)
        recs = mf.recommend(1, n=5)
        assert isinstance(recs, list)

    def test_recommend_for_new_user_returns_empty(self):
        df = pd.DataFrame({
            "user_id": [1, 1, 2, 2],
            "item_id": [1, 2, 1, 3],
            "rating": [5, 3, 4, 2]
        })
        mf = MatrixFactorization()
        mf.fit(df)
        recs = mf.recommend(99, n=5)
        assert recs == []

    def test_recommend_excludes_rated_items(self):
        df = pd.DataFrame({
            "user_id": [1, 1, 2],
            "item_id": [1, 2, 3],
            "rating": [5, 1, 4]
        })
        mf = MatrixFactorization()
        mf.fit(df)
        recs = mf.recommend(1, n=10)
        assert 1 not in recs
        assert 2 not in recs

    def test_multiple_users_items(self):
        df = pd.DataFrame({
            "user_id": [1, 1, 1, 2, 2, 2, 3, 3, 3],
            "item_id": [1, 2, 3, 1, 2, 4, 3, 4, 5],
            "rating": [5, 4, 3, 2, 5, 4, 3, 5, 4]
        })
        mf = MatrixFactorization()
        mf.fit(df)
        recs1 = mf.recommend(1, n=5)
        recs2 = mf.recommend(2, n=5)
        recs3 = mf.recommend(3, n=5)
        assert isinstance(recs1, list)
        assert isinstance(recs2, list)
        assert isinstance(recs3, list)
