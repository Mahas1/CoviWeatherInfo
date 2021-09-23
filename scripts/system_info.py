import platform
import psutil
import assets
import os


def hostinfo():
    system = platform.uname()
    cpu_usage = psutil.cpu_percent()
    memstats = psutil.virtual_memory()
    memUsedGB = "{0:.1f}".format(((memstats.used / 1024) / 1024) / 1024)
    memTotalGB = "{0:.1f}".format(((memstats.total / 1024) / 1024) / 1024)
    processor = str(system.processor) if str(system.processor) != "" else "N/A"

    print(f"Host Name: {assets.color_blue}{system.node}{assets.end_color_formatting}")
    print(f"Platform: {assets.color_blue}{system.system}{assets.end_color_formatting}")
    print(f"OS Version: {assets.color_blue}{system.version}{assets.end_color_formatting}")
    print(f"Release: {assets.color_blue}{system.release}{assets.end_color_formatting}")
    print(f"Machine type: {assets.color_blue}{system.machine}{assets.end_color_formatting}")
    print(f"CPU: {assets.color_blue}{processor}{assets.end_color_formatting}")
    print(f"CPU Threads: {assets.color_blue}{os.cpu_count()}{assets.end_color_formatting}")
    print(f"CPU Frequency: {assets.color_blue}{int(list(psutil.cpu_freq())[0])}MHz{assets.end_color_formatting}")
    print(f"CPU Usage: {assets.color_blue}{cpu_usage}%{assets.end_color_formatting}")
    print(
        f"RAM Usage: {assets.color_blue}{memUsedGB} GB{assets.end_color_formatting} of "
        f"{assets.color_blue}{memTotalGB} GB{assets.end_color_formatting} "
        f"{assets.color_pink}({memstats.percent}%){assets.end_color_formatting}")

    print("\n")
