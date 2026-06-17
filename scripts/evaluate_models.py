import sys
import os
import pickle
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.models.database import SessionLocal
from backend.models.user import Rating
from backend.evaluation.metrics import precision_at_k, recall_at_k, rmse
from backend.data_processing.preprocessor import train_test_split


def evaluate():
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

    train_df, test_df = train_test_split(df)

    from backend.algorithms.collaborative_filtering.matrix_factorization import MatrixFactorization
    model = MatrixFactorization()
    model.fit(train_df)

    precisions = []
    recalls = []
    for user_id in test_df["user_id"].unique():
        recs = model.recommend(user_id, n=10)
        relevant = test_df[test_df["user_id"] == user_id]["item_id"].tolist()
        precisions.append(precision_at_k(recs, relevant, 10))
        recalls.append(recall_at_k(recs, relevant, 10))

    print(f"Average Precision@10: {sum(precisions) / len(precisions):.4f}" if precisions else "N/A")
    print(f"Average Recall@10: {sum(recalls) / len(recalls):.4f}" if recalls else "N/A")


if __name__ == "__main__":
    evaluate()
