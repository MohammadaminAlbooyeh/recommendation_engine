import sys
import os
import pickle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.models.database import SessionLocal
from backend.models.user import User, Rating
from config.model_config import model_config


def generate_for_user(user_id: int, n: int = 10):
    with open(model_config.COLLABORATIVE_FILTERING_PATH, "rb") as f:
        model = pickle.load(f)

    db = SessionLocal()
    ratings = db.query(Rating).all()
    db.close()

    import pandas as pd
    df = pd.DataFrame([
        {"user_id": r.user_id, "item_id": r.item_id, "rating": r.rating}
        for r in ratings
    ])
    model.fit(df)
    return model.recommend(user_id, n)


def generate_for_all_users(n: int = 10):
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    results = {}
    for user in users:
        results[user.id] = generate_for_user(user.id, n)
    return results


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--user_id", type=int, help="User ID to generate for")
    parser.add_argument("--n", type=int, default=10, help="Number of recommendations")
    args = parser.parse_args()

    if args.user_id:
        recs = generate_for_user(args.user_id, args.n)
        print(f"Recommendations for user {args.user_id}: {recs}")
    else:
        all_recs = generate_for_all_users(args.n)
        for uid, recs in all_recs.items():
            print(f"User {uid}: {recs}")
