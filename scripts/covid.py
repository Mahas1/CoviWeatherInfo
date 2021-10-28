import requests
import ast


def corona_stats(country):
    if country is None:
        track_url = "https://disease.sh/v3/covid-19/all"
    else:
        track_url = f"https://disease.sh/v3/covid-19/countries/{country}?strict=true"
    response_dict = requests.get(track_url).content.decode("utf8")
    response_dict = ast.literal_eval(response_dict)

    if response_dict.get("message") == "Country not found or doesn't have any cases":
        print(f"{country} - Country not found or doesn't have any cases.\n")
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

    country_name = response_dict.get("country")  # not used in worldwide stats

    print(f"Covid 19 stats in {country_name}")
    print(f"Total cases: {total_cases}")
    print(f"New cases today: {today_cases}")
    print(f"Cases per million: {cases_per_million}")
    print("")
    print(f"Total deaths: {total_deaths}")
    print(f"Deaths today: {today_deaths}")
    print(f"Deaths per million: {deaths_per_million}")
    print("")
    print(f"Active cases: {active_cases}")
    print(f"Active cases per million: {active_per_million}")
    print("")
    print(f"Critical cases: {critical_cases}")
    print(f"Critical cases per million: {critical_per_million}")
    print("")
    print(f"Recovered: {total_recovered}")
    print(f"Recovered today: {today_recovered}")
    print(f"Recovered per million: {recovered_per_million}")
    print("")
    print(f"Total tests conducted: {total_tests}")
    print("")
    print(f"Population of {country_name}: {population}")
    print("")
