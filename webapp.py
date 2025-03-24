import streamlit as st
import joblib
import pandas as pd
from feature_extraction import extract_features_from_url
from safe_browsing import check_url_with_google

# Load trained model and feature names
model = joblib.load("phishing_model_xgb.pkl")
selected_features = joblib.load("selected_features.pkl")

# 🎨 Styled Web App
st.set_page_config(page_title="Phishing Detector", page_icon="🔍", layout="centered")

st.markdown("<h1>🔍 Phishing Website Detector</h1>", unsafe_allow_html=True)
st.markdown("<h3>Check if a website is safe using AI & Google Safe Browsing</h3>", unsafe_allow_html=True)

# 🌍 User Input for Website URL
url = st.text_input("🌍 Enter Website URL:", "")

if st.button("🚀 Analyze Website"):
    if url:
        with st.spinner("🔄 Checking Google Safe Browsing..."):
            google_result = check_url_with_google(url)

        if google_result == "Phishing":
            st.error("⚠️ **Google Safe Browsing: This URL is Phishing!** ❌")
        elif google_result == "Safe":
            st.success("✅ **Google Safe Browsing: This URL is Safe!**")
        else:
            st.warning("⚠️ Could not check with Google Safe Browsing.")

        # Extract Features Automatically
        extracted_features = extract_features_from_url(url)
        input_data = pd.DataFrame([extracted_features], columns=selected_features)

        # Make Prediction
        prediction = model.predict(input_data)

        # Show AI Model Result
        if prediction[0] == 1:
            st.error("⚠️ **AI Model: This website is Phishing!**")
        else:
            st.success("✅ **AI Model: This website is Legitimate!**")
    else:
        st.warning("⚠️ Please enter a valid website URL.")
