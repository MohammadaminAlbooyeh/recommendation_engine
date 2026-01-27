# Smart Notes - Notebook Application

A modern, full-stack note-taking application built with FastAPI, NiceGUI, and a clean REST API. Features a beautiful UI with dual interfaces - a modern web frontend and an elegant NiceGUI dashboard.

## Features

- ✨ **Dual Interface**: Choose between a modern HTML/CSS/JS frontend or a sleek NiceGUI-powered UI
- 📝 **Full CRUD Operations**: Create, read, update, and delete notes
- 🎨 **Beautiful Design**: Modern glassmorphism design with smooth animations
- 🔍 **Search Functionality**: Quickly find notes in the NiceGUI interface
- 💾 **SQLite Database**: Lightweight database with SQLAlchemy ORM
- 🚀 **FastAPI Backend**: High-performance async API
- ✅ **Comprehensive Tests**: Full test coverage for API endpoints

## Tech Stack

### Backend
- **FastAPI** - Modern web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation using Python type annotations
- **NiceGUI** - Web-based UI framework built on top of FastAPI
- **Uvicorn** - ASGI server

### Frontend (Alternative Interface)
- **Vanilla JavaScript** - No framework dependencies
- **HTML5 & CSS3** - Modern web standards
- **Responsive Design** - Works on all screen sizes

## Project Structure

```
notebook_app/
├── backend/
│   ├── app/
│   │   ├── api/           # API routes
│   │   ├── core/          # Configuration
│   │   ├── db/            # Database setup
│   │   ├── models/        # SQLAlchemy models
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── services/      # Business logic
│   │   ├── main.py        # Application entry point
│   │   └── ui.py          # NiceGUI interface
│   ├── tests/             # Test suite
│   └── requirements.txt   # Python dependencies
├── frontend/              # Static web frontend
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   └── templates/
└── docs/                  # Documentation
```

## Installation

### Prerequisites
- Python 3.9 or higher
- pip

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd notebook_app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r backend/requirements.txt
```

4. (Optional) Create a `.env` file for custom configuration:
```bash
cp .env.example .env
```

## Running the Application

### Using the Run Script (Recommended)
```bash
python run.py
```

### Manual Start
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The application will be available at:
- **NiceGUI Interface**: http://localhost:8000/
- **API Documentation**: http://localhost:8000/docs
- **Alternative Frontend**: http://localhost:8000/static/index.html (if served)

## API Endpoints

### Notes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/notes/` | Get all notes |
| GET | `/api/notes/{note_id}` | Get a specific note |
| POST | `/api/notes/` | Create a new note |
| PUT | `/api/notes/{note_id}` | Update a note |
| DELETE | `/api/notes/{note_id}` | Delete a note |

### Example Request

```bash
# Create a note
curl -X POST "http://localhost:8000/api/notes/" \
  -H "Content-Type: application/json" \
  -d '{"title": "My First Note", "content": "This is a test note"}'

# Get all notes
curl "http://localhost:8000/api/notes/"
```

## Development

### Running Tests
```bash
cd backend
pytest tests/
```

### Database

The application uses SQLite by default. The database file (`sql_app.db`) will be created automatically in the backend directory.

To use a different database, set the `DATABASE_URL` environment variable:
```bash
export DATABASE_URL="postgresql://user:password@localhost/dbname"
```

## Configuration

Configuration is managed through environment variables or the `.env` file:

- `DATABASE_URL`: Database connection string (default: `sqlite:///./sql_app.db`)

## Features in Detail

### NiceGUI Interface
- Real-time note updates
- Inline editing with smooth transitions
- Responsive design with glassmorphism effects
- Search functionality
- Toast notifications

### REST API
- Full OpenAPI documentation
- Request/response validation
- Error handling
- CORS support (configurable)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or contributions, please open an issue on GitHub.

---

Built with ❤️ using FastAPI and NiceGUI
