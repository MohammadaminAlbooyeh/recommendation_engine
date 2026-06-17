from sqlalchemy.orm import Session
from typing import Optional, List
from backend.models import user
from backend.utils.exceptions import InvalidUserError


def get_user(db: Session, user_id: int) -> Optional[user.User]:
    return db.query(user.User).filter(user.User.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> Optional[user.User]:
    return db.query(user.User).filter(user.User.username == username).first()


def get_all_users(db: Session, skip: int = 0, limit: int = 100) -> List[user.User]:
    return db.query(user.User).offset(skip).limit(limit).all()


def create_user(db: Session, username: str, email: str) -> user.User:
    db_user = user.User(username=username, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if not db_user:
        raise InvalidUserError(user_id)
    db.delete(db_user)
    db.commit()
