from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    NAME: str
    VERSION: str
    API_KEY: str
    MODEL_NAME: str
    EMBEDDING_MODEL: str
    TEMPERATURE: int
    FILE_ALLOWED_TYPES: list
    FILE_CHUNK_SIZE: int
    FILE_MAX_SIZE: int

    class Config:
        env_file = '.env'

def get_settings():
    return Settings()
