import matplotlib.pyplot as plt
import pandas as pd
import os

class RegistrationChart:

    def __init__(self, file_path):
        self.file_path = file_path

    def create_bar_chart(self):

        df = pd.read_json(self.file_path)

        event_counts = df.groupby("event").size()

        plt.figure(figsize=(8, 5))
        plt.bar(event_counts.index, event_counts.values)

        plt.title("Registrations by Event")
        plt.xlabel("Event")
        plt.ylabel("Participants")

        os.makedirs("charts", exist_ok=True)

        path = "charts/chart.png"
        plt.savefig(path)
        plt.close()

        return path