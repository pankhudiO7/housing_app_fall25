import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "titanic.csv")

def load_titanic_csv(path):
    records = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append({
                "survived": int(row["survived"]),
                "pclass": int(row["pclass"]),
                "sex": row["sex"],
                "age": float(row["age"]) if row["age"] else None,
                "fare": float(row["fare"]) if row["fare"] else None,
                "embarked": row["embarked"]
            })
    return records

if __name__ == "__main__":
    print("Looking for file at:")
    print(DATA_PATH)

    data = load_titanic_csv(DATA_PATH)
    print("Rows loaded:", len(data))
    print("Sample row:", data[0])
