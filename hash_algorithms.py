import hashlib

def generate_hash(data, algorithm):
    hash_obj = hashlib.new(algorithm)
    hash_obj.update(data.encode("utf-8"))
    return hash_obj.hexdigest()

# Example usage
data = "Hello, Cybersecurity!"
algorithms = ["sha256", "sha512", "blake2b", "sha3_256"]

for algo in algorithms:
    print(f"{algo.upper()} Hash: {generate_hash(data, algo)}")