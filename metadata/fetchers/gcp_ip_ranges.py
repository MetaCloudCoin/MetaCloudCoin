import requests

def fetch_gcp_ip_ranges():
    """
    Fetches Google's public IP ranges metadata.
    Returns:
        dict: JSON with GCP metadata, or error info.
    """
    url = "https://www.gstatic.com/ipranges/cloud.json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
