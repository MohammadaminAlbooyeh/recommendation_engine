import sys
import os
import time
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.models.database import SessionLocal
from backend.models.user import Rating
from backend.algorithms.collaborative_filtering.matrix_factorization import MatrixFactorization
from backend.algorithms.collaborative_filtering.als import ALS
from backend.algorithms.content_based.content_similarity import ContentSimilarity


def benchmark():
    db = SessionLocal()
    ratings = db.query(Rating).all()
    db.close()

    if not ratings:
        print("No ratings found.")
        return

    df = pd.DataFrame([
        {"user_id": r.user_id, "item_id": r.item_id, "rating": r.rating}
        for r in ratings
    ])

    models = [
        ("MatrixFactorization", MatrixFactorization()),
        ("ALS", ALS()),
        ("ContentSimilarity", ContentSimilarity()),
    ]

    for name, model in models:
        start = time.perf_counter()
        model.fit(df)
        fit_time = time.perf_counter() - start

        start = time.perf_counter()
        recs = model.recommend(df["user_id"].iloc[0], 10)
        rec_time = time.perf_counter() - start

        print(f"{name:25s} | Fit: {fit_time:.4f}s | Recommend: {rec_time:.4f}s | Results: {len(recs)} items")


if __name__ == "__main__":
    benchmark()
