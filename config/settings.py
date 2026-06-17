import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = "Recommendation Engine"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me-in-production")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/recommendation_db")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    CACHE_TTL: int = int(os.getenv("CACHE_TTL", "300"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    DEFAULT_RECOMMENDATIONS_N: int = int(os.getenv("DEFAULT_RECOMMENDATIONS_N", "10"))


settings = Settings()
