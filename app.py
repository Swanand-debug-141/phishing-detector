from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the trained model and feature names
model = joblib.load("phishing_model.pkl")
feature_names = joblib.load("feature_names.pkl")  # Load feature names from training

# Define Flask App
app = Flask(__name__)

@app.route('/')
def home():
    return "Phishing Website Detection API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        # Convert input to DataFrame with correct feature names
        input_data = pd.DataFrame([data], columns=feature_names)

        # Make prediction
        prediction = model.predict(input_data)

        result = {"prediction": "Phishing" if prediction[0] == 1 else "Legitimate"}
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
