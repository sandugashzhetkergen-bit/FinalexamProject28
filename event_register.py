class EventRegister:

    def __init__(self):
        self.registrations = []

    def add_registration(self, registration):

        for reg in self.registrations:

            if reg.event == registration.event and reg.user == registration.user:
                return "Duplicate registration!"

        self.registrations.append(registration)

        return "Registration added"
    def show_registrations(self):
        for reg in self.registrations:
            print(reg.to_dict())