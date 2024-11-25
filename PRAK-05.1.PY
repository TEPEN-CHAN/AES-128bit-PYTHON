# def generate_key(plaintext, key):
#     key = list(key)
#     if len(plaintext) == len(key):
#         return key
#     else:
#         for i in range(len(plaintext) - len(key)):
#             key.append(key[i % len(key)])
#     return "".join(key)

# def encrypt_vigenere(plaintext, key):
#     ciphertext = []
#     for i in range(len(plaintext)):
#         p = ord(plaintext[i].upper()) - ord('A')
#         k = ord(key[i].upper()) - ord('A')
#         c = (p + k) % 26
#         ciphertext.append(chr(c + ord('A')))
#     return "".join(ciphertext)

# def decrypt_vigenere(ciphertext, key):
#     plaintext = []
#     for i in range(len(ciphertext)):
#         c = ord(ciphertext[i].upper()) - ord('A')
#         k = ord(key[i].upper()) - ord('A')
#         p = (c - k + 26) % 26
#         plaintext.append(chr(p + ord('A')))
#     return "".join(plaintext)

# # Input
# plaintext = "UNIKASANTOTHOMAS"
# key = "MEDAN"

# # Generate the key
# generated_key = generate_key(plaintext, key)

# # Encrypt the plaintext
# ciphertext = encrypt_vigenere(plaintext, generated_key)
# print(f"Ciphertext: {ciphertext}")

# # Decrypt the ciphertext
# decrypted_text = decrypt_vigenere(ciphertext, generated_key)
# print(f"Decrypted Text: {decrypted_text}")

def generate_key(plaintext, key):
    key = list(key)
    if len(plaintext) == len(key):
        return key
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(plaintext, key):
    print("\nProses Enkripsi:")
    ciphertext = []
    for i in range(len(plaintext)):
        p = ord(plaintext[i].upper()) - ord('A')
        k = ord(key[i].upper()) - ord('A')
        c = (p + k) % 26
        ciphertext.append(chr(c + ord('A')))
        print(f"Step {i+1}: (plaintext: {plaintext[i].upper()}, key: {key[i].upper()}) -> "
              f"p: {p}, k: {k}, c: {(p + k) % 26} -> cipher: {ciphertext[-1]}")
    return "".join(ciphertext)

# Input dari pengguna
plaintext = input("Masukkan plaintext: ").replace(" ", "").upper()
key = input("Masukkan kunci: ").replace(" ", "").upper()

# Generate the key
generated_key = generate_key(plaintext, key)

# Encrypt the plaintext
ciphertext = encrypt_vigenere(plaintext, generated_key)
print(f"\nHasil Ciphertext: {ciphertext}")

