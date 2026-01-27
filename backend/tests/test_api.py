import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.database import Base, get_db
from app.models.note import Note

# Create a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Setup and teardown for each test"""
    # Setup: Create tables
    Base.metadata.create_all(bind=engine)
    yield
    # Teardown: Drop all tables
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def test_create_note():
    """Test creating a new note"""
    response = client.post(
        "/api/notes/",
        json={"title": "Test Note", "content": "This is a test note"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Note"
    assert data["content"] == "This is a test note"
    assert "id" in data
    assert "created_at" in data

def test_read_notes_empty():
    """Test reading notes when database is empty"""
    response = client.get("/api/notes/")
    assert response.status_code == 200
    assert response.json() == []

def test_read_notes():
    """Test reading all notes"""
    # Create test notes
    client.post("/api/notes/", json={"title": "Note 1", "content": "Content 1"})
    client.post("/api/notes/", json={"title": "Note 2", "content": "Content 2"})
    
    response = client.get("/api/notes/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "Note 1"
    assert data[1]["title"] == "Note 2"

def test_read_note():
    """Test reading a specific note"""
    # Create a note
    create_response = client.post(
        "/api/notes/",
        json={"title": "Specific Note", "content": "Specific Content"}
    )
    note_id = create_response.json()["id"]
    
    # Read the note
    response = client.get(f"/api/notes/{note_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Specific Note"
    assert data["content"] == "Specific Content"
    assert data["id"] == note_id

def test_read_note_not_found():
    """Test reading a note that doesn't exist"""
    response = client.get("/api/notes/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"

def test_update_note():
    """Test updating an existing note"""
    # Create a note
    create_response = client.post(
        "/api/notes/",
        json={"title": "Original Title", "content": "Original Content"}
    )
    note_id = create_response.json()["id"]
    
    # Update the note
    response = client.put(
        f"/api/notes/{note_id}",
        json={"title": "Updated Title", "content": "Updated Content"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["content"] == "Updated Content"
    assert data["id"] == note_id

def test_update_note_not_found():
    """Test updating a note that doesn't exist"""
    response = client.put(
        "/api/notes/9999",
        json={"title": "Test", "content": "Test"}
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"

def test_delete_note():
    """Test deleting a note"""
    # Create a note
    create_response = client.post(
        "/api/notes/",
        json={"title": "To Delete", "content": "Will be deleted"}
    )
    note_id = create_response.json()["id"]
    
    # Delete the note
    response = client.delete(f"/api/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Note deleted"
    
    # Verify it's deleted
    get_response = client.get(f"/api/notes/{note_id}")
    assert get_response.status_code == 404

def test_delete_note_not_found():
    """Test deleting a note that doesn't exist"""
    response = client.delete("/api/notes/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"

def test_create_note_validation():
    """Test note creation with invalid data"""
    # Missing title
    response = client.post(
        "/api/notes/",
        json={"content": "Content only"}
    )
    assert response.status_code == 422
    
    # Missing content
    response = client.post(
        "/api/notes/",
        json={"title": "Title only"}
    )
    assert response.status_code == 422

def test_notes_pagination():
    """Test notes pagination"""
    # Create 15 notes
    for i in range(15):
        client.post("/api/notes/", json={"title": f"Note {i}", "content": f"Content {i}"})
    
    # Test pagination
    response = client.get("/api/notes/?skip=0&limit=10")
    assert response.status_code == 200
    assert len(response.json()) == 10
    
    response = client.get("/api/notes/?skip=10&limit=10")
    assert response.status_code == 200
    assert len(response.json()) == 5

def test_note_timestamps():
    """Test that timestamps are created properly"""
    response = client.post(
        "/api/notes/",
        json={"title": "Timestamp Test", "content": "Testing timestamps"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "created_at" in data
    
    # Verify timestamp format
    from datetime import datetime
    created_at = datetime.fromisoformat(data["created_at"].replace('Z', '+00:00'))
    assert isinstance(created_at, datetime)

def test_multiple_notes_different_content():
    """Test creating multiple notes with different content"""
    notes = [
        {"title": "Work Note", "content": "Meeting at 3pm"},
        {"title": "Personal Note", "content": "Buy groceries"},
        {"title": "Idea Note", "content": "New project idea"}
    ]
    
    created_ids = []
    for note in notes:
        response = client.post("/api/notes/", json=note)
        assert response.status_code == 200
        created_ids.append(response.json()["id"])
    
    # Verify all notes exist
    response = client.get("/api/notes/")
    assert response.status_code == 200
    assert len(response.json()) == 3

# Cleanup
import os
@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    """Cleanup test database after all tests"""
    def remove_test_db():
        if os.path.exists("./test.db"):
            os.remove("./test.db")
    request.addfinalizer(remove_test_db)
