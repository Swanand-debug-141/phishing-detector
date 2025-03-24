import requests
import os

# Load API Key from environment variable (More Secure)
GOOGLE_API_KEY = os.getenv("GOOGLE_SAFE_BROWSING_API_KEY")

def check_url_with_google(url):
    """
    Check if the URL is safe using Google Safe Browsing API.
    Returns 'Safe' if no threat is detected, otherwise returns 'Phishing'.
    """

    api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={GOOGLE_API_KEY}"

    payload = {
        "client": {
            "clientId": "phishing-detector",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        result = response.json()
        if "matches" in result:
            return "Phishing"
        else:
            return "Safe"
    else:
        return "Error checking URL"
