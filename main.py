import avaneesh, karchick, mahas, mysql_funcs


def give_options():
    to_print = karchick.colour_blue("""
    1. Get Covid-19 data for your location
    2. Get Weather data for your location
    3. Add your location to database for Covid data
    4. Add your location to database for Weather data
    5. Test internet connection speed
    6. Exit
    """)
    print(to_print)
    choice = input("Enter your choice: ")
    return choice


karchick.clear_screen()
print(karchick.colour_pink("Welcome to CoviWeatherInfo!"))

while True:
    choice = give_options()
    if choice == "1":
        karchick.clear_screen()
        location = mysql_funcs.fetch_covid_location()
        if location:
            mahas.get_covid_stats(location)
    elif choice == "2":
        karchick.clear_screen()
        location = mysql_funcs.fetch_weather_location()
        if location:
            mahas.get_weather_info(location)
    elif choice == "3":
        karchick.clear_screen()
        mysql_funcs.add_covid_location()
    elif choice == "4":
        karchick.clear_screen()
        mysql_funcs.add_weather_location()
    elif choice == "5":
        karchick.clear_screen()
        avaneesh.test_speed()
    elif choice == "6":
        karchick.clear_screen()
        print(karchick.colour_cyan(mahas.get_dad_joke()))
        print("\nThank you for using CoviWeatherInfo!")
        break
    else:
        karchick.clear_screen()
        print(karchick.colour_red("Invalid choice!"))
        continue
