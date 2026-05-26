from registration import add_registration

if __name__ == "__main__":
    print(add_registration("Python Workshop", "Ali", "pending"))
    print(add_registration("Python Workshop", "Ali", "pending"))  # дубль
    print(add_registration("AI Conference", "Dana", "approved"))

import json

from registration import Registration
from event_register import EventRegister
app = EventRegister()
# JSON оқу
with open("data/registrations.json", "r") as file:
    data = json.load(file)

# JSON -> object
for item in data:

    reg = Registration(
        item["event"],
        item["user"],
        item["status"]
    )
    print(app.add_registration(reg))
print("\nAll registrations:\n")
app.show_registrations()

from event_register import EventRegister
from generator import generate
app = EventRegister()

generate(app, 10)

print("\nAll registrations:\n")

app.show_registrations()

from RegistrationAnalytics import RegistrationAnalytics


analytics = RegistrationAnalytics("data/registrations.csv")


analytics.show_data()

analytics.status_conversion()

analytics.group_by_event()

analytics.event_status_analysis()

import uvicorn

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)