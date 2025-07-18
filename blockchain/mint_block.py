from hash_engine.generate_metadata_hash import generate_hash
import time

block = {
    'timestamp': time.time(),
    'metadata_hash': generate_hash()
}

print(block)
