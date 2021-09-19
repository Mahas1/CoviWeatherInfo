import platform
import subprocess


def install_deps():
    with open("deps_install_log.txt", "w") as file:
        command = ["pip3", "install", "-r", "requirements.txt"]
        if platform.system() == "Windows":
            command[0] = "pip"
        subprocess.call(command, stdout=file, shell=True)
    if platform.system() == "Windows":
        subprocess.call(["cls"], shell=True)
    else:
        subprocess.call(["clear"], shell=True)
