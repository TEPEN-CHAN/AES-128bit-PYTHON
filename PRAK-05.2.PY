def generate_key(plaintext, key):
    key = list(key)
    if len(plaintext) == len(key):
        return key
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def decrypt_vigenere(ciphertext, key):
    print("\nProses Dekripsi:")
    plaintext = []
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i].upper()) - ord('A')
        k = ord(key[i].upper()) - ord('A')
        p = (c - k + 26) % 26
        plaintext.append(chr(p + ord('A')))
        print(f"Step {i+1}: (ciphertext: {ciphertext[i].upper()}, key: {key[i].upper()}) -> "
              f"c: {c}, k: {k}, p: {(c - k + 26) % 26} -> plain: {plaintext[-1]}")
    return "".join(plaintext)

# Input dari pengguna
ciphertext = input("Masukkan ciphertext: ").replace(" ", "").upper()
key = input("Masukkan kunci: ").replace(" ", "").upper()

# Generate the key
generated_key = generate_key(ciphertext, key)

# Decrypt the ciphertext
decrypted_text = decrypt_vigenere(ciphertext, generated_key)
print(f"\nHasil Teks Terdekripsi: {decrypted_text}")
