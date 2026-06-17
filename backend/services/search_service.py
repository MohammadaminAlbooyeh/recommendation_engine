from sqlalchemy.orm import Session
from typing import List
from backend.models.user import Item


def search_by_title(db: Session, query: str, limit: int = 20) -> List[Item]:
    return db.query(Item).filter(Item.title.ilike(f"%{query}%")).limit(limit).all()


def search_by_genre(db: Session, genre: str, limit: int = 50) -> List[Item]:
    return db.query(Item).filter(Item.genre.ilike(f"%{genre}%")).limit(limit).all()


def search_by_description(db: Session, query: str, limit: int = 20) -> List[Item]:
    return db.query(Item).filter(Item.description.ilike(f"%{query}%")).limit(limit).all()


def full_text_search(db: Session, query: str, limit: int = 20) -> List[Item]:
    pattern = f"%{query}%"
    return db.query(Item).filter(
        Item.title.ilike(pattern) | Item.description.ilike(pattern) | Item.genre.ilike(pattern)
    ).limit(limit).all()
