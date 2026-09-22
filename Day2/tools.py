import urllib.request
import json


def get_weather(city):
    # Coordinates for Coimbatore
    latitude = 11.0168
    longitude = 76.9558

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        "&current=temperature_2m,relative_humidity_2m,weather_code"
    )

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        current = data["current"]

        return {
            "city": city,
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "weather_code": current["weather_code"]
        }

    except Exception as e:
        return {
            "city": city,
            "error": str(e)
        }