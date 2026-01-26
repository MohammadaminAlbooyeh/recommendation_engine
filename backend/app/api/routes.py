from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..schemas.note import Note, NoteCreate
from ..services.note_service import get_notes, get_note, create_note, update_note, delete_note

router = APIRouter()

@router.get("/notes/", response_model=list[Note])
def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notes = get_notes(db)
    return notes[skip : skip + limit]

@router.get("/notes/{note_id}", response_model=Note)
def read_note(note_id: int, db: Session = Depends(get_db)):
    db_note = get_note(db, note_id=note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.post("/notes/", response_model=Note)
def create_note_endpoint(note: NoteCreate, db: Session = Depends(get_db)):
    return create_note(db=db, note=note)

@router.put("/notes/{note_id}", response_model=Note)
def update_note_endpoint(note_id: int, note: NoteCreate, db: Session = Depends(get_db)):
    db_note = update_note(db=db, note_id=note_id, note=note)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.delete("/notes/{note_id}")
def delete_note_endpoint(note_id: int, db: Session = Depends(get_db)):
    db_note = delete_note(db=db, note_id=note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted"}