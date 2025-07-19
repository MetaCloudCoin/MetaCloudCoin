import json
from datetime import datetime

def fetch_azure_status():
    """
    Simulates Azure service metadata.
    Replace with real API if available in future.
    """
    return {
        "provider": "Azure",
        "timestamp": datetime.utcnow().isoformat(),
        "services": [
            {"name": "Compute", "status": "Available"},
            {"name": "Storage", "status": "Available"},
            {"name": "Networking", "status": "Available"}
        ],
        "region": "global"
    }
