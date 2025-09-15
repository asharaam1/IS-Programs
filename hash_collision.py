import hashlib

def check_hash_collision(data1, data2, algorithm):
    hash1 = hashlib.new(algorithm)
    hash1.update(data1.encode())

    hash2 = hashlib.new(algorithm)
    hash2.update(data2.encode())

    return hash1.hexdigest(), hash2.hexdigest(), hash1.hexdigest() == hash2.hexdigest()

# Example usage
data1 = "hello123"
data2 = "hello124"  # Slightly different input

md5_hash1, md5_hash2, md5_match = check_hash_collision(data1, data2, "md5")
sha256_hash1, sha256_hash2, sha256_match = check_hash_collision(data1, data2, "sha256")

print(f"MD5 Hashes:\n {md5_hash1}\n {md5_hash2}\n Collision: {md5_match}")
print(f"SHA-256 Hashes:\n {sha256_hash1}\n {sha256_hash2}\n Collision: {sha256_match}")
