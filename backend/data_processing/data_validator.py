import pandas as pd
from typing import List, Tuple
from backend.utils.constants import RATING_MIN, RATING_MAX


def validate_ratings(df: pd.DataFrame) -> List[str]:
    errors = []
    if "user_id" not in df.columns:
        errors.append("Missing column: user_id")
    if "item_id" not in df.columns:
        errors.append("Missing column: item_id")
    if "rating" not in df.columns:
        errors.append("Missing column: rating")
    if "rating" in df.columns:
        out_of_range = df[(df["rating"] < RATING_MIN) | (df["rating"] > RATING_MAX)]
        if not out_of_range.empty:
            errors.append(f"Ratings out of range [{RATING_MIN}, {RATING_MAX}]: {len(out_of_range)} rows")
    return errors


def validate_items(df: pd.DataFrame) -> List[str]:
    errors = []
    if "item_id" not in df.columns:
        errors.append("Missing column: item_id")
    return errors


def validate_no_duplicates(df: pd.DataFrame, subset: List[str]) -> List[str]:
    dups = df.duplicated(subset=subset, keep=False)
    if dups.any():
        return [f"Found {dups.sum()} duplicate rows on {subset}"]
    return []


def validate_no_missing_values(df: pd.DataFrame) -> List[str]:
    missing = df.columns[df.isnull().any()].tolist()
    if missing:
        return [f"Missing values in columns: {missing}"]
    return []


def is_valid_dataset(df: pd.DataFrame) -> Tuple[bool, List[str]]:
    errors = []
    if df.empty:
        errors.append("Dataset is empty")
        return False, errors
    errors.extend(validate_ratings(df))
    errors.extend(validate_no_missing_values(df))
    return len(errors) == 0, errors
