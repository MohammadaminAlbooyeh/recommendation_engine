from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Dict, List
from backend.models.user import Rating, Item
from backend.models.interaction import Interaction


def get_average_rating(db: Session) -> float:
    result = db.query(func.avg(Rating.rating)).scalar()
    return float(result) if result else 0.0


def get_rating_distribution(db: Session) -> Dict[float, int]:
    results = db.query(Rating.rating, func.count(Rating.id)).group_by(Rating.rating).all()
    return {float(r): c for r, c in results}


def get_most_rated_items(db: Session, limit: int = 10) -> List[tuple]:
    results = db.query(
        Item.id, Item.title, func.count(Rating.id).label("count"),
        func.avg(Rating.rating).label("avg_rating")
    ).join(Rating).group_by(Item.id).order_by(func.count(Rating.id).desc()).limit(limit).all()
    return results


def get_popular_genres(db: Session, limit: int = 5) -> List[tuple]:
    results = db.query(
        Item.genre, func.count(Rating.id).label("count")
    ).join(Rating).group_by(Item.genre).order_by(func.count(Rating.id).desc()).limit(limit).all()
    return results


def get_active_users(db: Session, limit: int = 10) -> List[tuple]:
    from backend.models.user import User
    results = db.query(
        User.id, User.username, func.count(Interaction.id).label("activity_count")
    ).join(Interaction).group_by(User.id).order_by(func.count(Interaction.id).desc()).limit(limit).all()
    return results
