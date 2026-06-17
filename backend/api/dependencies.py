from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from typing import Optional
from backend.models.database import get_db
from backend.utils.config import config


def get_db_session(db: Session = Depends(get_db)):
    return db


def verify_token(authorization: Optional[str] = Header(None)):
    if not config.DEBUG:
        if not authorization:
            raise HTTPException(status_code=401, detail="Authorization header missing")
        scheme, _, token = authorization.partition(" ")
        if scheme.lower() != "bearer" or not token:
            raise HTTPException(status_code=401, detail="Invalid authorization scheme")
    return True
