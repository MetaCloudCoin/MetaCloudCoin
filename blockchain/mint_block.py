import os
import sys

# This adds the root MetaCloudCoin directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from hash_engine.generate_metadata_hash import generate_hash
import time
import json


block = {
    "timestamp": time.time(),
    "metadata_hash": generate_hash()
}

# Save as metadata_block.json (for easy use in GitHub Actions)
with open("docs/metadata_block.json", "w") as f:
    json.dump(block, f, indent=2)

print(f"Generated hash: {block['metadata_hash']}")
print(f"Timestamp: {block['timestamp']}")
