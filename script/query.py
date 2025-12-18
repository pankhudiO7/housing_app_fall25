import sqlite3
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "titanic.db")
OUTPUT_CSV = os.path.join(BASE_DIR, "data", "titanic_ml.csv")

conn = sqlite3.connect(DB_PATH)

query = """
SELECT survived, pclass, sex, age, fare, embarked
FROM passengers
WHERE age IS NOT NULL AND embarked IS NOT NULL
"""

df = pd.read_sql_query(query, conn)
conn.close()

print("Rows returned:", len(df))
print(df.head())

df.to_csv(OUTPUT_CSV, index=False)
print("ML-ready CSV saved to:", OUTPUT_CSV)

