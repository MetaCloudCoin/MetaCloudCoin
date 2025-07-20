import os
import sys
import json
import time
from datetime import datetime

# Ensure project root is in path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from hash_engine.generate_metadata_hash import generate_hash

# Generate metadata
metadata_hash, metadata = generate_hash()

block = {
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "metadata_hash": metadata_hash,
    "providers": metadata["providers"]
}

# 🔄 Corrected to match GitHub repo filename
history_path = os.path.join(project_root, "docs", "metadata_block_history.json")

# Load or initialize history
if os.path.exists(history_path):
    with open(history_path, "r") as f:
        history = json.load(f)
else:
    history = []

# Append new block
history.append(block)

# Save back to history file
with open(history_path, "w") as f:
    json.dump(history, f, indent=2)

# Optional: update current block too
with open(os.path.join(project_root, "docs", "metadata_block.json"), "w") as f:
    json.dump(block, f, indent=2)

print("✅ New metadata block appended to metadata_block_history.json")
print(f"Metadata hash: {metadata_hash}")

