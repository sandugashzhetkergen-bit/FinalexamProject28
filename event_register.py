class EventRegister:
    def __init__(self):
        self.registrations = []

    def add(self, reg):
        for r in self.registrations:
            if r.event == reg.event and r.user == reg.user:
                return "DUPLICATE"

        self.registrations.append(reg)
        return "OK"

    def get_all(self):
        return [r.to_dict() for r in self.registrations]