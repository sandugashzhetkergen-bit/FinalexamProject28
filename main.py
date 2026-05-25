from registration import Registration
from event_register import EventRegister
from generator import generate
from services import save_json
from analytics import stats
import pandas as pd
import os


def save_csv(data):
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv("data/registrations.csv", index=False)


def main():
    system = EventRegister()

    system.add(Registration("Python Workshop", "Ali", "approved"))
    system.add(Registration("AI Conference", "Dana", "pending"))

    generate(system, 30)

    data = system.get_all()

    save_json(data)
    save_csv(data)

    print("PROJECT RUN SUCCESS ✅")

    stats()


if __name__ == "__main__":
    main()