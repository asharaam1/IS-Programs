import hashlib

def calculate_file_hash(file_path, algorithm='sha256'):
    hash_obj = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as file:
        while chunk := file.read(4096):
            hash_obj.update(chunk)

    return hash_obj.hexdigest()

# Example usage
file_path = "file_integrity.txt"
print(f"SHA-256 Hash of file: {calculate_file_hash(file_path, 'sha256')}")
print(f"SHA-512 Hash of file: {calculate_file_hash(file_path, 'sha512')}")
