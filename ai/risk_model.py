import sys
import os
import joblib
import numpy as np
import pandas as pd
from datetime import datetime

MODEL_PATH = "ai/deployment_model.pkl"
DATA_PATH = "ai/deployment_history.csv"
#edited
# If model doesn't exist yet → allow deployment
if not os.path.exists(MODEL_PATH):
    print(0.0)
    exit()

model = joblib.load(MODEL_PATH)

try:
    lines_changed = int(sys.argv[1])
    files_changed = int(sys.argv[2])
    commit_message_length = int(sys.argv[3])
    churn_rate = float(sys.argv[4])
except:
    print(0.0)
    exit()

commit_hour = datetime.now().hour
previous_failure_rate = 0

if os.path.exists(DATA_PATH):
    data = pd.read_csv(DATA_PATH)
    if len(data) > 0:
        previous_failure_rate = data["failed"].mean()

features = np.array([[
    lines_changed,
    files_changed,
    commit_message_length,
    commit_hour,
    churn_rate,
    previous_failure_rate
]])

proba = model.predict_proba(features)

if proba.shape[1] == 1:
    probability = 0.0
else:
    probability = proba[0][1]

print(round(float(probability), 4))