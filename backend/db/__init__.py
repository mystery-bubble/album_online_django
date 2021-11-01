import psycopg2
import os


class db:
    def __init__(self):
        self.database = os.getenv("SQL_DATABASE")
        self.user = os.getenv("SQL_USER")
        self.password = os.getenv("SQL_PASSWORD")
        self.host = os.getenv("SQL_HOST")
        self.port = os.getenv("SQL_PORT")

        self.conn = self.connectDb()

        print(f"Database version : {self.useDb('SELECT VERSION()')} ")

    def connectDb(self) -> psycopg2.connection:
        return psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )

    def closeDb(self):
        self.conn.close()

    def useDb(self, sql: str):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()
        return cur.fetchall()
