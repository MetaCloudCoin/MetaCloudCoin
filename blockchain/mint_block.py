import os, sys, time, json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from hash_engine.generate_metadata_hash import generate_hash

BLOCK_PATH = "docs/metadata_block.json"
HISTORY_PATH = "docs/metadata_block_history.json"

# Generate current block
new_block = {
    "timestamp": time.time(),
    "metadata_hash": generate_hash()
}

# Load previous block
try:
    with open(BLOCK_PATH, "r") as f:
        old_block = json.load(f)
except FileNotFoundError:
    old_block = None

# Compare hashes
if not old_block or new_block["metadata_hash"] != old_block["metadata_hash"]:
    with open(BLOCK_PATH, "w") as f:
        json.dump(new_block, f, indent=2)

    # Append to history
    try:
        with open(HISTORY_PATH, "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

    history.append(new_block)
    with open(HISTORY_PATH, "w") as f:
        json.dump(history, f, indent=2)

    print("✅ New metadata detected. Block added.")
else:
    print("⏩ No change in metadata. Skipped block.")
