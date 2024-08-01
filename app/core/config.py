from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings

class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = True
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10

class Settings(BaseSettings):
    db: DatabaseConfig


settings = Settings()
