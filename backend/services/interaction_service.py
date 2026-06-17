from sqlalchemy.orm import Session
from typing import List, Optional
from backend.models.interaction import Interaction
import datetime


def log_interaction(
    db: Session, user_id: int, item_id: int,
    event_type: str, value: float = 1.0, session_id: str = None
) -> Interaction:
    db_interaction = Interaction(
        user_id=user_id, item_id=item_id,
        event_type=event_type, value=value,
        session_id=session_id, timestamp=datetime.datetime.utcnow()
    )
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction


def get_user_interactions(db: Session, user_id: int, limit: int = 50) -> List[Interaction]:
    return db.query(Interaction).filter(
        Interaction.user_id == user_id
    ).order_by(Interaction.timestamp.desc()).limit(limit).all()


def get_recent_interactions(db: Session, minutes: int = 60) -> List[Interaction]:
    cutoff = datetime.datetime.utcnow() - datetime.timedelta(minutes=minutes)
    return db.query(Interaction).filter(Interaction.timestamp >= cutoff).all()


def get_interactions_by_type(db: Session, event_type: str, limit: int = 100) -> List[Interaction]:
    return db.query(Interaction).filter(
        Interaction.event_type == event_type
    ).order_by(Interaction.timestamp.desc()).limit(limit).all()
