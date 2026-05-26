from fastapi import FastAPI
from fastapi.responses import FileResponse

from event_register import EventRegister
from RegistrationChar import RegistrationChart

app = FastAPI()

db = EventRegister()
chart = RegistrationChart("data/registrations.json")


@app.post("/register")
def register(event: str, user: str, status: str = "pending"):
    return db.add(event, user, status)


@app.get("/registrations")
def get_all():
    return db.load()


@app.get("/by-event")
def by_event():
    data = db.load()
    result = {}

    for i in data:
        result.setdefault(i["event"], []).append(i["user"])

    return result


@app.get("/chart")
def chart_route():
    path = chart.create_bar_chart()
    return FileResponse(path, media_type="image/png")