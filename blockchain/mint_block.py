from hash_engine.generate_metadata_hash import generate_hash
import time
import json

block = {
    "timestamp": time.time(),
    "metadata_hash": generate_hash()
}

with open("docs/metadata_block.json", "w") as f:
    json.dump(block, f, indent=2)

print(f"Generated hash: {block['metadata_hash']}")
print(f"Timestamp: {block['timestamp']}")
