import pandas as pd
import matplotlib.pyplot as plt
import os

def stats(filename="data/registrations.csv"):
    df = pd.read_csv(filename)

    result = df.groupby("event").size()

    result.plot(kind="bar")
    plt.title("Events statistics")

    os.makedirs("charts", exist_ok=True)

    plt.savefig("charts/events.png")

    return result.to_dict()