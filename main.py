"""
    - covid info
    - weather info
    - test internet connection speed
    - system information - cpu, ram and so on
    - Logging
    - joke when user exits
    - make a database with a table for name-location for weather and covid info,
        and a table for name-language for translation
"""

import json
from scripts import sql

if not __name__ == "__main__":
    exit()

with open("mysql_config.json", "r") as sql_config:
    sql_config = json.load(sql_config)
    sql_host = sql_config["host"]
    sql_port = int(sql_config["port"])
    sql_user = sql_config["user"]
    sql_pass = sql_config["password"]
    sql_db = sql_config["database"]

try:
    database = sql.Sql(sql_host, sql_port, sql_user, sql_pass, sql_db)
except Exception as e:
    raise e

print(database.get_locations())