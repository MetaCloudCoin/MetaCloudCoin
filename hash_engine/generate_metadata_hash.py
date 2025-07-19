import json
import hashlib
from metadata.fetchers import aws_ip_ranges, azure_status
from datetime import datetime

def generate_metadata_hash():
    # Fetch metadata from providers
    aws_data = aws_ip_ranges.fetch_aws_ip_ranges()
    azure_data = azure_status.fetch_azure_status()

    # Combine metadata
    combined_metadata = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "providers": {
            "aws": aws_data,
            "azure": azure_data,
        }
    }

    # Serialize to JSON (sorted for consistent hashing)
    metadata_json = json.dumps(combined_metadata, sort_keys=True)

    # Compute SHA256 hash
    metadata_hash = hashlib.sha256(metadata_json.encode("utf-8")).hexdigest()

    return metadata_hash, combined_metadata

