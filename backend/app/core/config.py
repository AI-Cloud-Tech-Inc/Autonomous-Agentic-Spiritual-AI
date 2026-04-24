"""
Application Configuration
"""
from pydantic_settings import BaseSettings
from typing import List
import secrets
import os


def generate_secret_key() -> str:
    """Generate a secure random secret key"""
    return secrets.token_urlsafe(32)


class Settings(BaseSettings):
    """Application settings"""
    
    # Application
    APP_NAME: str = "AI-Film-Studio"
    APP_ENV: str = "development"
    DEBUG: bool = True
    API_VERSION: str = "v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", generate_secret_key())
    
    # Database
    DATABASE_URL: str = "sqlite:///./ai_film_studio.db"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # AI Services
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    STABILITY_API_KEY: str = ""
    ELEVENLABS_API_KEY: str = ""
    REPLICATE_API_TOKEN: str = ""
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    
    # File Upload
    MAX_UPLOAD_SIZE: int = 104857600  # 100MB
    ALLOWED_EXTENSIONS: List[str] = [".mp4", ".mov", ".avi", ".png", ".jpg", ".jpeg"]
    
    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

# Validate production settings
if settings.APP_ENV == "production":
    if settings.SECRET_KEY == generate_secret_key() or len(settings.SECRET_KEY) < 32:
        raise ValueError(
            "SECRET_KEY must be set to a secure random value in production. "
            "Generate one using: python -c 'import secrets; print(secrets.token_urlsafe(32))'"
        )
