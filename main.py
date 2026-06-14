import time
from services.openweather_api import get_weather
from services.excel_files import save_file

while True:
    weather_record = get_weather()
    save_file([weather_record])
    print("Pobrano informacje")
    time.sleep(10)