from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings

class DatabaseConfig(BaseModel):
    url: PostgresDsn

class Settings(BaseSettings):
    db_url: DatabaseConfig


settings = Settings()
