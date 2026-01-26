from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Default to SQLite for simplicity. Override via env var DATABASE_URL
    database_url: str = "sqlite:///./sql_app.db"

    class Config:
        env_file = ".env"

settings = Settings()