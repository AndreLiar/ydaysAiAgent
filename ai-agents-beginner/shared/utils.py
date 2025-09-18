"""
Utility functions for AI agents - logging, configuration, helpers
"""

import os
import logging
from typing import Dict, Any, Optional
from dotenv import load_dotenv

def setup_logging(level: str = "INFO", format_string: Optional[str] = None) -> logging.Logger:
    """Set up logging for agents"""
    
    if format_string is None:
        format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    
    logger = logging.getLogger("ai_agents")
    logger.setLevel(numeric_level)
    
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(numeric_level)
        formatter = logging.Formatter(format_string)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger

def load_config(config_file: Optional[str] = None) -> Dict[str, Any]:
    """Load configuration from .env file"""
    
    if config_file:
        load_dotenv(config_file)
    else:
        load_dotenv()
    
    config = {
        # API Keys
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "anthropic_api_key": os.getenv("ANTHROPIC_API_KEY"),
        "google_api_key": os.getenv("GOOGLE_API_KEY"),
        
        # Local models
        "ollama_base_url": os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        "ollama_model": os.getenv("OLLAMA_MODEL", "llama2"),
        
        # Application
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "max_requests_per_minute": int(os.getenv("MAX_REQUESTS_PER_MINUTE", "10")),
    }
    
    return {k: v for k, v in config.items() if v is not None}

def validate_api_key(api_key: Optional[str], service: str) -> bool:
    """Basic API key validation"""
    if not api_key:
        return False
    
    if service.lower() == "openai":
        return api_key.startswith("sk-") and len(api_key) > 20
    elif service.lower() == "anthropic":
        return api_key.startswith("sk-ant-") and len(api_key) > 20
    
    return len(api_key) > 10

def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text with ellipsis"""
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."