import sys
import os
import pickle
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.models.database import SessionLocal
from backend.models.user import Rating
from backend.algorithms.collaborative_filtering.matrix_factorization import MatrixFactorization
from backend.algorithms.content_based.content_similarity import ContentSimilarity
from backend.algorithms.collaborative_filtering.als import ALS
from config.model_config import model_config


def load_ratings():
    db = SessionLocal()
    ratings = db.query(Rating).all()
    db.close()
    if not ratings:
        print("No ratings found in database.")
        return None
    return pd.DataFrame([
        {"user_id": r.user_id, "item_id": r.item_id, "rating": r.rating}
        for r in ratings
    ])


def train_collaborative_filtering(df):
    print("Training Matrix Factorization model...")
    model = MatrixFactorization()
    model.fit(df)
    with open(model_config.COLLABORATIVE_FILTERING_PATH, "wb") as f:
        pickle.dump(model, f)
    print(f"Saved to {model_config.COLLABORATIVE_FILTERING_PATH}")


def train_content_based(df):
    print("Training Content Similarity model...")
    model = ContentSimilarity()
    model.fit(df)
    with open(model_config.CONTENT_BASED_PATH, "wb") as f:
        pickle.dump(model, f)
    print(f"Saved to {model_config.CONTENT_BASED_PATH}")


def train_als(df):
    print("Training ALS model...")
    model = ALS()
    model.fit(df)
    with open(model_config.COLLABORATIVE_FILTERING_PATH.replace(".pkl", "_als.pkl"), "wb") as f:
        pickle.dump(model, f)
    print("Saved ALS model")


if __name__ == "__main__":
    df = load_ratings()
    if df is not None:
        train_collaborative_filtering(df)
        train_content_based(df)
        train_als(df)
        print("All models trained successfully!")
