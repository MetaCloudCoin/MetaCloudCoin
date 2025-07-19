import json
import hashlib
from datetime import datetime

from metadata.fetchers import aws_ip_ranges, azure_status, gcp_ip_ranges

def generate_hash():
    # Fetch metadata from all providers
    aws_data = aws_ip_ranges.fetch_aws_ip_ranges()
    azure_data = azure_status.fetch_azure_status()
    gcp_data = gcp_ip_ranges.fetch_gcp_metadata()

    # Combine data into a unified metadata object
    combined_metadata = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "providers": {
            "aws": aws_data,
            "azure": azure_data,
            "gcp": gcp_data
        }
    }

    # Serialize to JSON (sorted keys for deterministic hashing)
    metadata_json = json.dumps(combined_metadata, sort_keys=True)

    # Compute SHA-256 hash
    metadata_hash = hashlib.sha256(metadata_json.encode("utf-8")).hexdigest()

    return metadata_hash, combined_metadata


