import json
import hashlib
import os

def validate_chain(history_path):
    if not os.path.exists(history_path):
        print("❌ metadata_block_history.json not found.")
        return

    with open(history_path, "r") as f:
        history = json.load(f)

    for i, block in enumerate(history):
        if "providers" not in block:
            print(f"⚠️ Skipping legacy block at index {i} (no providers)")
            continue

        try:
            canonical = json.dumps({
                "timestamp": block["timestamp"],
                "providers": block["providers"]
            }, sort_keys=True)

            actual_hash = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
            expected_hash = block["metadata_hash"]

            if actual_hash != expected_hash:
                print(f"❌ Tampered block at index {i} - hash mismatch!")
                print(f"Expected: {expected_hash}")
                print(f"Actual:   {actual_hash}")
                return

        except KeyError as e:
            print(f"❌ Missing key {e} in block at index {i}")
            return

    print("✅ Chain is valid — all hashes match and no tampering detected.")

if __name__ == "__main__":
    validate_chain("docs/metadata_block_history.json")

