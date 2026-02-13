from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # App
    app_name: str = "BI System MVP"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    # Просто жестко задаем для MVP
    cors_origins: List[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]
    
    # Database
    database_url: str = "postgresql://user:password@localhost:5432/bi_system_db"
    
    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
