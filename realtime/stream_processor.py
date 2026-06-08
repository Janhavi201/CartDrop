import time
import random
import joblib
import pandas as pd

from feature_engine import FeatureEngine

# Load trained model
model = joblib.load("training/model.pkl")

# Feature engine
engine = FeatureEngine()

event_types = [
    "scroll",
    "cart",
    "hover",
    "view"
]

labels = {
    0: "Abandoning",
    1: "Researching",
    2: "Ready To Buy"
}

session_count = 1

print(f"\n===== Session {session_count} Started =====\n")

while True:

    # Reset after 100 events
    if len(engine.events) >= 100:

        print(f"\n===== Session {session_count} Ended =====\n")

        session_count += 1

        engine = FeatureEngine()

        print(f"\n===== Session {session_count} Started =====\n")

    # Generate random event
    event = {
        "type": random.choice(event_types)
    }

    engine.add_event(event)

    # Extract features
    features = engine.extract_features()

    df = pd.DataFrame([features])

    prediction = model.predict(df)[0]

    print(
        f"Events: {len(engine.events):3d} | "
        f"Prediction: {labels[prediction]}"
    )

    time.sleep(2)