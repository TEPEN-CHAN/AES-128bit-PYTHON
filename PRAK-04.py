def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext

# Meminta input dari pengguna untuk aturan substitusi
aturan_substitusi = {}
jumlah_aturan = int(input("Berapa banyak aturan substitusi yang ingin Anda masukkan? "))

for i in range(jumlah_aturan):
    key = input(f"Masukkan karakter plaintext ke-{i+1}: ").upper()
    value = input(f"Masukkan karakter substitusi untuk '{key}': ").upper()
    aturan_substitusi[key] = value

# Meminta input plaintext
plaintext = input("Masukkan plaintext: ").upper()

# Melakukan proses substitusi
ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

# Menampilkan hasil
print(f'Plaintext: {plaintext}')
print(f'Ciphertext: {ciphertext}')
