import json
import sys
import time

import assets
from scripts.install_dependencies import install_deps

try:
    import requests
    import googletrans
    import speedtest
except ModuleNotFoundError:  # if the modes do not exist, we install the dependencies
    print("Missing dependencies. Attempting to install them now...")
    install_deps()  # calling the function that installs dependencies
    with open("deps_error_log.txt", "r") as errorFile:
        string = errorFile.read()
        if string != "":
            print(f"{assets.color_red}Errors have occurred while installing dependencies.{assets.end_color_formatting}")
        else:
            print(f"{assets.color_green}No errors have occurred while installing dependencies."
                  f"{assets.end_color_formatting}")
    print(f"Install logs available in {assets.color_green}deps_install_log.txt{assets.end_color_formatting}.\n"
          f"Error logs available in {assets.color_green}deps_error_log.txt{assets.end_color_formatting}\n")

import requests
import googletrans
from scripts.test_speed import test_speed

version = float(f"{sys.version_info[0]}.{sys.version_info[1]}")  # python version
if version <= 3.6:
    print(f"This program {assets.color_red}CAN NOT{assets.end_color_formatting} run in Python 3.6 and lower. "
          f"{assets.color_yellow}Python 3.7 or higher is recommended.{assets.end_color_formatting} "
          f"Your version of python is {assets.color_cyan}{version}{assets.end_color_formatting}.\n"
          f"{assets.color_red}Aborting...{assets.end_color_formatting}")
    sys.exit("Please update your Python install.")  # formatted strings can't work in python 3.6 and older.


def get_joke(categories: list = None, blacklist: list = None):
    categories_str = "+".join(categories) if categories else "any"
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
    if not joke_text or not joke_category:
        joke_text, joke_category = get_joke()
    print(f"Here's a {assets.color_blue}{joke_category}{assets.end_color_formatting} joke for you!\n")
    print(joke_text)
    sys.exit()


def speed_test():
    list_result = test_speed()
    print(f"Ping: {list_result[0]}ms")
    print(f"Upload: {list_result[1]}Mbps")
    print(f"Download: {list_result[2]}Mbps")
    print(f"Server Name: {list_result[3]}")
    print(f"Server Location: {list_result[4]}")
    print(f"Sent: {list_result[5]}MB | Recieved: {list_result[6]}MB")
    print("\n")


def user_input():
    print("Enter your choice:\n"
          "1. Test connection speed\n"
          "2. Exit")
    user_i = input(f"{assets.color_green}> {assets.end_color_formatting}")
    if user_i == "1":
        speed_test()
        user_input()
    if user_i == "2":
        exit_program(joke_category=joke_category, joke_text=joke)


"""Actual code starts here"""

assets_start_time = time.monotonic()
print("Readying assets...")
try:
    joke, joke_category = get_joke()
except requests.ConnectionError:
    print(f"{assets.color_red}Could not connect to the internet :({assets.end_color_formatting}")
    sys.exit()
time_now = time.monotonic()
elapsed_time = round((time_now - assets_start_time), 2)
print(f"{assets.color_green}Assets readied in {elapsed_time} seconds.{assets.end_color_formatting}\n")


user_input()
