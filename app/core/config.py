from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class DatabaseConfig(BaseModel):
    # Postgres server data
    host: str
    port: int
    user: str
    password: str
    name: str

    # Engine args
    echo: bool = True
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10

    @property
    def DATABASE_URL_asyncpg(self):
        return "postgresql+asyncpg://%s:%s@%s:%d/%s" % (
            self.user, self.password, self.host, self.port, self.name
        )

class Settings(BaseSettings):
    postgres: DatabaseConfig

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="_",
        case_sensitive=False
    )


settings = Settings()
