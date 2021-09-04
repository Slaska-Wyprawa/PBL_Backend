from functools import lru_cache
import os
from config.config import Settings
from sqlmodel import Field, Session, SQLModel, create_engine, select
USER = os.getenv('DATABASE_USERNAME')
PASSWORD = os.getenv('DATABASE_PASSWORD')
ADDRESS = os.getenv('DATABASE_ADDRESS')
PORT = os.getenv('DATABASE_PORT')
NAME = os.getenv('DATABASE_NAME')


@lru_cache()
def get_settings():
    return Settings()


settings: Settings = get_settings()
database_connection_url = settings.database_connection_url


engine = create_engine(database_connection_url,echo=True)





