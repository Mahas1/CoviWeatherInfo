import mysql.connector as mysql
host = input("Enter the MySql host: ")
user = input("Enter the MySql user: ")
passwd = input("Enter the MySql password: ")
db = input("Enter the MySql database: ")
connection = mysql.connect(
    host=host,
    user=user,
    passwd=passwd,
    database=db
)

cursor = connection.cursor(buffered=True)
"""Database Schema
Table: covid
Columns:
    - name (varchar(255))
    - location (varchar(255))

Table: weather
Columns:
    - name (varchar(255))
    - city (varchar(255))
"""


def check_connection():
    try:
        connection.ping()
        print("Connection is alive!")
    except mysql.Error:
        print("Connection is dead!")


def create_tables():
    cursor.execute("CREATE TABLE IF NOT EXISTS covid(name VARCHAR(255), location VARCHAR(255))")
    cursor.execute("CREATE TABLE IF NOT EXISTS weather(name VARCHAR(255), city VARCHAR(255))")
    connection.commit()


def add_covid_location():
    name = input("Enter name: ")
    location = input("Enter location: ")
    cursor.execute("SELECT * FROM covid WHERE name=%s", (name,))
    result = cursor.fetchone()
    if result != () and result is not None:
        cursor.execute("UPDATE covid SET location=%s WHERE name=%s", (location, name))
    else:
        cursor.execute("INSERT INTO covid VALUES(%s,%s)", (name, location))
    connection.commit()


def remove_covid_location():
    name = input("Enter name: ")
    cursor.execute("DELETE FROM covid WHERE name=%s", (name,))
    connection.commit()


def fetch_covid_location():
    name = input("Enter name: ")
    cursor.execute("SELECT * FROM covid WHERE name=%s", (name,))
    result = cursor.fetchone()
    if result != () and result is not None:
        return result[1]
    else:
        print("No record found!")


def add_weather_location():
    name = input("Enter name: ")
    city = input("Enter city: ")
    cursor.execute("SELECT * FROM weather WHERE name=%s", (name,))
    result = cursor.fetchone()
    if result != () and result is not None:
        cursor.execute("UPDATE weather SET city=%s WHERE name=%s", (city, name))
    else:
        cursor.execute("INSERT INTO weather VALUES(%s,%s)", (name, city))
    connection.commit()


def remove_weather_location():
    name = input("Enter name: ")
    cursor.execute("DELETE FROM weather WHERE name=%s", (name,))
    connection.commit()


def fetch_weather_location():
    name = input("Enter name: ")
    cursor.execute("SELECT * FROM weather WHERE name=%s", (name,))
    result = cursor.fetchone()
    if result != () and result is not None:
        return result[1]
    else:
        print("No record found!")