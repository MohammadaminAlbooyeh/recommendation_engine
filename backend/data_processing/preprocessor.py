import pandas as pd
import numpy as np


def normalize_ratings(df: pd.DataFrame, col: str = "rating") -> pd.DataFrame:
    result = df.copy()
    min_r, max_r = result[col].min(), result[col].max()
    if max_r > min_r:
        result[f"{col}_norm"] = (result[col] - min_r) / (max_r - min_r)
    else:
        result[f"{col}_norm"] = 0.5
    return result


def fill_missing_values(df: pd.DataFrame, col: str, strategy: str = "mean") -> pd.DataFrame:
    result = df.copy()
    if strategy == "mean":
        result[col] = result[col].fillna(result[col].mean())
    elif strategy == "median":
        result[col] = result[col].fillna(result[col].median())
    elif strategy == "zero":
        result[col] = result[col].fillna(0)
    elif strategy == "mode":
        result[col] = result[col].fillna(result[col].mode().iloc[0] if not result[col].mode().empty else 0)
    return result


def encode_categorical(df: pd.DataFrame, col: str) -> pd.DataFrame:
    result = df.copy()
    result[f"{col}_encoded"] = result[col].astype("category").cat.codes
    return result


def create_user_item_matrix(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(index="user_id", columns="item_id", values="rating").fillna(0)


def train_test_split(df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42) -> tuple:
    np.random.seed(random_state)
    users = df["user_id"].unique()
    test_users = np.random.choice(users, size=int(len(users) * test_size), replace=False)
    test_mask = df["user_id"].isin(test_users)
    return df[~test_mask], df[test_mask]
