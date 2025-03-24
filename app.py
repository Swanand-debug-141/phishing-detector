from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the new XGBoost model and selected features
model = joblib.load("phishing_model_xgb.pkl")
selected_features = joblib.load("selected_features.pkl")

# Define Flask App
app = Flask(__name__)

@app.route('/')
def home():
    return "Phishing Website Detection API is Running with XGBoost!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        # Convert input to DataFrame with selected features
        input_data = pd.DataFrame([data], columns=selected_features)

        # Make prediction
        prediction = model.predict(input_data)

        result = {"prediction": "Phishing" if prediction[0] == 1 else "Legitimate"}
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
