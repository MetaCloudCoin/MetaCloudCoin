import os
import sys
import json
from datetime import datetime
from hash_engine.generate_metadata_hash import generate_hash

# Set path for GitHub Actions (if needed)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Generate fresh metadata
metadata_hash, combined_metadata = generate_hash()

block = {
    "timestamp": combined_metadata["timestamp"],
    "metadata_hash": metadata_hash,
    "providers": combined_metadata["providers"],
    "region": "global"
}

# Overwrite full chain history with just this one block
with open("docs/metadata_block_history.json", "w") as f:
    json.dump([block], f, indent=2)

print("✅ Chain reset with a single valid block.")
print(f"Metadata hash: {metadata_hash}")

