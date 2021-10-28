import json

import mysql.connector as Sql

import assets

with open("config.json", "r") as configFile:
    config = json.load(configFile)

host = config.get("myql_hostname")
port = config.get("mysql_hostport")
username = config.get("mysql_username")
password = config.get("mysql_password")
database = config.get("mysql_dbname")
try:
    connection = Sql.connect(
        host=host,
        port=port,
        user=username,
        passwd=password,
        database=database,
        autocommit=True
    )
except Exception as e:
    print(f"An error occured: {str(e)}")
    print(f"{assets.color_red}COULD NOT CONNECT TO DATABASE. ABORTING...{assets.end_color_formatting}")
    exit(1)

if connection and connection.is_connected():
    print("Connected to database successfully!")

cursor = connection.cursor(buffered=True)


# while True:
#     command = input("> ")
#     if command == "exit":
#         connection.close()
#         break
#     try:
#         cursor.execute(command)
#         print(cursor.fetchall())
#     except Exception as e:
#         print(str(e))

def get_locations():
    cursor.execute("SELECT * FROM locations;")
    response = cursor.fetchall()
    dictionary = {}
    for entry in response:
        dictionary[entry[0]] = entry[1]
    return dictionary


def insert_location():
    name = input(f"{assets.color_green}Enter your name: {assets.end_color_formatting}")
    location = input("enter location: ")
    cursor.execute(f"DELETE FROM locations WHERE name = '{name}'")  # deleting already existing entry
    cursor.execute(f"INSERT INTO locations VALUES('{name}', '{location}')")
    print(f"{assets.color_green}Done!\n{assets.end_color_formatting}")


def remove_location():
    name = input(f"{assets.color_green}Enter your name: {assets.end_color_formatting}")
    cursor.execute(f"DELETE FROM locations WHERE name = '{name}'")
    print(f"{assets.color_green}Done!\n{assets.end_color_formatting}")


def retrieve_location():
    name = input(f"{assets.color_green}Enter your name: {assets.end_color_formatting}")
    print("\n")
    cursor.execute(f"SELECT location FROM locations WHERE name = '{name}'")
    result = (cursor.fetchall())
    if len(result) > 0:
        print(result[0][0], "\n")
        return result[0][0]
    else:
        print("No results found\n")
