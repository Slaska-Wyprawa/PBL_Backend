from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    database_connection_url: str
    open_route_api_key: str

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"
