import pandas as pd
import os

ALERT_FILE = "reports/alerts.csv"
alerts_history = []


def generate_alert(message, severity):

    alert = {
        "Severity": severity,
        "Message": message
    }

    print(f"[{severity}] {message}")

    df = pd.DataFrame([alert])

    if os.path.exists(ALERT_FILE):

        df.to_csv(
            ALERT_FILE,
            mode="a",
            header=False,
            index=False
        )

    else:

        df.to_csv(
            ALERT_FILE,
            index=False
        )
def get_alerts():

    return alerts_history