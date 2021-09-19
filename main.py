"""
Features in mind:
    - covid info
    - weather info
    - easter egg (hopefully)
    - translation using googletrans
    - test connection speed
    - total rundown of system info (additional feature that is totally useless, but cool nonetheless)
    - joke at the end ----------- (groundwork has been laid)
    - make a database with a table for name-location for weather and covid info,
        and a table for name-language for translation
"""

import json
import sys
import time

import assets
from scripts.install_dependencies import install_deps

try:
    import requests
    import googletrans
except ModuleNotFoundError:  # if the modes do not exist, we install the dependencies
    print("Missing dependencies. Attempting to install them now...")
    install_deps()  # calling the function that installs dependencies
    print(f"Installed dependencies. Install logs available in "
          f"{assets.color_green}deps_install_log.txt{assets.end_color_formatting}. "
          f"Please rerun this program.")
    sys.exit()

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
        setup, delivery = response.get("setup"), response.get("delivery")  # getting the variables from the dictionaey
        joke_text = f"{setup}\n{assets.color_pink}{delivery}{assets.end_color_formatting}"
    else:
        joke_text = response.get("joke")

    return joke_text, response.get("category")


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
# to be printed when the user exits
print(f"Here's a nice little {joke_category} joke for you!\n\n{joke}")
