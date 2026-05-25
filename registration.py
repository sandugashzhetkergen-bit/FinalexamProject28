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