import json
from urllib.parse import quote as encode

import requests

with open("config.json", "r") as configFile:
    apiKey = json.load(configFile).get("weather_api_key")

url = "https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}".format(cityName="{cityName}",
                                                                                           apiKey=apiKey)


def get_weather_response(location):
    final_url = url.format(cityName=encode(location))
    with requests.get(final_url) as response:
        response = json.loads(response.content)
    return response


def get_country_code(city_name: str):
    final_url = url.format(cityName=encode(city_name))
    with requests.get(final_url) as response:
        response = json.loads(response.content)
        result = json.loads(response)
    country_code = result.get("sys").get("country")
    return country_code


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
    print(f"Coord - {latitude} latitude, {longitude} longitude")
    print(f"Weather - {weather}")
    print(f"Temp/feelslike - {actual_temp}˚C / {feels_like}˚C")
    print(f"min/max - {temp_min}˚C/{temp_max}˚C")
    print(f"Humidity - {humidity}%")
    print("\n")
