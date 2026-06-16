# Recommendation Engine

A full-stack recommendation engine built with FastAPI, React, and PostgreSQL. It uses Collaborative Filtering to provide personalized recommendations.

## Features
- **FastAPI Backend**: High-performance API for managing users, items, and ratings.
- **Collaborative Filtering**: Matrix Factorization based recommendation algorithm.
- **React Frontend**: Modern UI for interacting with the engine.
- **Dockerized**: Easy setup with Docker and Docker Compose.

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Python 3.9+ (if running locally)
- Node.js (if running frontend locally)

### Running with Docker
1. Clone the repository.
2. Run `docker-compose up --build`.
3. The API will be available at `http://localhost:8000`.
4. The Frontend will be available at `http://localhost:3000`.

### Manual Setup
1. **Backend**:
   ```bash
   pip install -r requirements.txt
   export DATABASE_URL=postgresql://user:pass@localhost:5432/db
   python backend/main.py
   ```
2. **Frontend**:
   ```bash
   cd frontend
   npm install
   npm start
   ```

### Seeding Data
To populate the database with sample data:
```bash
python scripts/seed_data.py
```

## Architecture
See `docs/ARCHITECTURE.md` for details on the system design.
