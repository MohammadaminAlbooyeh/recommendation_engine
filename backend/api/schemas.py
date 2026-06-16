from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class RatingBase(BaseModel):
    user_id: int
    item_id: int
    rating: float

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class ItemBase(BaseModel):
    title: str
    genre: Optional[str] = None
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
