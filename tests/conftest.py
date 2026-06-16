import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.api import routes
from backend.models import database, user

@pytest.fixture
def test_db():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    database.Base.metadata.create_all(bind=engine)
    TestSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return TestSession

@pytest.fixture
def test_session(test_db):
    session = test_db()
    yield session
    session.close()

@pytest.fixture
def sample_items(test_session):
    items = []
    for i in range(5):
        item = user.Item(title=f"Item {i}", genre=f"Genre {i % 3}", description=f"Description {i}")
        test_session.add(item)
        items.append(item)
    test_session.commit()
    return items

@pytest.fixture
def sample_users(test_session):
    users = []
    for i in range(3):
        u = user.User(username=f"user{i}", email=f"user{i}@test.com")
        test_session.add(u)
        users.append(u)
    test_session.commit()
    return users

@pytest.fixture
def sample_ratings(test_session, sample_users, sample_items):
    ratings = []
    for u in sample_users:
        for j, item in enumerate(sample_items):
            r = user.Rating(user_id=u.id, item_id=item.id, rating=float((j % 5) + 1))
            test_session.add(r)
            ratings.append(r)
    test_session.commit()
    return ratings

@pytest.fixture
def client(test_db):
    app = FastAPI()
    app.include_router(routes.router)

    @app.get("/")
    async def root():
        return {"message": "Welcome to the Recommendation Engine API", "status": "active"}

    def override_get_db():
        session = test_db()
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[database.get_db] = override_get_db
    return TestClient(app)
