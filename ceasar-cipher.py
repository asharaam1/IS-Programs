
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(cipher, shift):
    return caesar_encrypt(cipher, -shift)

# Input
message = input("Enter message: ")
shift = int(input("Enter shift (0-25): "))

# Output
encrypted_msg = caesar_encrypt(message, shift)
decrypted_msg = caesar_decrypt(encrypted_msg, shift)

print("Encrypted:", encrypted_msg)
print("Decrypted:", decrypted_msg)