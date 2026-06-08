import pandas as pd
import joblib
import matplotlib.pyplot as plt

model = joblib.load("training/model.pkl")

df = pd.read_csv("data/synthetic_sessions.csv")

X = df.drop("target", axis=1)

importance = model.feature_importances_

feature_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

feature_df = feature_df.sort_values(
    by="Importance",
    ascending=False
)

print(feature_df)

plt.figure(figsize=(10,6))

plt.barh(
    feature_df["Feature"],
    feature_df["Importance"]
)

plt.xlabel("Importance")
plt.ylabel("Features")
plt.title("Random Forest Feature Importance")

plt.tight_layout()
plt.show()