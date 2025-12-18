import sqlite3
import os
from parse import load_titanic_csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "titanic.db")
CSV_PATH = os.path.join(BASE_DIR, "data", "titanic.csv")

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passengers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            survived INTEGER,
            pclass INTEGER,
            sex TEXT,
            age REAL,
            fare REAL,
            embarked TEXT
        )
    """)
    conn.commit()

def insert_data(conn, records):
    cursor = conn.cursor()
    for r in records:
        cursor.execute("""
            INSERT INTO passengers
            (survived, pclass, sex, age, fare, embarked)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            r["survived"],
            r["pclass"],
            r["sex"],
            r["age"],
            r["fare"],
            r["embarked"]
        ))
    conn.commit()

if __name__ == "__main__":
    print("Creating database...")

    records = load_titanic_csv(CSV_PATH)

    conn = sqlite3.connect(DB_PATH)
    create_tables(conn)
    insert_data(conn, records)
    conn.close()

    print("Database created successfully at:")
    print(DB_PATH)
