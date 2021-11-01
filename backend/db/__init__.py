import psycopg2
import os


class db:
    def __init__(self, DATABASE_URL=None):
        self.conn = psycopg2.connect(DATABASE_URL or os.getenv("DATABASE_URL"), sslmode="require")

    def closeDb(self):
        self.conn.close()
