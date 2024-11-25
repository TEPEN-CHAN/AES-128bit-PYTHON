import numpy as np

# Fungsi untuk mengonversi teks menjadi tabel biner
def text_to_binary_table(text):
    binary_table = []
    for char in text:
        binary_code = format(ord(char), '08b')
        binary_table.append((char.upper(), binary_code))
    for _ in range(8 - len(text)):
        binary_table.append(("SPASI", "00000000"))
    return binary_table

# Fungsi untuk melakukan permutasi berdasarkan tabel
def permutate(bits, table):
    return [bits[i - 1] for i in table]

# Fungsi untuk melakukan pergeseran kiri
def left_shift(bits, n):
    return bits[n:] + bits[:n]

# Fungsi untuk menghasilkan subkunci
def generate_subkeys(key_bits):
    PC_1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]
    PC_2 = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]

    # Step 1: Initial Permutation with PC-1
    permuted_key = permutate(key_bits, PC_1)
    C, D = permuted_key[:28], permuted_key[28:]
    
    print("\nKunci Awal setelah Permutasi PC-1:")
    for i in range(0, 56, 7):
        print(' '.join(map(str, permuted_key[i:i+7])))

    # Step 2: Left Shifts and Subkey Generation with PC-2
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    subkeys = []
    
    for round_num, shift in enumerate(shifts, 1):
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        
        # Gabungkan C dan D setelah pergeseran, lalu permutasi dengan PC-2
        combined = C + D
        subkey = permutate(combined, PC_2)
        subkeys.append(subkey)

        print(f"\nC{round_num}: {' '.join(map(str, C))}")
        print(f"D{round_num}: {' '.join(map(str, D))}")
        print(f"K{round_num}: {' '.join(map(str, subkey))}")

    return subkeys

# Input dari pengguna
plaintext = input("Masukkan plaintext (maksimal 8 karakter): ")
key = input("Masukkan kunci (maksimal 8 karakter): ")

# Konversi plaintext dan key ke bentuk biner
print("\nPlaintext dalam Biner:")
plaintext_binary = text_to_binary_table(plaintext)
for char, binary in plaintext_binary:
    print(f"{char}\t{binary}")

print("\nKunci dalam Biner:")
key_binary = text_to_binary_table(key)
for char, binary in key_binary:
    print(f"{char}\t{binary}")

# Menggabungkan key binary menjadi satu string dan ubah ke dalam bit list
key_str = ''.join(binary for _, binary in key_binary)
key_bits = [int(bit) for bit in key_str]

# Generate subkeys dan tampilkan hasil tiap tahap
subkeys = generate_subkeys(key_bits)
print("\nSubkeys yang Dihasilkan untuk Setiap Putaran:")
for i, subkey in enumerate(subkeys, 1):
    print(f"K{i}: {' '.join(map(str, subkey))}")