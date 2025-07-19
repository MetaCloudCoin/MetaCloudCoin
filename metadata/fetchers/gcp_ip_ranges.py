import requests
import datetime

def fetch_gcp_metadata():
    url = "https://www.gstatic.com/ipranges/cloud.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "provider": "GCP",
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "data": data
        }
    except Exception as e:
        return {"error": str(e)}

