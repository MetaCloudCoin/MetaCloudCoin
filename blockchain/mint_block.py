import os
import sys
import json
import time

# Add project root to sys.path for GitHub Actions or CLI
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# ⬅️ Now import the updated generator function that returns both hash and metadata
from hash_engine.generate_metadata_hash import generate_metadata_hash

# ⬅️ Get both the hash and full metadata
metadata_hash, full_metadata = generate_metadata_hash()

block = {
    "timestamp": time.time(),
    "metadata_hash": metadata_hash,
    "providers": full_metadata["providers"]
}

# Save as metadata_block.json
with open("docs/metadata_block.json", "w") as f:
    json.dump(block, f, indent=2)

print(f"✅ Generated hash: {block['metadata_hash']}")
print(f"🕒 Timestamp: {block['timestamp']}")
