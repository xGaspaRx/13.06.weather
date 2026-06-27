from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    API_KEY = os.getenv("ENV_API_KEY")
    PLACE = os.getenv("ENV_PLACE")
    WEATHER_FILE = os.getenv("ENV_WEATHER_FILE")
    DB_HOST = os.getenv("ENV_DB_HOST")
    DB_USER = os.getenv("ENV_DB_USER")
    DB_PASSWORD = os.getenv("ENV_DB_PASSWORD")
    DB_DATABASE = os.getenv("ENV_DB_DATABASE")

    # sciezka pliku
    # silnik od excela
    # rodzaj bazy