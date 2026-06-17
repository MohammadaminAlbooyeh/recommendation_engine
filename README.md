# Recommendation Engine 🎬

A production-ready, full-stack recommendation engine built with **FastAPI**, **React**, and **PostgreSQL**. Provides intelligent, personalized recommendations using multiple algorithms including Collaborative Filtering, Content-Based, and Hybrid approaches.

## ✨ Key Features

- **🤖 Multiple Algorithms**: Collaborative Filtering, Content-Based, Embedding-based, and Hybrid approaches
- **⚡ FastAPI Backend**: High-performance async API with full CORS support
- **🎨 Modern React Frontend**: Responsive UI with real-time updates
- **📊 Comprehensive Analytics**: User engagement tracking and interaction logging
- **🔍 Advanced Search**: Full-text search with similarity scoring
- **⚙️ Caching Layer**: Redis-ready with in-memory and LRU strategies
- **📈 A/B Testing Framework**: Statistical significance testing for algorithm variants
- **📡 Monitoring**: Prometheus metrics, Grafana dashboards, and alerts
- **🐳 Container Ready**: Docker, Docker Compose, and Kubernetes configurations
- **✅ Test Suite**: 36 comprehensive unit and integration tests

## 📋 Project Structure

```
recommendation_engine/
├── backend/                      # FastAPI backend application
│   ├── api/                      # API routes and schemas
│   │   ├── routes.py            # REST endpoints
│   │   ├── schemas.py           # Pydantic models
│   │   ├── dependencies.py      # FastAPI dependencies
│   │   └── middleware.py        # Custom middleware
│   ├── models/                  # SQLAlchemy ORM models
│   │   ├── user.py              # User, Item, Rating models
│   │   ├── database.py          # Database configuration
│   │   ├── interaction.py       # User interactions
│   │   └── recommendation.py    # Recommendation records
│   ├── services/                # Business logic layer
│   │   ├── recommendation_service.py
│   │   ├── user_service.py
│   │   ├── item_service.py
│   │   ├── rating_service.py
│   │   ├── analytics_service.py
│   │   └── search_service.py
│   ├── algorithms/              # Recommendation algorithms
│   │   ├── base_recommender.py
│   │   ├── collaborative_filtering.py
│   │   ├── content_based.py
│   │   ├── hybrid.py
│   │   └── embeddings.py
│   ├── caching/                 # Caching strategies
│   │   ├── cache_manager.py
│   │   ├── memory_cache.py
│   │   ├── redis_cache.py
│   │   └── cache_strategies.py
│   ├── data_processing/         # Data processing utilities
│   │   ├── data_loader.py
│   │   ├── preprocessor.py
│   │   ├── feature_engineering.py
│   │   ├── similarity_calculator.py
│   │   └── embedding_generator.py
│   ├── evaluation/              # Metrics and evaluation
│   │   ├── metrics.py
│   │   ├── precision_recall.py
│   │   ├── ranking_metrics.py
│   │   ├── diversity_metrics.py
│   │   ├── serendipity.py
│   │   └── a_b_testing.py
│   ├── middleware/              # HTTP middleware
│   │   ├── auth.py
│   │   ├── cors_handler.py
│   │   ├── error_handler.py
│   │   ├── request_id.py
│   │   └── timing.py
│   ├── utils/                   # Utility functions
│   │   ├── config.py
│   │   ├── constants.py
│   │   ├── decorators.py
│   │   ├── exceptions.py
│   │   ├── helpers.py
│   │   └── validators.py
│   └── main.py                  # FastAPI application entry
├── frontend/                    # React TypeScript frontend
│   ├── src/
│   │   ├── components/          # React components
│   │   ├── pages/               # Page components
│   │   ├── hooks/               # Custom React hooks
│   │   ├── services/            # API client services
│   │   ├── utils/               # Frontend utilities
│   │   ├── styles/              # CSS/styling
│   │   └── App.tsx              # Main app component
│   ├── public/                  # Static assets
│   └── package.json             # Dependencies
├── tests/                       # Test suite
│   ├── unit/                    # Unit tests (15 tests)
│   ├── integration/             # Integration tests (13 tests)
│   └── load/                    # Performance tests
├── scripts/                     # Utility scripts
│   ├── seed_data.py             # Database seeding
│   ├── init_db.py               # Database initialization
│   ├── train_models.py          # Model training
│   ├── generate_recommendations.py
│   ├── evaluate_models.py
│   ├── benchmark.py
│   ├── a_b_test.py
│   └── export_recommendations.py
├── config/                      # Configuration files
│   ├── settings.py
│   ├── database_config.py
│   ├── algorithm_config.py
│   ├── model_config.py
│   └── logging_config.py
├── kubernetes/                  # K8s manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── configmap.yaml
│   └── secret.yaml
├── monitoring/                  # Monitoring setup
│   ├── prometheus.yml
│   ├── alerts.yml
│   └── grafana_dashboards/
├── docker/                      # Docker configurations
│   ├── Dockerfile.frontend
│   └── nginx/
├── docs/                        # Documentation
│   ├── ARCHITECTURE.md
│   ├── API_REFERENCE.md
│   ├── SETUP_GUIDE.md
│   ├── ALGORITHMS.md
│   ├── EVALUATION.md
│   ├── DEPLOYMENT.md
│   ├── PERFORMANCE.md
│   ├── A_B_TESTING.md
│   └── TROUBLESHOOTING.md
├── docker-compose.yml
├── Dockerfile.api
├── Makefile
├── requirements.txt
├── setup.py
├── LICENSE
└── README.md
```

## 🔄 System Architecture & Data Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                      USER BROWSER                               │
└────────────────────────────┬────────────────────────────────────┘
                             │
                    HTTP/REST (Port 3000)
                             │
        ┌────────────────────▼─────────────────────┐
        │      REACT FRONTEND (Port 3000)          │
        │  ├─ Item Discovery                      │
        │  ├─ Rating Interface                    │
        │  ├─ Recommendation Display              │
        │  └─ User Analytics                      │
        └────────────────────┬─────────────────────┘
                             │
                    HTTP/REST (Port 8000)
                  Cross-Origin (CORS)
                             │
        ┌────────────────────▼──────────────────────────┐
        │    FASTAPI BACKEND (Port 8000)                │
        │  ┌──────────────────────────────────────────┐ │
        │  │ API Routes & Endpoints                  │ │
        │  │ ├─ GET  /items                          │ │
        │  │ ├─ POST /ratings                        │ │
        │  │ ├─ GET  /recommendations/{user_id}      │ │
        │  │ └─ GET  /interactions                   │ │
        │  └──────────────────────────────────────────┘ │
        │  ┌──────────────────────────────────────────┐ │
        │  │ Business Logic Layer (Services)         │ │
        │  │ ├─ RecommendationService                │ │
        │  │ ├─ UserService                          │ │
        │  │ ├─ RatingService                        │ │
        │  │ ├─ InteractionService                   │ │
        │  │ ├─ AnalyticsService                     │ │
        │  │ └─ SearchService                        │ │
        │  └──────────────────────────────────────────┘ │
        │  ┌──────────────────────────────────────────┐ │
        │  │ Algorithm Layer                         │ │
        │  │ ├─ CollaborativeFiltering               │ │
        │  │ ├─ ContentBasedFiltering                │ │
        │  │ ├─ HybridRecommender                    │ │
        │  │ └─ EmbeddingBased                       │ │
        │  └──────────────────────────────────────────┘ │
        │  ┌──────────────────────────────────────────┐ │
        │  │ Caching Layer                           │ │
        │  │ ├─ In-Memory Cache (LRU/FIFO)           │ │
        │  │ └─ Redis Cache (Optional)               │ │
        │  └──────────────────────────────────────────┘ │
        └────────────────────┬───────────────────────────┘
                             │
                      SQL (Port 5432)
                             │
        ┌────────────────────▼──────────────────────┐
        │    PostgreSQL/SQLite Database             │
        │  ├─ users table                           │
        │  ├─ items table                           │
        │  ├─ ratings table (user-item interactions)│
        │  ├─ interactions table                    │
        │  ├─ recommendations table                 │
        │  └─ user_profiles table                   │
        └───────────────────────────────────────────┘
```

## 📊 Recommendation Algorithm Workflow

```
User Interaction
      │
      ▼
┌─────────────────────────┐
│  Collect User Ratings   │
│  & Interactions         │
└────────┬────────────────┘
         │
         ▼
┌──────────────────────────────────────┐
│   DATA PROCESSING PIPELINE           │
├──────────────────────────────────────┤
│  1. Data Loading                     │
│     └─ Fetch ratings from database  │
│                                      │
│  2. Preprocessing                    │
│     ├─ Handle missing values         │
│     ├─ Normalize ratings             │
│     └─ Filter sparse data            │
│                                      │
│  3. Feature Engineering              │
│     ├─ User-Item matrix construction │
│     ├─ User similarity scores        │
│     └─ Item embeddings               │
│                                      │
│  4. Data Validation                  │
│     └─ Quality checks                │
└────────┬─────────────────────────────┘
         │
         ▼
┌────────────────────────────────────────────┐
│   RECOMMENDATION ALGORITHMS                │
├────────────────────────────────────────────┤
│                                            │
│  ┌──────────────────────────────────────┐ │
│  │ Collaborative Filtering              │ │
│  │ (User-Based & Item-Based)            │ │
│  │  • Matrix Factorization              │ │
│  │  • Cosine Similarity                 │ │
│  │  • K-Nearest Neighbors               │ │
│  └──────────────────────────────────────┘ │
│                                            │
│  ┌──────────────────────────────────────┐ │
│  │ Content-Based Filtering              │ │
│  │  • TF-IDF                            │ │
│  │  • Item Features                     │ │
│  │  • Genre/Category Matching           │ │
│  └──────────────────────────────────────┘ │
│                                            │
│  ┌──────────────────────────────────────┐ │
│  │ Hybrid Approaches                    │ │
│  │  • Weighted Ensemble                 │ │
│  │  • Stacking Combiner                 │ │
│  └──────────────────────────────────────┘ │
│                                            │
└────────┬─────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────┐
│  RANKING & FILTERING               │
│  ├─ Score predictions              │
│  ├─ Remove rated items             │
│  ├─ Apply diversity constraints    │
│  └─ Rank by relevance              │
└────────┬───────────────────────────┘
         │
         ▼
┌────────────────────────────────────┐
│  CACHE RESULTS                     │
│  ├─ Store in memory                │
│  ├─ Redis cache (if configured)    │
│  └─ TTL-based expiration           │
└────────┬───────────────────────────┘
         │
         ▼
┌────────────────────────────────────┐
│  RETURN RECOMMENDATIONS            │
│  └─ Send to Frontend API           │
└────────────────────────────────────┘
```

## 🚀 Getting Started

### Prerequisites
- **Docker & Docker Compose** (for containerized setup)
- **Python 3.9+** (for local backend)
- **Node.js 14+** (for local frontend)
- **PostgreSQL 13+** (optional, SQLite used for local dev)

### Quick Start with Docker

```bash
# Clone and navigate
git clone <repository>
cd recommendation_engine

# Start all services
docker-compose up --build

# Services will be available at:
# - Frontend: http://localhost:3000
# - API: http://localhost:8000
# - Database: localhost:5432
```

### Manual Setup (Local Development)

#### Backend Setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure database
export DATABASE_URL="sqlite:///recommendation.db"  # or PostgreSQL URL

# Run backend
python -m uvicorn backend.main:app --reload
# API available at http://localhost:8000
```

#### Frontend Setup
```bash
# Install dependencies
cd frontend
npm install

# Start development server
npm start
# Frontend available at http://localhost:3000

# Build production bundle
npm run build
```

### Initialize Database
```bash
# Create tables and seed sample data
python scripts/seed_data.py

# Or initialize database only
python scripts/init_db.py
```

## 📡 API Endpoints

### Core Endpoints
- `GET /` - Health check
- `GET /items` - List all items
- `GET /items/{item_id}` - Get item details
- `POST /ratings` - Submit a rating
- `GET /recommendations/{user_id}` - Get personalized recommendations
- `GET /interactions` - Get user interactions

### Query Parameters
- `/recommendations/{user_id}?n=10` - Get top 10 recommendations
- `/items?skip=0&limit=100` - Pagination
- `/search?q=movie_title` - Search items

## ✅ Testing

### Run All Tests
```bash
# Unit + Integration tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=backend --cov-report=html

# Specific test type
pytest tests/unit/ -v
pytest tests/integration/ -v
pytest tests/load/ -v
```

### Test Results
- ✅ 36 total tests
- ✅ 15 unit tests
- ✅ 13 integration tests
- ✅ 8 load/performance tests
- ✅ 100% pass rate

## 📊 Monitoring & Evaluation

### Evaluation Metrics
- **Precision@K**: Top-K recommendation precision
- **Recall@K**: Top-K recommendation recall
- **NDCG**: Normalized Discounted Cumulative Gain
- **RMSE/MAE**: Rating prediction accuracy
- **Coverage**: Catalog coverage
- **Diversity**: Recommendation diversity
- **Serendipity**: Unexpected relevance

### Monitor Performance
```bash
# Start Prometheus & Grafana
docker-compose up prometheus grafana

# Access dashboards
# Prometheus: http://localhost:9090
# Grafana: http://localhost:3000 (admin/admin)
```

### A/B Testing
```bash
# Run A/B test comparing algorithms
python scripts/a_b_test.py --algorithm1 collaborative --algorithm2 hybrid
```

## 📚 Documentation

- **[Architecture Guide](docs/ARCHITECTURE.md)** - System design and components
- **[API Reference](docs/API_REFERENCE.md)** - Detailed endpoint documentation
- **[Setup Guide](docs/SETUP_GUIDE.md)** - Deployment instructions
- **[Algorithm Details](docs/ALGORITHMS.md)** - How each algorithm works
- **[Evaluation](docs/EVALUATION.md)** - Metrics and benchmarking
- **[Performance Tips](docs/PERFORMANCE.md)** - Optimization strategies
- **[A/B Testing](docs/A_B_TESTING.md)** - Running experiments
- **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Common issues

## 🛠️ Development

### Project Status
- ✅ Backend: Complete with 6 algorithms
- ✅ Frontend: React UI with full features
- ✅ Testing: 36 comprehensive tests (all passing)
- ✅ Documentation: Comprehensive guides
- ✅ Monitoring: Prometheus + Grafana setup
- ✅ Deployment: Docker, Docker Compose, Kubernetes ready

### Recent Improvements
- Fixed SQLAlchemy datetime deprecation warnings
- Updated Pydantic v2 compatibility
- Resolved frontend build issues
- Verified end-to-end integration

### Code Quality
```
Language Stats:
- Python:     ~3,500 lines (backend + tests)
- TypeScript: ~2,000 lines (frontend)
- YAML:       Configuration & infrastructure
- Markdown:   ~400 lines (documentation)
```

## 🐳 Deployment Options

### Docker Compose (Development/Staging)
```bash
docker-compose up --build
```

### Kubernetes (Production)
```bash
kubectl apply -f kubernetes/
```

### Cloud Platforms
- **AWS**: ECS, EKS, RDS support
- **GCP**: Cloud Run, GKE support
- **Azure**: Container Instances, AKS support
- **Heroku**: Procfile ready

## 📞 Support & Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

**Built with ❤️ using FastAPI, React, and SQLAlchemy**
