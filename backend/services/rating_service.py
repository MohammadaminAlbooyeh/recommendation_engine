from sqlalchemy.orm import Session
from typing import List, Optional
from backend.models.user import Rating


def create_rating(db: Session, user_id: int, item_id: int, rating_value: float) -> Rating:
    db_rating = Rating(user_id=user_id, item_id=item_id, rating=rating_value)
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating


def get_ratings_for_user(db: Session, user_id: int) -> List[Rating]:
    return db.query(Rating).filter(Rating.user_id == user_id).all()


def get_ratings_for_item(db: Session, item_id: int) -> List[Rating]:
    return db.query(Rating).filter(Rating.item_id == item_id).all()


def get_all_ratings(db: Session) -> List[Rating]:
    return db.query(Rating).all()


def get_user_rating_for_item(db: Session, user_id: int, item_id: int) -> Optional[Rating]:
    return db.query(Rating).filter(
        Rating.user_id == user_id, Rating.item_id == item_id
    ).first()


def delete_rating(db: Session, rating_id: int):
    db_rating = db.query(Rating).filter(Rating.id == rating_id).first()
    if db_rating:
        db.delete(db_rating)
        db.commit()
