import requests

def fetch_azure_status():
    """
    Fetches the Azure service health metadata.
    Returns:
        dict: JSON metadata or error message.
    """
    url = "https://azure.microsoft.com/api/status/en-us/status.json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
