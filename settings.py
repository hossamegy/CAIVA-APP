from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    NAME: str
    VERSION: str
    API_KEY: str
    MODEL_NAME: str
    EMBEDDING_MODEL: str
    TEMPERATURE: int
    
    class Config:
        env_file = '.env'

def get_settings():
    return Settings()
