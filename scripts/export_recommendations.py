import sys
import os
import csv
import pickle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.models.database import SessionLocal
from backend.models.user import User, Rating
from config.model_config import model_config


def export_recommendations(output_file: str, n: int = 10):
    with open(model_config.COLLABORATIVE_FILTERING_PATH, "rb") as f:
        model = pickle.load(f)

    db = SessionLocal()
    ratings = db.query(Rating).all()
    users = db.query(User).all()
    db.close()

    import pandas as pd
    df = pd.DataFrame([
        {"user_id": r.user_id, "item_id": r.item_id, "rating": r.rating}
        for r in ratings
    ])
    model.fit(df)

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["user_id", "recommended_item_ids"])
        for user in users:
            recs = model.recommend(user.id, n)
            writer.writerow([user.id, ",".join(map(str, recs))])

    print(f"Exported recommendations to {output_file}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="recommendations.csv", help="Output CSV file")
    parser.add_argument("--n", type=int, default=10, help="Number of recommendations per user")
    args = parser.parse_args()
    export_recommendations(args.output, args.n)
