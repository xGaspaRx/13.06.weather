import time
from services.openweather_api import get_weather
from services.excel_files import save_file, read_file
from services.dashboard import render
from services.mysql_db import save_weather_record, create_weather_table

# render()

create_weather_table()

while True:
    weather_record = get_weather() # pobranie danych pogodowych / openweather_api.py
    save_file([weather_record]) # zapis excela / excel_files.py
    save_weather_record(weather_record) # zapis mysql / mysql_db.py
    print("Pobrano informacje")
    time.sleep(10)