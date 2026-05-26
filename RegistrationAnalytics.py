import pandas as pd
class RegistrationAnalytics:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    # барлық data
    def show_data(self):
        print(self.df)

    # status count
    def status_conversion(self):

        print("\nStatus conversion:\n")

        print(self.df["status"].value_counts())

    # event бойынша groupby
    def group_by_event(self):

        print("\nGroup by event:\n")

        grouped = self.df.groupby("event").size()

        print(grouped)

    # event + status
    def event_status_analysis(self):

        print("\nEvent + status analysis:\n")

        result = self.df.groupby("event")["status"].value_counts()

        print(result)