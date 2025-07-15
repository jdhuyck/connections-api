from pydantic import PostgresDsn, field_validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    API_V1_STR: str = "/api/v1"

    @field_validator("DATABASE_URL")
    def validate_db_url(cls, v):
        if isinstance(v, str):
            return v
        return v.unicode_string()

    class Config:
        case_sensitive = True
        env_file = ".env"
        extra = "ignore"

settings = Settings()