import time
import assets
import mysql.connector as Sql
import json

with open("config.json", "r") as configFile:
    config = json.load(configFile)

host = config.get("myql_hostname")
port = config.get("mysql_hostport")
username = config.get("mysql_username")
password = config.get("mysql_password")
database = config.get("mysql_dbname")

connection = Sql.connect(
    host=host,
    port=port,
    user=username,
    passwd=password,
    database=database,
    autocommit=True
)

if connection.is_connected():
    print("Connected successfully!")

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
    print(response)
    dictionary = {}
    for entry in response:
        dictionary[entry[0]] = entry[1]
    return dictionary


def insert_location():
    name = input(f"{assets.color_green}enter name: {assets.end_color_formatting}")
    location = input("enter location: ")
    cursor.execute(f"INSERT INTO locations VALUES('{name}', '{location}')")
    print(f"{assets.color_green}Done!\n{assets.end_color_formatting}")


def remove_location():
    name = input(f"{assets.color_green}enter your name: {assets.end_color_formatting}")
    cursor.execute(f"DELETE FROM locations WHERE name = '{name}'")
    print(f"{assets.color_green}Done!\n{assets.end_color_formatting}")