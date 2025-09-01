# Step 1: Function to find gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Step 2: Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# --- Input primes ---
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

n = p * q
phi = (p - 1) * (q - 1)

# Choose small e
e = 3
while gcd(e, phi) != 1:
    e += 2

d = mod_inverse(e, phi)

print("Public Key:", (e, n))
print("Private Key:", (d, n))

msg = int(input("Enter message as number (< n): "))

# Encryption & Decryption
cipher = pow(msg, e, n)
plain = pow(cipher, d, n)

print("Encrypted:", cipher)
print("Decrypted:", plain)
