from fastapi import FastAPI
from fastapi.responses import FileResponse
from event_register import EventRegister
from RegistrationChar import RegistrationChart
import json

app = FastAPI()

register = EventRegister()


# Главная страница
@app.get("/")
def home():
    return {
        "message": "Event Registration API is working"
    }


# Все регистрации
@app.get("/registrations")
def get_registrations():

    with open("data/registrations.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


# Добавить регистрацию
@app.post("/register")
def add_registration(event: str, user: str, status: str):

    result = register.add_registration(event, user, status)

    return {
        "result": result
    }


# Скачать JSON файл
@app.get("/download-json")
def download_json():

    return FileResponse(
        "data/registrations.json",
        media_type="application/json",
        filename="registrations.json"
    )


# График регистраций
@app.get("/chart")
def get_chart():

    chart = RegistrationChart("data/registrations.json")

    chart_path = chart.create_bar_chart()

    return FileResponse(
        chart_path,
        media_type="image/png",
        filename="chart.png"
    )