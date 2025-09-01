def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = ""
    for c in key:
        if c not in matrix and c.isalpha():
            matrix += c
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J skipped
        if c not in matrix:
            matrix += c
    return [list(matrix[i:i+5]) for i in range(0, 25, 5)]

def find_position(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

def process_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(c for c in text if c.isalpha())
    pairs, i = [], 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i+1]
            if a == b:  # double letter → insert X
                pairs.append(a + "X")
                i += 1
            else:
                pairs.append(a + b)
                i += 2
        else:
            pairs.append(a + "Z")  # last single letter → add Z
            i += 1
    return pairs

def encrypt_playfair(text, matrix):
    pairs = process_text(text)
    result = ""
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:  # same row
            result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:  # same column
            result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:  # rectangle swap
            result += matrix[r1][c2] + matrix[r2][c1]
    return result

def decrypt_playfair(cipher, matrix):
    pairs = [cipher[i:i+2] for i in range(0, len(cipher), 2)]
    result = ""
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            result += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            result += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    return result

# --- Test ---
key = input("Enter keyword: ")
matrix = generate_matrix(key)
print("Key Matrix:")
for row in matrix:
    print(row)

msg = input("Enter message to encrypt: ")
cipher = encrypt_playfair(msg, matrix)
print("Encrypted:", cipher)

plain = decrypt_playfair(cipher, matrix)
print("Decrypted:", plain)
