import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)

# Example usage
password = "hacker@123"
hashed_pwd = hash_password(password)
print(f"Hashed Password: {hashed_pwd}")

# Verify Password
print(f"Password Match: {verify_password(password, hashed_pwd)}")
