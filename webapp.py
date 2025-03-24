import streamlit as st
import joblib
import pandas as pd
from feature_extraction import extract_features_from_url

# Load trained model and feature names
model = joblib.load("phishing_model.pkl")
feature_names = joblib.load("feature_names.pkl")

# 🎨 Custom Streamlit Page Settings
st.set_page_config(page_title="Phishing Detector", page_icon="🔍", layout="centered")

# 🎭 Custom CSS for Advanced Styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #141e30, #243b55);
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-image: url("https://source.unsplash.com/random/1600x900/?technology,security");
        background-size: cover;
        background-repeat: no-repeat;
    }
    .stTextInput>div>div>input {
        font-size: 18px;
        padding: 12px;
        border-radius: 8px;
        border: 2px solid #ff4d4d;
        background-color: #1a1a1a;
        color: white;
    }
    .stButton>button {
        background-color: #ff4d4d;
        color: white;
        font-size: 18px;
        padding: 12px 24px;
        border-radius: 12px;
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #ff0000;
        transform: scale(1.05);
    }
    .result-box {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        margin-top: 20px;
    }
    .safe {
        background-color: #2ecc71;
        color: white;
    }
    .danger {
        background-color: #e74c3c;
        color: white;
    }
    h1, h3 {
        text-align: center;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 🔍 Page Title
st.markdown("<h1>🔍 Phishing Website Detector</h1>", unsafe_allow_html=True)
st.markdown("<h3>Check if a website is safe or a phishing attempt.</h3>", unsafe_allow_html=True)

# 🌍 User Input for Website URL
url = st.text_input("🌍 Enter Website URL:", "")

# 🚀 Check Button
if st.button("🚀 Analyze Website"):
    if url:
        with st.spinner("🔄 Scanning the website..."):
            # Extract Features Automatically
            extracted_features = extract_features_from_url(url)
            input_data = pd.DataFrame([extracted_features], columns=feature_names)

            # Make Prediction
            prediction = model.predict(input_data)

        # 🛑 Show Result in Beautiful Box
        if prediction[0] == 1:
            st.markdown('<div class="result-box danger">⚠️ This website is **Phishing!** ❌</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-box safe">✅ This website is **Legitimate!** 🎉</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter a valid website URL.")

# Run with: streamlit run webapp.py
