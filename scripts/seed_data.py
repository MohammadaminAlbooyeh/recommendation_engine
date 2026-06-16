import sys
import os
# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.orm import Session
from backend.models import database, user
import random

def seed():
    db = next(database.get_db())
    
    # Add some items (Movies)
    movies = [
        {"title": "The Shawshank Redemption", "genre": "Drama", "description": "Two imprisoned men bond over a number of years."},
        {"title": "The Godfather", "genre": "Crime", "description": "The aging patriarch of an organized crime dynasty transfers control to his reluctant son."},
        {"title": "The Dark Knight", "genre": "Action", "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham."},
        {"title": "Pulp Fiction", "genre": "Crime", "description": "The lives of two mob hitmen, a boxer, a gangster and his wife."},
        {"title": "Inception", "genre": "Sci-Fi", "description": "A thief who steals corporate secrets through the use of dream-sharing technology."},
        {"title": "The Matrix", "genre": "Sci-Fi", "description": "A computer hacker learns from mysterious rebels about the true nature of his reality."},
        {"title": "Forrest Gump", "genre": "Drama", "description": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal."},
        {"title": "Interstellar", "genre": "Sci-Fi", "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."},
    ]
    
    db_items = []
    for m in movies:
        item = user.Item(**m)
        db.add(item)
        db_items.append(item)
    
    db.commit()
    
    # Add some users
    usernames = ["alice", "bob", "charlie", "david", "eve"]
    db_users = []
    for uname in usernames:
        u = user.User(username=uname, email=f"{uname}@example.com")
        db.add(u)
        db_users.append(u)
    
    db.commit()
    
    # Add some random ratings
    for u in db_users:
        # Each user rates 3-5 random movies
        rated_items = random.sample(db_items, random.randint(3, 5))
        for item in rated_items:
            rating = user.Rating(user_id=u.id, item_id=item.id, rating=float(random.randint(3, 5)))
            db.add(rating)
            
    db.commit()
    print("Database seeded successfully!")

if __name__ == "__main__":
    # Create tables first
    database.Base.metadata.create_all(bind=database.engine)
    seed()
