import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from safe_browsing import check_url_with_google

# 🎨 Streamlit Page Config
st.set_page_config(page_title="Phishing Detector", page_icon="🔍", layout="wide")

# 🔍 App Title & Subtitle
st.markdown("<h1>🔍 Phishing Website Detector</h1>", unsafe_allow_html=True)
st.markdown("<h3>Check if a website is safe using Google Safe Browsing API</h3>", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Dashboard"])

# 🌍 Home Page: URL Checker (Only Google Safe Browsing API)
if page == "Home":
    url = st.text_input("🌍 Enter Website URL:", "")

    if st.button("🚀 Check Website"):
        if url:
            with st.spinner("🔄 Checking Google Safe Browsing..."):
                google_result = check_url_with_google(url)

            # Show Google Safe Browsing result
            if google_result == "Phishing":
                st.error("⚠️ **Google Safe Browsing: This URL is Phishing!** ❌")
            else:
                st.success("✅ **Google Safe Browsing: This URL is Safe!**")
        else:
            st.warning("⚠️ Please enter a valid website URL.")

# 📊 Dashboard Page
elif page == "Dashboard":
    st.header("📊 Phishing Analysis Dashboard")

    # Load sample dataset (Replace this with real-time data if available)
    df = pd.read_csv("dataset.csv")

    # Plot: Distribution of Phishing vs. Legitimate
    fig = px.pie(df, names="CLASS_LABEL", title="Phishing vs. Legitimate Websites", labels={"CLASS_LABEL": "Website Type"})
    st.plotly_chart(fig)

    # Plot: URL Length Distribution
    fig, ax = plt.subplots()
    sns.histplot(df["UrlLength"], bins=30, kde=True, ax=ax)
    ax.set_title("URL Length Distribution")
    st.pyplot(fig)

    # Correlation Heatmap
    st.subheader("📌 Feature Correlation")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), cmap="coolwarm", annot=False, ax=ax)
    st.pyplot(fig)
