import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

DATA_PATH = "ai/deployment_history.csv"
MODEL_PATH = "ai/deployment_model.pkl"

if not os.path.exists(DATA_PATH):
    print("No training data available.")
    exit()

data = pd.read_csv(DATA_PATH)

if len(data) < 5:
    print("Not enough data to train model.")
    exit()

X = data.drop("failed", axis=1)
y = data["failed"]

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

joblib.dump(model, MODEL_PATH)

print("Model trained successfully.")
