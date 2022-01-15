import mysql.connector as mysql

connection = mysql.connect(
    host="localhost",
    user="root",
    passwd="Maha2021$",
    database="coviweatherinfo"
)

cursor = connection.cursor()

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


def create_tables():
    cursor.execute("CREATE TABLE IF NOT EXISTS covid(name VARCHAR(255), location VARCHAR(255))")
    cursor.execute("CREATE TABLE IF NOT EXISTS weather(name VARCHAR(255), city VARCHAR(255))")
    connection.commit()


def add_covid_location():
    name = input("Enter name: ")
    location = input("Enter location: ")
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
        print(result[1])
    else:
        print("No record found!")
