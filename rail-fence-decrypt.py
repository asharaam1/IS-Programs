def rail_fence_decrypt(cipher, rails):
    n = len(cipher)
    pattern = [0] * n
    row, step = 0, 1

    for i in range(n):
        pattern[i] = row
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step

    result = [''] * n
    index = 0
    for r in range(rails):
        for i in range(n):
            if pattern[i] == r:
                result[i] = cipher[index]
                index += 1
    return ''.join(result)

msg = input("Enter encrypted message: ")
r = int(input("Enter number of rails: "))

plain = rail_fence_decrypt(msg, r)
print("Decrypted:", plain)