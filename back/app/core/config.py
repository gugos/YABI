from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # App
    app_name: str = "BI System MVP"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    cors_origins: list = ["http://localhost:5173", "http://127.0.0.1:5173"]
    
    # Database
    sqlite_path: str = "data/combined_data.db"
    
    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
