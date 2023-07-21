from pydantic_settings import BaseSettings
from pydantic import PostgresDsn


class Settings(BaseSettings):
    APP_PORT: int = 8000
    REAL_DATABASE_URL: PostgresDsn = "postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres"
    TEST_DATABASE_URL: PostgresDsn = "postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres_test"

    class Config:
        env_file = ".env"


settings = Settings()
