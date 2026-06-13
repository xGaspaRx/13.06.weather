from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    API_KEY = os.getenv("ENV_API_KEY")
    PLACE = os.getenv("ENV_PLACE")

    # sciezka pliku
    # silnik od excela
    # rodzaj bazy