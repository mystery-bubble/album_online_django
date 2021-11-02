import psycopg2
import os


class db:
    def __init__(self):
        self.conn = psycopg2.connect(
            os.getenv("SQL_URL"), sslmode="require"
        )
        cursor = self.conn.cursor()
        cursor.execute("SELECT VERSION()")
        print([i for i in cursor.fetchone()])
        self.conn.commit()

        cursor.close()


db()
