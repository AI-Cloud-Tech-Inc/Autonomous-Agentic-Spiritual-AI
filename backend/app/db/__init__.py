"""
Database initialization
"""
from app.models import Base
from app.db.session import engine


def init_db():
    """Initialize database tables"""
    Base.metadata.create_all(bind=engine)
