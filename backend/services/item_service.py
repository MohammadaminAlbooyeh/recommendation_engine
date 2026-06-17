from sqlalchemy.orm import Session
from typing import Optional, List
from backend.models.user import Item
from backend.utils.exceptions import InvalidItemError


def get_item(db: Session, item_id: int) -> Optional[Item]:
    return db.query(Item).filter(Item.id == item_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    return db.query(Item).offset(skip).limit(limit).all()


def get_items_by_ids(db: Session, item_ids: List[int]) -> List[Item]:
    return db.query(Item).filter(Item.id.in_(item_ids)).all()


def create_item(db: Session, title: str, genre: str = None, description: str = None) -> Item:
    db_item = Item(title=title, genre=genre, description=description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def search_items(db: Session, query: str, limit: int = 20) -> List[Item]:
    return db.query(Item).filter(Item.title.ilike(f"%{query}%")).limit(limit).all()


def delete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if not db_item:
        raise InvalidItemError(item_id)
    db.delete(db_item)
    db.commit()
