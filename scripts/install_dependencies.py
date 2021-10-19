import platform
import subprocess
import sys


def install_deps():
    out_file = open("deps_install_log.txt", "w")
    err_file = open("deps_error_log.txt", "w")
    command = [sys.executable, "-m", "pip", "install", "-r", "requirements.txt",
               "--no-warn-script-location", "--disable-pip-version-check"]
    subprocess.run(command, stdout=out_file, stderr=err_file)
    out_file.close()
    err_file.close()
    if platform.system() == "Windows":
        subprocess.call(["cls"], shell=True)
    else:
        subprocess.call(["clear"], shell=True)
