from sqlalchemy.orm import Session
from typing import List
import pandas as pd
from backend.models import user
from backend.algorithms.collaborative_filtering.matrix_factorization import MatrixFactorization

def get_top_n_recommendations(user_id: int, n: int, db: Session) -> List[user.Item]:
    # 1. Fetch all ratings from the database
    ratings_query = db.query(user.Rating).all()
    if not ratings_query:
        return []
    
    # 2. Convert to DataFrame
    df = pd.DataFrame([
        {"user_id": r.user_id, "item_id": r.item_id, "rating": r.rating}
        for r in ratings_query
    ])
    
    # 3. Use the recommendation algorithm
    model = MatrixFactorization()
    model.fit(df)
    recommended_item_ids = model.recommend(user_id, n)
    
    # 4. Fetch item details from database
    recommended_items = db.query(user.Item).filter(user.Item.id.in_(recommended_item_ids)).all()
    
    return recommended_items
