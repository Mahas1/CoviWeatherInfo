import speedtest


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
            print("Download speed:{:.2f} Mb/s".format(speed.download() / 1024 / 1024))
        elif choice == 2:
            print('Counting...')
            print("Upload speed:{:.2f} Mb/s".format(speed.upload() / 1024 / 1024))
        elif choice == 3:
            print('Exiting the program')
            return
        else:
            print("Please choose the right option")

