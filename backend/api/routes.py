from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.models import database, user
from backend.api import schemas
from backend.services import recommendation_service

router = APIRouter()

@router.get("/items", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    items = db.query(user.Item).offset(skip).limit(limit).all()
    return items

@router.post("/ratings", response_model=schemas.Rating)
def create_rating(rating: schemas.RatingCreate, db: Session = Depends(database.get_db)):
    db_rating = user.Rating(**rating.model_dump())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

@router.get("/recommendations/{user_id}", response_model=List[schemas.Item])
def get_recommendations(user_id: int, n: int = 10, db: Session = Depends(database.get_db)):
    recommendations = recommendation_service.get_top_n_recommendations(user_id, n, db)
    return recommendations
