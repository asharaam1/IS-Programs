def rail_fence_encrypt(text, rails):
    text = text.replace(" ", "")  # remove spaces
    fence = ['' for _ in range(rails)]
    row, step = 0, 1

    for ch in text:
        fence[row] += ch
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step

    return ''.join(fence)

msg = input("Enter message: ")
r = int(input("Enter number of rails: "))

cipher = rail_fence_encrypt(msg, r)
print("Encrypted:", cipher)