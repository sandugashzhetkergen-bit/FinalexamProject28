import json
import os
FILE = "data/registrations.json"
class Registration:
    def __init__(self, event, user, status):
        self.event = event
        self.user = user
        self.status = status

    def to_dict(self):
        return {
            "event": self.event,
            "user": self.user,
            "status": self.status
        }

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)
def save(data):
    os.makedirs(os.path.dirname(FILE), exist_ok=True)
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
def add_registration(event, user, status):
    data = load()
    for reg in data:
        if reg["event"] == event and reg["user"] == user:
            return "Duplicate registration!"

    new_reg = Registration(event, user, status)
    data.append(new_reg.to_dict())

    save(data)
    return "Registration added"