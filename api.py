from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/registrations")
def get_all():
    df = pd.read_csv("data/registrations.csv")
    return df.to_dict(orient="records")


@app.get("/stats")
def get_stats():
    df = pd.read_csv("data/registrations.csv")
    return df.groupby("event").size().to_dict()