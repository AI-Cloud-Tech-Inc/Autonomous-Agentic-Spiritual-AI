"""
Core Package

Contains fundamental utilities for the AI Film Agent system.
"""

from .llm_client import LLMClient
from .config import Config

__all__ = ["LLMClient", "Config"]
