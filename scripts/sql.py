import pymysql


class Sql:
    def __init__(self, host, port: int, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.connect()
        self.create_table()
        try:
            self.get_locations()
        except:
            pass

    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.database,
                                        autocommit=True)
            self.cursor = self.conn.cursor()
        except Exception as e:
            raise e

    def is_connected(self):
        try:
            self.cursor.execute("SELECT 1")
            return True
        except Exception as e:
            if isinstance(e, pymysql.OperationalError) or isinstance(e, AttributeError):
                return False
            else:
                raise e

    def close(self):
        self.cursor.close()
        self.conn.close()

    def execute(self, command):
        try:
            self.cursor.execute(command)
            return self.cursor.fetchall()
        except Exception as e:
            raise e

    def get_locations(self):
        try:
            result = dict(self.execute(f"SELECT name, location FROM {self.database}.locations"))
            return result
        except Exception as e:
            raise e

    def create_table(self):
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS locations (name VARCHAR(255), location VARCHAR(255))")
        except Exception as e:
            raise e

    def add_location(self, name, location):
        try:
            self.cursor.execute(f"INSERT INTO {self.database}.locations VALUES('{name}', '{location}')")
        except Exception as e:
            raise e

    def remove_location(self, name):
        try:
            self.cursor.execute(f"DELETE FROM locations WHERE name='{name}'")
        except Exception as e:
            raise e
