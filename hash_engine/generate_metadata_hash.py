import json
from metadata.fetchers.aws_ip_ranges import fetch_aws_ip_ranges
from metadata.fetchers.azure_status import fetch_azure_status
from metadata.fetchers.gcp_pricing import fetch_gcp_pricing
from utils.hash_utils import sha256_hash

def generate_hash():
    metadata = {
        "aws": fetch_aws_ip_ranges(),
        "azure": fetch_azure_status(),
        "gcp": fetch_gcp_pricing()
    }
    metadata_json = json.dumps(metadata, sort_keys=True)
    return sha256_hash(metadata_json)

if __name__ == "__main__":
    print(generate_hash())
