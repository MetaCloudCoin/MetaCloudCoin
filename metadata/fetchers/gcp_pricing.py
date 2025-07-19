import requests

def fetch_gcp_pricing():
    """
    Fetches the full GCP pricing metadata from Google's pricing calculator.
    Returns:
        dict: JSON response containing metadata, or error info.
    """
    url = "https://cloudpricingcalculator.appspot.com/static/data/pricelist.json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

