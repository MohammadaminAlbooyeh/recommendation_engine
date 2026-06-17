import pandas as pd
from typing import Optional
from backend.utils.exceptions import InsufficientDataError


def load_csv(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)


def load_ratings_csv(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    required = {"user_id", "item_id", "rating"}
    if not required.issubset(df.columns):
        raise InsufficientDataError(f"CSV must contain columns: {required}")
    return df


def load_items_csv(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    if "item_id" not in df.columns:
        raise InsufficientDataError("CSV must contain 'item_id' column")
    return df


def load_users_csv(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    if "user_id" not in df.columns:
        raise InsufficientDataError("CSV must contain 'user_id' column")
    return df


def load_from_database(query_callable, limit: Optional[int] = None) -> pd.DataFrame:
    data = query_callable()
    if limit:
        data = data[:limit]
    return pd.DataFrame(data)
