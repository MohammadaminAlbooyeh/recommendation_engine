import os


class DatabaseConfig:
    URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/recommendation_db")
    POOL_SIZE: int = int(os.getenv("DB_POOL_SIZE", "10"))
    MAX_OVERFLOW: int = int(os.getenv("DB_MAX_OVERFLOW", "20"))
    ECHO: bool = os.getenv("DB_ECHO", "false").lower() == "true"


database_config = DatabaseConfig()
