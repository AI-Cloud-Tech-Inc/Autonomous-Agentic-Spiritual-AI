"""
Configuration Management

Handles application configuration from environment variables and config files.

Functions:
    - load(): Load configuration
    - get(): Get configuration value
    - validate(): Validate configuration
"""

import os
from typing import Any, Dict, Optional


class Config:
    """
    Application configuration manager.
    
    Loads settings from:
        1. Environment variables
        2. .env file
        3. config.yaml file (if present)
    
    Attributes:
        settings: Current configuration dictionary
        
    Example:
        >>> config = Config()
        >>> api_key = config.get("OPENAI_API_KEY")
        >>> print(config.get("VIDEO_OUTPUT_FORMAT"))
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize configuration.
        
        Args:
            config_path: Path to config.yaml file
        """
        self.settings = self._load_defaults()
        
        if config_path:
            self._load_from_file(config_path)
        
        self._load_from_env()
    
    def _load_defaults(self) -> Dict[str, Any]:
        """
        Load default configuration values.
        
        Returns:
            Dict with default settings
        """
        return {
            # LLM Settings
            "LLM_PROVIDER": "openai",
            "LLM_MODEL": "gpt-4",
            
            # Video Settings
            "VIDEO_OUTPUT_FORMAT": "mp4",
            "VIDEO_RESOLUTION": "1920x1080",
            "VIDEO_FPS": 30,
            
            # Audio Settings
            "AUDIO_SAMPLE_RATE": 44100,
            "VOICE_DEFAULT": "en-US",
            
            # API Settings
            "API_HOST": "0.0.0.0",
            "API_PORT": 8000,
            
            # Paths
            "DATA_DIR": "./data",
            "OUTPUT_DIR": "./output",
            
            # Debug
            "DEBUG": False,
            "LOG_LEVEL": "INFO"
        }
    
    def _load_from_env(self):
        """Load configuration from environment variables."""
        env_mappings = {
            "OPENAI_API_KEY": "OPENAI_API_KEY",
            "ANTHROPIC_API_KEY": "ANTHROPIC_API_KEY",
            "LLM_PROVIDER": "LLM_PROVIDER",
            "LLM_MODEL": "LLM_MODEL",
            "VIDEO_OUTPUT_FORMAT": "VIDEO_OUTPUT_FORMAT",
            "DEBUG": "DEBUG"
        }
        
        for key, env_var in env_mappings.items():
            value = os.getenv(env_var)
            if value is not None:
                self.settings[key] = value
    
    def _load_from_file(self, path: str):
        """Load configuration from YAML file."""
        # Placeholder for YAML config loading
        pass
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key not found
            
        Returns:
            Configuration value
            
        Example:
            >>> config.get("VIDEO_OUTPUT_FORMAT")
            'mp4'
        """
        return self.settings.get(key, default)
    
    def set(self, key: str, value: Any):
        """
        Set configuration value.
        
        Args:
            key: Configuration key
            value: Value to set
        """
        self.settings[key] = value
    
    def validate(self) -> Dict[str, str]:
        """
        Validate required configuration.
        
        Returns:
            Dict of missing required keys
        """
        required = ["OPENAI_API_KEY"]
        missing = [k for k in required if not self.get(k)]
        return {"missing": missing}
