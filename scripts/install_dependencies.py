import platform
import subprocess
import sys


def install_deps():
    with open("deps_install_log.txt", "w") as file:
        command = [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        subprocess.run(command, stdout=file)

    if platform.system() == "Windows":
        subprocess.call(["cls"], shell=True)
    else:
        subprocess.call(["clear"], shell=True)
