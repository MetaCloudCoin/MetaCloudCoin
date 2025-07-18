from hash_engine.generate_metadata_hash import generate_hash
import time
import json

block = {
    "timestamp": time.time(),
    "metadata_hash": generate_hash()
}

<<<<<<< HEAD
=======
# Save as metadata_block.json (for easy use in GitHub Actions)
>>>>>>> de2493f3517b0b07dc6ed8319935cb5f9f439e8c
with open("docs/metadata_block.json", "w") as f:
    json.dump(block, f, indent=2)

print(f"Generated hash: {block['metadata_hash']}")
print(f"Timestamp: {block['timestamp']}")
<<<<<<< HEAD
=======

>>>>>>> de2493f3517b0b07dc6ed8319935cb5f9f439e8c
