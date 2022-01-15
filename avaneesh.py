import speedtest
import karchick


def test_speed():
    speed = speedtest.Speedtest()
    while True:
        choice = int(input("""Check you connection speed:
    1)Download speed
    2)Upload speed
    3)Exit

Choice(1/2/3):"""))
        if choice == 1:
            print('Counting...')
            print(karchick.colour_cyan("Download speed:{:.2f} Mb/s".format(speed.download() / 1024 / 1024)))
        elif choice == 2:
            print('Counting...')
            print(karchick.colour_cyan("Upload speed:{:.2f} Mb/s".format(speed.upload() / 1024 / 1024)))
        elif choice == 3:
            return
        else:
            print(karchick.colour_red("Please choose the right option"))
