"""
Database — SQLAlchemy engine, session factory, and table initialisation.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

from app.models.base import Base

# Allow DATABASE_URL to be overridden via env; default to local SQLite for development.
_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ai_film_studio.db")

# SQLite needs check_same_thread=False; the connect_args key is ignored by other drivers.
_connect_args = {"check_same_thread": False} if _DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(_DATABASE_URL, connect_args=_connect_args, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_tables() -> None:
    """Create all tables declared in the ORM models."""
    import app.models  # noqa: F401 — registers models with Base.metadata
    Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency that yields a DB session and closes it afterwards."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
