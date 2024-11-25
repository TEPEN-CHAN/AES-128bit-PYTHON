# Fungsi untuk mengonversi teks menjadi tabel biner
def text_to_binary_table(text):
    binary_table = []
    for char in text:
        # Tangani spasi dengan representasi biner 00000000
        if char == ' ':
            binary_code = "00000000"  # Biner untuk spasi
            binary_table.append(("SPASI", binary_code))
        else:
            binary_code = format(ord(char), '08b')  # Mengonversi karakter ke representasi biner 8 bit
            binary_table.append((char.upper(), binary_code))
    for _ in range(8 - len(text)):  # Tambahkan padding jika teks kurang dari 8 karakter
        binary_table.append(("PADDING", "00000000"))
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
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 16, 5, 3, 10, 9, 0, 7, 12],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 14, 3, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 15, 2],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 7, 12, 0, 14, 9, 5, 6]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 8, 15, 1, 14, 9, 10, 3, 12, 5, 0, 11, 4, 2, 6],
        [9, 6, 1, 8, 15, 13, 12, 10, 14, 0, 11, 7, 5, 3, 4, 2],
        [12, 1, 15, 10, 9, 14, 7, 4, 11, 8, 3, 5, 13, 0, 6, 2]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 15, 10, 3, 12, 1, 6, 7, 9, 5, 0, 14, 2, 4],
        [1, 15, 13, 8, 10, 3, 6, 9, 14, 5, 11, 0, 7, 4, 2, 12],
        [9, 14, 2, 6, 3, 1, 11, 8, 7, 4, 15, 10, 5, 13, 12, 0]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 10, 15, 9, 3, 5, 0, 6, 8],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 14, 0],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 9, 10, 4, 5, 3, 0]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 9, 1, 12, 14, 8, 7, 3, 13, 4, 5, 0, 11, 2, 6],
        [9, 14, 15, 5, 1, 8, 7, 4, 10, 3, 12, 2, 11, 6, 13, 0],
        [1, 12, 10, 15, 9, 8, 0, 14, 4, 7, 11, 2, 13, 3, 5, 6]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 15, 8, 6, 2],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 9, 2, 8, 0, 5, 6],
        [8, 12, 7, 1, 14, 2, 13, 11, 5, 4, 10, 3, 9, 15, 6, 0]
    ]
]


# Fungsi untuk S-Box
def s_box(bits):
    output = []
    for i in range(8):
        block = bits[i * 6:(i + 1) * 6]  # Membagi 48 bit menjadi 8 blok 6-bit
        row = int(f"{block[0]}{block[5]}", 2)  # Menentukan baris (bit pertama dan terakhir)
        col = int(''.join(map(str, block[1:5])), 2)  # Menentukan kolom (bit tengah)
        sbox_value = S_BOX[i][row][col]
        output.extend(list(map(int, format(sbox_value, '04b'))))  # Tambahkan hasil ke output
    return output


# Fungsi untuk F menggunakan S-Box dan P-Box
def f_function(R, K):
    E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20,
         21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    R_expanded = permutate(R, E)
    R_xor_K = [r ^ k for r, k in zip(R_expanded, K)]
    s_output = s_box(R_xor_K)
    return s_output


# Fungsi untuk enkripsi DES
def des_encrypt(plaintext_bits, subkeys):
    L, R = plaintext_bits[:32], plaintext_bits[32:]
    results = []

    for i in range(16):
        F_result = f_function(R, subkeys[i])
        new_R = [l ^ f for l, f in zip(L, F_result)]
        results.append((L, R, F_result))
        L = R
        R = new_R

    return results


# Input dari pengguna
plaintext = input("Masukkan plaintext (maksimal 8 karakter, termasuk spasi): ")
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
for i, (L, R, F) in enumerate(results, 1):
    print(f"\nPutaran {i}:")
    print(f"L{i}: {' '.join(map(str, L))}")
    print(f"R{i}: {' '.join(map(str, R))}")
    print(f"F{i}: {' '.join(map(str, F))}")

print("\nHasil akhir DES:")
L_final, R_final, F_final = results[-1]
print("L16:", ''.join(map(str, L_final)))
print("R16:", ''.join(map(str, R_final)))
print("F16:", ''.join(map(str, F_final)))
