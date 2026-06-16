# Architecture Overview

The Recommendation Engine follows a standard three-tier architecture:

## 1. Frontend (React)
- **Framework**: React 18
- **State Management**: React Hooks (useState, useEffect)
- **Communication**: Axios for HTTP requests to the backend.
- **Features**: User ID selection, item browsing, rating submission, and recommendation display.

## 2. Backend (FastAPI)
- **Framework**: FastAPI
- **Web Server**: Uvicorn
- **Database ORM**: SQLAlchemy
- **Services**:
    - `RecommendationService`: Coordinates between API routes and the algorithm.
- **Algorithms**:
    - `MatrixFactorization`: Implements User-Based Collaborative Filtering using Cosine Similarity.

## 3. Data Layer (PostgreSQL)
- **Schema**:
    - `users`: Stores user metadata.
    - `items`: Stores item (movie) metadata.
    - `ratings`: Stores user-item interactions (ratings 1-5).

## Data Flow
1. User interacts with the Frontend.
2. Frontend sends requests to FastAPI.
3. FastAPI fetches/saves data to PostgreSQL.
4. When recommendations are requested:
    a. `RecommendationService` fetches all ratings.
    b. `MatrixFactorization` builds a sparse user-item matrix.
    c. Cosine similarity is used to find similar items.
    d. Predicted scores are calculated, and top-N unrated items are returned.
