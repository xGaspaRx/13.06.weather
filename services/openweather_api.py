import requests
from datetime import datetime
from config import Config

def get_weather():
    API_KEY = Config.API_KEY
    PLACE = Config.PLACE

    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={PLACE}&appid={API_KEY}&units=metric")
        data = response.json()

        weather = {
            "name": data.get("name"),
            "temp": data.get("main").get("temp"),
            "feels_like": data.get("main").get("feels_like"),
            "wind_speed": data.get("wind").get("speed"),
            "pressure": data.get("main").get("pressure"),
            "humidity": data.get("main").get("humidity"),
            "clouds": data.get("clouds").get("all"),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return weather
    except:
        print("Błąd")