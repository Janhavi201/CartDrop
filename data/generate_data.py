import pandas as pd
import numpy as np

np.random.seed(42)

rows = 50000

data = {
    "session_duration": np.random.randint(1, 60, rows),
    "cart_value": np.random.randint(100, 15000, rows),
    "product_views": np.random.randint(1, 100, rows),
    "return_velocity": np.random.uniform(0, 10, rows),
    "scroll_changes": np.random.randint(0, 50, rows),
    "revisit_count": np.random.randint(0, 20, rows),
    "add_to_cart": np.random.randint(0, 10, rows),
    "remove_from_cart": np.random.randint(0, 10, rows),
    "checkout_visits": np.random.randint(0, 5, rows),
    "hover_time": np.random.randint(0, 500, rows),
    "comparison_clicks": np.random.randint(0, 20, rows),
    "wishlist_actions": np.random.randint(0, 10, rows)
}

df = pd.DataFrame(data)

labels = []

for _, row in df.iterrows():

    if row["checkout_visits"] >= 3 and row["cart_value"] > 2000:
        labels.append(2)

    elif row["revisit_count"] > 5 and row["comparison_clicks"] > 3:
        labels.append(1)

    else:
        labels.append(0)

df["target"] = labels

df.to_csv("data/synthetic_sessions.csv", index=False)

print("Dataset Generated Successfully")
print(df.head())