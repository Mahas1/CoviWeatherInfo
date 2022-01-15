import requests

weather_api_key = ""
if weather_api_key == "":
    weather_api_key = input("Enter your weather API key: ")


def get_covid_stats(country):
    track_url = f"https://disease.sh/v3/covid-19/countries/{country}?strict=true"
    response_dict = requests.get(track_url).json()

    if response_dict.get("message") == "Country not found or doesn't have any cases":
        print("Country not found or doesn't have any cases.")
        return

    total_cases = response_dict.get("cases")
    today_cases = response_dict.get("todayCases")
    total_deaths = response_dict.get("deaths")
    today_deaths = response_dict.get("todayDeaths")
    total_recovered = response_dict.get("recovered")
    today_recovered = response_dict.get("todayRecovered")
    active_cases = response_dict.get("active")
    critical_cases = response_dict.get("critical")
    cases_per_million = response_dict.get("casesPerOneMillion")
    deaths_per_million = response_dict.get("deathsPerOneMillion")
    total_tests = response_dict.get("tests")
    population = response_dict.get("population")
    active_per_million = response_dict.get("activePerOneMillion")
    recovered_per_million = response_dict.get("recoveredPerOneMillion")
    critical_per_million = response_dict.get("criticalPerOneMillion")

    print(f"\nCountry: {country.title()}")
    print(f"Total Cases: {total_cases}")
    print(f"Cases Today: {today_cases}")
    print(f"Total Deaths: {total_deaths}")
    print(f"Deaths Today: {today_deaths}")
    print(f"Total Recovered: {total_recovered}")
    print(f"Recovered Today: {today_recovered}")
    print(f"Active Cases: {active_cases}")
    print(f"Critical Cases: {critical_cases}")
    print(f"Cases per Million: {cases_per_million}")
    print(f"Deaths per Million: {deaths_per_million}")
    print(f"Total Tests: {total_tests}")
    print(f"Population of {country.title()}: {population}")
    print(f"Active per Million: {active_per_million}")
    print(f"Recovered per Million: {recovered_per_million}")
    print(f"Critical per Million: {critical_per_million}")


def get_weather_info(city):
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}"
    result = requests.get(weather_url).json()
    if result.get("cod") == 404:
        print("City not found.")
        return
    if result.get("cod") == 401:
        print("Invalid API Key.")
        return
    longitude = result.get("coord").get('lon')
    latitude = result.get("coord").get('lat')

    weather = result.get("weather")[0].get("main")
    actual_temp = int(result.get("main").get("temp") - 273.15)
    feels_like = int(result.get("main").get("feels_like") - 273.15)

    temp_min = int(result.get("main").get("temp_min") - 273.15)
    temp_max = int(result.get("main").get("temp_max") - 273.15)

    humidity = result.get("main").get("humidity")

    print(f"\nWeather for {city.title()}")
    print(f"Longitude: {longitude}")
    print(f"Latitude: {latitude}")
    print(f"Weather: {weather}")
    print(f"Actual Temperature: {actual_temp} C")
    print(f"Feels Like: {feels_like} C")
    print(f"Minimum Temperature: {temp_min} C")
    print(f"Maximum Temperature: {temp_max} C")
    print(f"Humidity: {humidity} C")


def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    with requests.get(url, headers=headers) as response:
        response_content = response.json()
    return response_content.get("joke")
