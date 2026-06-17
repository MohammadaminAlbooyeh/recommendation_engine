import pandas as pd
import numpy as np
from collections import defaultdict


def compute_user_features(df: pd.DataFrame) -> pd.DataFrame:
    user_features = df.groupby("user_id").agg(
        rating_count=("rating", "count"),
        rating_mean=("rating", "mean"),
        rating_std=("rating", "std"),
        rating_min=("rating", "min"),
        rating_max=("rating", "max"),
    ).fillna(0).reset_index()
    return user_features


def compute_item_features(df: pd.DataFrame) -> pd.DataFrame:
    item_features = df.groupby("item_id").agg(
        rating_count=("rating", "count"),
        rating_mean=("rating", "mean"),
        rating_std=("rating", "std"),
    ).fillna(0).reset_index()
    return item_features


def compute_popularity_score(df: pd.DataFrame, decay: float = 0.01) -> pd.DataFrame:
    item_counts = df["item_id"].value_counts().reset_index()
    item_counts.columns = ["item_id", "count"]
    item_counts["popularity"] = 1.0 / (1.0 + decay * (item_counts["count"].max() - item_counts["count"]))
    return item_counts


def create_user_item_affinity(df: pd.DataFrame) -> pd.DataFrame:
    user_mean = df.groupby("user_id")["rating"].transform("mean")
    item_mean = df.groupby("item_id")["rating"].transform("mean")
    global_mean = df["rating"].mean()
    result = df.copy()
    result["affinity"] = result["rating"] - 0.5 * user_mean - 0.3 * item_mean - 0.2 * global_mean
    return result
