import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.models.database import SessionLocal
from backend.models.user import User
from backend.evaluation.a_b_testing import run_experiment, compute_metric_difference
from backend.evaluation.metrics import precision_at_k


def control_recommender(user_id):
    from backend.algorithms.collaborative_filtering.matrix_factorization import MatrixFactorization
    return _recommend(user_id, MatrixFactorization)


def treatment_recommender(user_id):
    from backend.algorithms.content_based.content_similarity import ContentSimilarity
    return _recommend(user_id, ContentSimilarity)


def _recommend(user_id, AlgorithmClass):
    import pandas as pd
    from backend.models.user import Rating
    db = SessionLocal()
    ratings = db.query(Rating).all()
    db.close()
    df = pd.DataFrame([
        {"user_id": r.user_id, "item_id": r.item_id, "rating": r.rating}
        for r in ratings
    ])
    model = AlgorithmClass()
    model.fit(df)
    return model.recommend(user_id, 10)


if __name__ == "__main__":
    db = SessionLocal()
    users = [u.id for u in db.query(User).all()]
    db.close()

    result = run_experiment(control_recommender, treatment_recommender, users, lambda recs: len(recs))
    print("A/B Test Results:")
    for k, v in result.items():
        print(f"  {k}: {v}")
