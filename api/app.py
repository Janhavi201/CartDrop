from flask import Flask, jsonify, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("training/model.pkl")

LABELS = {
    0: "Abandoning",
    1: "Researching",
    2: "Ready To Buy"
}


@app.route("/")
def home():
    return jsonify({
        "project": "CartDrop",
        "status": "Running"
    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json(force=True)

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    return jsonify({
        "prediction": LABELS[prediction]
    })


if __name__ == "__main__":
    app.run(debug=True)