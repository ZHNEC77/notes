from pydantic import BaseModel, ConfigDict
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DataBaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI__",
        extra="ignore",
    )
    # model_config1: ignore  = ConfigDict(extra='forbid')
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DataBaseConfig


settings = Settings()
