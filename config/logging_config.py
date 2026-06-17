import os
import logging


class LoggingConfig:
    LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    FORMAT: str = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    FILE_PATH: str = os.getenv("LOG_FILE", "")
    ROTATION_SIZE: int = int(os.getenv("LOG_ROTATION_SIZE", "10485760"))
    BACKUP_COUNT: int = int(os.getenv("LOG_BACKUP_COUNT", "5"))


def configure_logging():
    config = LoggingConfig()
    handlers = [logging.StreamHandler()]
    if config.FILE_PATH:
        from logging.handlers import RotatingFileHandler
        handlers.append(RotatingFileHandler(
            config.FILE_PATH, maxBytes=config.ROTATION_SIZE, backupCount=config.BACKUP_COUNT
        ))
    logging.basicConfig(level=getattr(logging, config.LEVEL.upper(), logging.INFO), format=config.FORMAT, handlers=handlers)


logging_config = LoggingConfig()
