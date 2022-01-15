import subprocess

pink = "\033[95m"
blue = "\033[94m"
cyan = "\033[96m"
green = "\033[92m"
yellow = "\033[93m"
red = "\033[91m"
bold = "\033[1m"
underline = "\033[4m"
end_formatting = "\033[0m"


def colour_pink(text):
    return pink + text + end_formatting


def colour_blue(text):
    return blue + text + end_formatting


def colour_cyan(text):
    return cyan + text + end_formatting


def colour_green(text):
    return green + text + end_formatting


def colour_yellow(text):
    return yellow + text + end_formatting


def colour_red(text):
    return red + text + end_formatting


def clear_screen():
    subprocess.run("clear || cls ", shell=True)
    # || is the OR operator in bash.
    # So it will run the first command if it is successful, or the second command if the first command fails.
