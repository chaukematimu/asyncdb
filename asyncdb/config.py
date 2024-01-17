from pydantic import BaseSettings


class Settings(BaseSettings):
    PSQL_DSN: str

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
