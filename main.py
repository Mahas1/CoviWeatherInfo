import requests
import json

# work in progress
# this is by no means complete. we still have a long way to go, and new features will be added.
"""
Features in mind:
    - covid info
    - weather info
    - easter egg (hopefully)
    - translation using googletrans
    - test connection speed
    - total rundown of system info (additional feature that is totally useless, but cool nonetheless)
    - joke at the end (fun)
    - make a database with a table for name-location for weather and covid info, 
        and a table for name-language for translation
"""

blacklist_flags = ["nsfw", "religious", "political", "racist", "sexist", "explicit"]  # for personal reference


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
        joke = setup + "\n" + delivery
    else:
        joke = response.get("joke")

    return joke, response.get("category")


joke, category = get_joke()
print(f"Here's a nice little {category} joke for you!\n\n{joke}")
# would be nice to display when the user exits the program
