from pydantic_settings import BaseSettings
from pydantic import PostgresDsn


class Settings(BaseSettings):
    APP_PORT: int = 8000
    REAL_DATABASE_URL: str
    TEST_DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
