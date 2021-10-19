import json

import requests

with open("config.json", "r") as configFile:
    apiKey = json.load(configFile).get("weather_api_key")

url = "https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}".format(cityName="chennai",
                                                                                           apiKey=apiKey)
with requests.get(url) as response:
    response = json.loads(response.content)


def get_embed_from_weather_dict(result: dict):
    longitude = result.get("coord").get('lon')
    latitude = result.get("coord").get('lat')

    weather = result.get("weather")[0].get("main")
    icon = result.get("weather")[0].get("icon")
    actual_temp = int(result.get("main").get("temp") - 273.15)
    feels_like = int(result.get("main").get("feels_like") - 273.15)
    temp_min, temp_max = int(result.get("main").get("temp_min") - 273.15), \
                         int(result.get("main").get("temp_max") - 273.15)
    humidity = result.get("main").get("humidity")

    country_code = result.get("sys").get("country")
    name = result.get("name")

    print(f"Name - {name} | Country - {country_code}")
    print(f"Coord - {latitude}, {longitude}")
    print(f"Weather - {weather}")
    print(f"Temp/feelslike - {actual_temp}/{feels_like}")
    print(f"min/max - {temp_min}/{temp_max}")
    print(f"Humidity - {humidity}")


get_embed_from_weather_dict(response)
