import pandas as pd
from config import Config
import os

def save_file(data):
    new_df = pd.DataFrame(data)
    try:
        if os.path.exists(Config.WEATHER_FILE):
            old_df = pd.read_excel(Config.WEATHER_FILE)
            df = pd.concat([old_df, new_df], ignore_index=True)
            df.to_excel(Config.WEATHER_FILE, index=False)
        else:
            new_df.to_excel(Config.WEATHER_FILE, index=False)
    except Exception as e:
        print(e)


def read_file():
    try:
        df = pd.read_excel(Config.WEATHER_FILE)
        return  df
    except:
        print("Wystąpił problem")