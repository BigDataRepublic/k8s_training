import psycopg2
import os


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
        )

    def run_query(self, query: str) -> list:
        with self.conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    def close_connection(self):
        self.conn.commit()
        self.conn.close()
