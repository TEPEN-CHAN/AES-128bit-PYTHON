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

# Fungsi permutasi berdasarkan tabel
def permutate(bits, table):
    return [bits[i - 1] for i in table]

# Fungsi pergeseran kiri
def left_shift(bits, n):
    return bits[n:] + bits[:n]

# Fungsi untuk menghasilkan subkunci
def generate_subkeys(key_bits):
    PC_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 
            63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    PC_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 
            55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    permuted_key = permutate(key_bits, PC_1)
    C, D = permuted_key[:28], permuted_key[28:]
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    subkeys = []

    for shift in shifts:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        combined = C + D
        subkey = permutate(combined, PC_2)
        subkeys.append(subkey)

    return subkeys

# Tabel S-Box
S_BOX = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    
    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]


# Fungsi F menggunakan S-Box
def f_function(R, K):
    E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 
         21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    R_expanded = permutate(R, E)
    R_xor_K = [r ^ k for r, k in zip(R_expanded, K)]
    s_output = []  # Hasil S-Box

    for i in range(8):
        block = R_xor_K[i*6:(i+1)*6]
        row = int(f"{block[0]}{block[5]}", 2)
        col = int(''.join(map(str, block[1:5])), 2)
        sbox_value = S_BOX[i][row][col]
        s_output += [int(x) for x in format(sbox_value, '04b')]

    return s_output

# DES dengan putaran untuk L1 hingga L16 dan R1 hingga R16
def des_encrypt(plaintext_bits, subkeys):
    L, R = plaintext_bits[:32], plaintext_bits[32:]
    results = []

    for i in range(16):
        F_result = f_function(R, subkeys[i])
        new_R = [l ^ f for l, f in zip(L, F_result)]
        results.append((L, R, F_result))  # Menyimpan hasil L, R, dan S-Box tiap putaran
        L = R
        R = new_R

    return results

# Input dari pengguna
plaintext = input("Masukkan plaintext (maksimal 8 karakter): ")
key = input("Masukkan kunci (maksimal 8 karakter): ")

# Konversi plaintext dan key ke bentuk biner
plaintext_binary = text_to_binary_table(plaintext)
key_binary = text_to_binary_table(key)

# Menggabungkan key binary menjadi satu string dan ubah ke dalam bit list
key_str = ''.join(binary for _, binary in key_binary)
key_bits = [int(bit) for bit in key_str]

# Generate subkeys
subkeys = generate_subkeys(key_bits)

# Enkripsi DES dan tampilkan hasil L dan R tiap putaran
plaintext_bits = [int(bit) for _, binary in plaintext_binary for bit in binary]
results = des_encrypt(plaintext_bits, subkeys)

print("\nHasil L1-R1 hingga L16-R16 setiap putaran:")
for i, (L, R, S) in enumerate(results, 1):
    print(f"\nPutaran {i}:")
    print(f"L{i}: {' '.join(map(str, L))}")
    print(f"R{i}: {' '.join(map(str, R))}")
    print(f"S{i}: {' '.join(map(str, S))}")

print("\nHasil akhir DES:")
L_final, R_final, S_final = results[-1]
print("L16:", ''.join(map(str, L_final)))
print("R16:", ''.join(map(str, R_final)))
print("S16:", ''.join(map(str, S_final)))