from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api import routes
from backend.models import database
from backend.utils.logger import logger

app = FastAPI(title="Recommendation Engine API", version="1.0.0")

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(routes.router)

@app.on_event("startup")
async def startup():
    logger.info("Starting up the Recommendation Engine API")
    # Initialize database
    database.Base.metadata.create_all(bind=database.engine)

@app.get("/")
async def root():
    return {"message": "Welcome to the Recommendation Engine API", "status": "active"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
