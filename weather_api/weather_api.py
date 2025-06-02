import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
def fetch_weather_data():
    api_url= os.getenv("WEATHER_API_URL")
    response = requests.get(api_url)
    if response.status_code == 200:
        try:
            response.raise_for_status()
            data = response.json()
            
            print("Weather data fetched successfully!")
            print(json.dumps(data, indent=4))  # Print the data in a readable format
            return data

        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            raise

    

def mock_fetch_data():
   return {
    "request": {
        "type": "City",
        "query": "New York, United States of America",
        "language": "en",
        "unit": "m"
    },
    "location": {
        "name": "New York",
        "country": "United States of America",
        "region": "New York",
        "lat": "40.714",
        "lon": "-74.006",
        "timezone_id": "America/New_York",
        "localtime": "2025-06-02 05:14",
        "localtime_epoch": 1748841240,
        "utc_offset": "-4.0"
    },
    "current": {
        "observation_time": "09:14 AM",
        "temperature": 13,
        "weather_code": 116,
        "weather_icons": [
            "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png"
        ],
        "weather_descriptions": [
            "Partly cloudy"
        ],
        "astro": {
            "sunrise": "05:27 AM",
            "sunset": "08:22 PM",
            "moonrise": "12:11 PM",
            "moonset": "01:13 AM",
            "moon_phase": "Waxing Crescent",
            "moon_illumination": 38
        },
        "air_quality": {
            "co": "495.8",
            "no2": "33.485",
            "o3": "61",
            "so2": "11.84",
            "pm2_5": "17.945",
            "pm10": "18.685",
            "us-epa-index": "2",
            "gb-defra-index": "2"
        },
        "wind_speed": 9,
        "wind_degree": 315,
        "wind_dir": "NW",
        "pressure": 1014,
        "precip": 0,
        "humidity": 64,
        "cloudcover": 75,
        "feelslike": 13,
        "uv_index": 0,
        "visibility": 16,
        "is_day": "no"
    }
}