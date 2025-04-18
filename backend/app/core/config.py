from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost/db"
    JWT_SECRET: str = "secret"
    
    class Config:
        env_file = ".env"

settings = Settings()
