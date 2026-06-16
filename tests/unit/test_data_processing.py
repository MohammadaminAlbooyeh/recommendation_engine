import pandas as pd
import numpy as np

class DataProcessor:
    @staticmethod
    def create_data_frame(ratings):
        return pd.DataFrame(ratings)
    @staticmethod
    def create_user_item_matrix(df):
        return df.pivot_table(index='user_id', columns='item_id', values='rating').fillna(0)
    @staticmethod
    def train_test_split(df, test_size=0.2, random_state=None):
        if random_state is not None:
            np.random.seed(random_state)
        indices = df.index.tolist()
        np.random.shuffle(indices)
        split = int(len(indices) * (1 - test_size))
        return df.loc[indices[:split]], df.loc[indices[split:]]

class TestDataProcessing:
    def test_data_frame_creation(self):
        ratings = [{"user_id": 1, "item_id": 1, "rating": 5}]
        dp = DataProcessor()
        df = dp.create_data_frame(ratings)
        assert isinstance(df, pd.DataFrame)
        assert list(df.columns) == ["user_id", "item_id", "rating"]
        assert len(df) == 1

    def test_user_item_matrix_creation(self):
        df = pd.DataFrame({
            "user_id": [1, 1, 2],
            "item_id": [1, 2, 1],
            "rating": [5, 3, 4]
        })
        dp = DataProcessor()
        matrix = dp.create_user_item_matrix(df)
        assert isinstance(matrix, pd.DataFrame)
        assert matrix.shape == (2, 2)

    def test_train_test_split(self):
        df = pd.DataFrame({
            "user_id": [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
            "item_id": [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
            "rating": [5, 4, 3, 2, 5, 4, 3, 2, 5, 4]
        })
        dp = DataProcessor()
        train, test = dp.train_test_split(df, test_size=0.2, random_state=42)
        assert isinstance(train, pd.DataFrame)
        assert isinstance(test, pd.DataFrame)
        assert len(train) + len(test) == len(df)
