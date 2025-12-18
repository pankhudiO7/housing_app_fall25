from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import os

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "titanic_model.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

app = FastAPI(title="Titanic Prediction API")

# Define input schema
class Passenger(BaseModel):
    pclass: int
    sex: str
    age: float
    fare: float
    embarked: str

class Payload(BaseModel):
    instances: list[Passenger]

# Prediction endpoint
@app.post("/predict")
def predict(payload: Payload):
    df = pd.DataFrame([p.dict() for p in payload.instances])
    
    # Encode 'sex' and 'embarked' manually if needed
    df['sex'] = df['sex'].map({'male': 0, 'female': 1})
    df['embarked'] = df['embarked'].map({'S':0, 'C':1, 'Q':2})
    
    preds = model.predict(df)
    return {"predictions": preds.tolist()}
