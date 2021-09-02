from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    database_connection_url: str

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"
