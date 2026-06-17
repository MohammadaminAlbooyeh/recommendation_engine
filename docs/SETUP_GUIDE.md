# Setup Guide

## Prerequisites

- Docker and Docker Compose
- Python 3.9+
- Node.js 16+
- PostgreSQL 13 (if running locally)

## Quick Start with Docker

```bash
docker-compose up --build
```

This starts PostgreSQL, the API server on port 8000, and the frontend on port 3000.

## Manual Setup

### Backend

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/recommendation_db
python scripts/init_db.py
python scripts/seed_data.py
python -m uvicorn backend.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm start
```

## Configuration

Copy `.env.example` to `.env` and adjust:

| Variable | Default | Description |
|---|---|---|
| DATABASE_URL | postgresql://postgres:postgres@db:5432/recommendation_db | Database connection |
| REDIS_URL | redis://localhost:6379/0 | Redis connection |
| CACHE_TTL | 300 | Cache TTL in seconds |
| LOG_LEVEL | INFO | Logging level |
| SECRET_KEY | change-me | JWT secret key |
| DEBUG | false | Enable debug mode |
