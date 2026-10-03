"""Configuration settings for Shakuni Backend."""

import os
from typing import List
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "Shakuni: Strategic Deception & Manipulation Analysis API"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))

    # CORS origins
    _origins_raw: str = os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173,http://localhost:3000,http://127.0.0.1:3000"
    )
    ALLOWED_ORIGINS: List[str] = [origin.strip() for origin in _origins_raw.split(",") if origin.strip()]

    # Max length limits for analysis payloads
    MAX_TEXT_LENGTH: int = int(os.getenv("MAX_TEXT_LENGTH", "10000"))
    MAX_BATCH_SIZE: int = int(os.getenv("MAX_BATCH_SIZE", "50"))


settings = Settings()
