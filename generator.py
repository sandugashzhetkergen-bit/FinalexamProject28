from faker import Faker
from registration import Registration

fake = Faker()

events = ["Python Workshop", "AI Conference", "Hackathon"]

statuses = ["approved", "pending", "rejected"]


def generate(register, count=20):

    for _ in range(count):

        reg = Registration(
            event=fake.random_element(events),
            user=fake.name(),
            status=fake.random_element(statuses)
        )
        register.add_registration(reg)