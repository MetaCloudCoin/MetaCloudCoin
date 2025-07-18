import hashlib
import json
from metadata.fetch_aws_ip_ranges import fetch_aws_ip_ranges

def generate_hash():
    data = fetch_aws_ip_ranges()
    raw = json.dumps(data, sort_keys=True).encode('utf-8')
    return hashlib.sha256(raw).hexdigest()
