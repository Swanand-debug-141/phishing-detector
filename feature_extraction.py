import re
import tldextract

def extract_features_from_url(url):
    """
    Extracts numerical features from the given URL.
    """
    features = {}

    # Number of dots in URL
    features["NumDots"] = url.count('.')

    # Number of hyphens in URL
    features["NumDash"] = url.count('-')

    # Length of the URL
    features["UrlLength"] = len(url)

    # Presence of '@' symbol (Phishing URLs often use @ to redirect)
    features["AtSymbol"] = 1 if '@' in url else 0

    # Check if "https" is present in the domain name (bad practice)
    extracted_url = tldextract.extract(url)
    domain = extracted_url.domain
    features["HttpsInHostname"] = 1 if "https" in domain.lower() else 0

    # Length of the hostname
    features["HostnameLength"] = len(extracted_url.domain)

    # Subdomain count
    features["SubdomainLevel"] = url.count('.') - 1

    # Number of query parameters in URL
    features["QueryLength"] = len(url.split('?')[-1]) if '?' in url else 0

    # Presence of IP address instead of domain name (Suspicious)
    features["IpAddress"] = 1 if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", extracted_url.domain) else 0

    # Presence of double slashes after domain (Phishing pattern)
    features["DoubleSlashInPath"] = 1 if '//' in url[7:] else 0

    return features
