from hash_engine.generate_metadata_hash import generate_hash

def test_generate_hash():
    hash_val = generate_hash()
    assert len(hash_val) == 64
