from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PSQL_DSN: str


settings = Settings()
