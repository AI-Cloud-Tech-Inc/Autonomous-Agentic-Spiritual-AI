"""Utility functions."""
import logging
from datetime import datetime


def setup_logger(name: str = "spiritual_agent") -> logging.Logger:
    """Set up logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Console handler
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger


def validate_input(text: str) -> bool:
    """Validate user input."""
    return bool(text and len(text.strip()) > 0)


def format_timestamp(dt: datetime) -> str:
    """Format datetime to readable string."""
    return dt.strftime("%Y-%m-%d %H:%M:%S")
