import streamlit as st
import pandas as pd
import joblib

model = joblib.load("training/model.pkl")

st.title("CartDrop Dashboard")

session_duration = st.slider(
    "Session Duration",
    1,
    60,
    20
)

cart_value = st.slider(
    "Cart Value",
    100,
    15000,
    2000
)

product_views = st.slider(
    "Product Views",
    1,
    100,
    10
)

revisit_count = st.slider(
    "Revisit Count",
    0,
    20,
    2
)

checkout_visits = st.slider(
    "Checkout Visits",
    0,
    5,
    0
)

features = {
    "session_duration": session_duration,
    "cart_value": cart_value,
    "product_views": product_views,
    "return_velocity": 5,
    "scroll_changes": 10,
    "revisit_count": revisit_count,
    "add_to_cart": 2,
    "remove_from_cart": 0,
    "checkout_visits": checkout_visits,
    "hover_time": 100,
    "comparison_clicks": 5,
    "wishlist_actions": 2
}

if st.button("Predict"):

    df = pd.DataFrame([features])

    prediction = model.predict(df)[0]

    labels = {
        0: "Abandoning",
        1: "Researching",
        2: "Ready To Buy"
    }

    st.success(
        f"Prediction: {labels[prediction]}"
    )