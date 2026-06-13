import time
from services.openweather_api import get_weather


while True:
    weather_record = get_weather()
    print(weather_record)

    time.sleep(15)