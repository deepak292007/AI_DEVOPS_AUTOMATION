import csv
import os
from datetime import datetime

DATA_PATH = "ai/deployment_history.csv"

def log_deployment(
    lines_changed,
    files_changed,
    commit_message_length,
    churn_rate,
    failed
):
    file_exists = os.path.isfile(DATA_PATH)

    commit_hour = datetime.now().hour
    previous_failure_rate = 0

    if file_exists:
        with open(DATA_PATH, "r") as f:
            reader = list(csv.DictReader(f))
            if len(reader) > 0:
                failures = sum(int(row["failed"]) for row in reader)
                previous_failure_rate = failures / len(reader)

    with open(DATA_PATH, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "lines_changed",
                "files_changed",
                "commit_message_length",
                "commit_hour",
                "churn_rate",
                "previous_failure_rate",
                "failed"
            ])

        writer.writerow([
            lines_changed,
            files_changed,
            commit_message_length,
            commit_hour,
            churn_rate,
            previous_failure_rate,
            failed
        ])
