import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
#edited
DATA_PATH = "ai/deployment_history.csv"
MODEL_PATH = "ai/deployment_model.pkl"

FEATURE_COLUMNS = [
    "lines_changed",
    "files_changed",
    "commit_message_length",
    "commit_hour",
    "churn_rate",
    "previous_failure_rate"
]

# ---------------------------------------------------
# 1️⃣ Ensure Dataset Exists (Auto-create if missing)
# ---------------------------------------------------
if not os.path.exists(DATA_PATH):
    print("Dataset not found. Creating new dataset.")
    df = pd.DataFrame(columns=FEATURE_COLUMNS + ["failed"])
    df.to_csv(DATA_PATH, index=False)

data = pd.read_csv(DATA_PATH)

# ---------------------------------------------------
# 2️⃣ If Not Enough Data → Create Baseline Model
# ---------------------------------------------------
if len(data) < 5:
    print("Not enough data. Creating baseline model.")

    model = RandomForestClassifier(n_estimators=10)

    # 6 feature dummy input
    X_dummy = [
    [0, 0, 0, 0, 0.0, 0.0],
    [1, 1, 1, 1, 1.0, 1.0]
    ]

    y_dummy = [0, 1]

    model.fit(X_dummy, y_dummy)
    joblib.dump(model, MODEL_PATH)

    print("Baseline model created successfully.")
    exit()

# ---------------------------------------------------
# 3️⃣ Normal Training
# ---------------------------------------------------
X = data[FEATURE_COLUMNS]
y = data["failed"]

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

joblib.dump(model, MODEL_PATH)

print("Model trained successfully.")