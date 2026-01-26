from fastapi import FastAPI
from .api.routes import router
from .db.database import engine
from .models.note import Note
from . import ui

app = FastAPI(title="Notebook App")

@app.on_event("startup")
def create_tables():
    Note.metadata.create_all(bind=engine)

app.include_router(router, prefix="/api")

# Initialize NiceGUI UI
ui.init(app)