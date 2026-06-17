from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)


class ItemBase(BaseModel):
    title: str
    genre: Optional[str] = None
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    price: float = 0.0
    image_url: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Interaction(BaseModel):
    id: int
    user_id: int
    item_id: int
    event_type: str
    value: float
    session_id: Optional[str] = None
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)


class Recommendation(BaseModel):
    id: int
    user_id: int
    item_id: int
    score: float
    algorithm: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
