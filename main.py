import json
import platform
import subprocess
import sys
import time

import assets
from scripts import install_dependencies, weather, covid

if sys.version_info.major < 3 and sys.version_info.minor < 7:
    print(("This program {red}CAN NOT{end} run in Python 3.6 and lower. "
           "{yellow}Python 3.8 or higher is recommended.{end} "
           "Your version of python is {cyan}{version}{end}.\n"
           "{red}Aborting...{end}").format(
        red=assets.color_red,
        end=assets.end_color_formatting,
        yellow=assets.color_yellow,
        cyan=assets.color_cyan,
        version=f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"))
    exit(1)  # formatted strings can't work in python 3.6 and older, and also some modules may need 3.7+
try:
    import requests
    import googletrans
    import speedtest
    import psutil
    import aiml
    import mysql
except ModuleNotFoundError:  # if the modes do not exist, we install the dependencies
    print("Missing dependencies. Attempting to install them now...")
    install_dependencies.install_deps()  # calling the function that installs dependencies
    with open("deps_error_log.txt", "r") as errorFile:
        string = errorFile.read()
        if string != "":
            print(f"{assets.color_red}Errors have occurred while installing dependencies. "
                  f"Please check the error log.{assets.end_color_formatting}")
        else:
            print(f"{assets.color_green}No errors have occurred while installing dependencies."
                  f"{assets.end_color_formatting}")
    print(f"Install logs available in {assets.color_green}deps_install_log.txt{assets.end_color_formatting}.\n"
          f"Error logs available in {assets.color_green}deps_error_log.txt{assets.end_color_formatting}\n"
          f"Please restart this program for changes to take effect.")
    exit(0)

import requests
from scripts.test_speed import test_speed
from scripts.system_info import hostinfo
from scripts import botchat, sql_functions

with open("config.json", "r") as configFile:
    project_config = json.load(configFile)


def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    with requests.get(url, headers=headers) as response:
        response_content = json.loads(response.content)
    return response_content.get("joke"), "Dad"


def get_joke_jokeapi(categories: list = None, blacklist: list = None):
    # this function is in case you want dark jokes.
    # The default joke provider will be the dad joke one (for obvious reaso ns)

    categories_str = "+".join(categories) if categories else "any"  # yes I love ternary operators, how did you know?
    blacklist_str = "+".join(blacklist) if blacklist else None

    url = f"https://v2.jokeapi.dev/joke/{categories_str}"

    if blacklist_str:
        url += f"?blacklistFlags={blacklist_str}"
        # if there are blacklists provided, we want to add the blacklist parameter to the url

    response = requests.get(url=url).content  # getting the json response from the API
    response = json.loads(response)  # string to dict conversion

    if response.get("type") == "twopart":  # jokes can be in two parts or one.
        setup, delivery = response.get("setup"), response.get("delivery")  # getting the variables from the dictionary
        joke_text = f"{setup}\n{assets.color_pink}{delivery}{assets.end_color_formatting}"
    else:
        joke_text = response.get("joke")

    return joke_text, response.get("category")


def exit_program(joke_text=None, joke_category=None):
    clear_screen()
    if not joke_text or not joke_category:
        joke_text, joke_category = get_joke_jokeapi()
    print(f"Here's a {assets.color_blue}{joke_category}{assets.end_color_formatting} joke for you!\n")
    print(joke_text)
    print(f"\n{assets.color_pink}Bye!{assets.end_color_formatting}")
    exit(0)


def speed_test():
    clear_screen()
    list_result = test_speed()
    if not list_result[-1].isnumeric():
        return print(list_result[-1])
    print(f"Ping: {assets.color_cyan}{list_result[0]} ms{assets.end_color_formatting}")
    print(f"Upload: {assets.color_cyan}{list_result[1]} Mbps{assets.end_color_formatting}")
    print(f"Download: {assets.color_cyan}{list_result[2]} Mbps{assets.end_color_formatting}")
    print(f"Server Name: {assets.color_cyan}{list_result[3]}{assets.end_color_formatting}")
    print(f"Server Location: {assets.color_cyan}{list_result[4]}{assets.end_color_formatting}")
    print(f"Sent: {assets.color_pink}{list_result[5]} MB{assets.end_color_formatting} | "
          f"Received: {assets.color_pink}{list_result[6]} MB{assets.end_color_formatting}")
    print("\n")


def chat_respond():
    while True:
        query = input(f"{assets.color_cyan}> {assets.end_color_formatting}")
        if query.lower() in ["exit", "quit"]:
            print("Bye!\n")
            break
        botchat.respond(query)


def clear_screen():
    if platform.system() == "Windows":
        subprocess.call(["cls"], shell=True)
    else:
        subprocess.call(["clear"], shell=True)


def user_input():
    print("Enter your choice:\n"
          "S. Test connection speed\n"
          "I. System Information\n"
          "W. Get weather info\n"
          "A. Add your location to database\n"
          "R. Remove your location from database\n"
          "F. Find your location from database\n"
          "C. Get Covid-19 stats for a location\n"
          "Q. Exit")
    user_i = input(f"{assets.color_green}> {assets.end_color_formatting}")
    if user_i.lower() == "s":
        clear_screen()
        speed_test()
        user_input()
    elif user_i.lower() == "i":
        clear_screen()
        hostinfo()
        user_input()
    elif user_i.lower() == "w":
        clear_screen()
        is_stored_in_db = True if input("Press 1 for entering location, and 2 for entering your name: ") == "1" \
            else False
        if is_stored_in_db:
            location = input("Enter your location: ")
        else:
            location = sql_functions.retrieve_location()
        if location:
            weather.get_embed_from_weather_dict(weather.get_weather_response(location))
        else:
            print("Location was not found in database. Aborting...\n")
        user_input()
    elif user_i.lower() == "a":
        clear_screen()
        sql_functions.insert_location()
        user_input()
    elif user_i.lower() == "r":
        clear_screen()
        sql_functions.remove_location()
        user_input()
    elif user_i.lower() == "f":
        clear_screen()
        sql_functions.retrieve_location()
        print("\n")
        user_input()
    elif user_i.lower() == "c":
        clear_screen()
        is_stored_in_db = True if input("Press 1 for entering country's name, "
                                        "and 2 for entering your name: ") == "2" \
            else False
        if is_stored_in_db:
            location = sql_functions.retrieve_location()
            if location:
                country = weather.get_country_code(sql_functions.retrieve_location())
            else:
                country = None
        else:
            country = input("Enter the country's name: ")
        if country:
            covid.corona_stats(country)
        user_input()
    elif user_i.lower() == "q":
        exit_program(joke_category=joke_category, joke_text=joke)
    elif user_i == project_config.get("botchat_secret_character"):
        print(f"{assets.color_yellow}You have found BotChat! type \"exit\" to exit.{assets.end_color_formatting}")
        print("Hello! What can I call you?")
        chat_respond()
        user_input()
    elif user_i == "pika":
        clear_screen()
        print(assets.pikachu)
        user_input()
    else:
        print("Unknown choice. Try again.")
        user_input()


"""Actual code starts here"""

assets_start_time = time.monotonic()
print("Readying assets...")
try:
    speedtest.Speedtest()  # initializing sample speedtest object to see if there is a network connection
    if not project_config.get("dad_jokes"):
        joke, joke_category = get_joke_jokeapi()
    else:
        joke, joke_category = get_dad_joke()
except Exception as e:
    if isinstance(e, requests.ConnectionError) or isinstance(e, speedtest.ConfigRetrievalError):
        print(f"{assets.color_red}Could not connect to the internet :({assets.end_color_formatting}")
        if sys.platform.lower() == "darwin":
            print("You seem to be on macOS. Are you sure you installed the SSL certificates?")
        sys.exit()
    else:
        print(f"{assets.color_red}{assets.format_underline}An Exception occurred: {assets.format_bold}{str(e)}"
              f"{assets.end_color_formatting}{assets.end_color_formatting}{assets.end_color_formatting}")
        exit(0)
time_now = time.monotonic()
elapsed_time = round((time_now - assets_start_time), 2)
clear_screen()
print(f"{assets.color_green}Assets readied in {elapsed_time} seconds.{assets.end_color_formatting}\n")

user_input()  # asking for input
