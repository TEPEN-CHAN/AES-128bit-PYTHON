# # # def text_to_binary_table(text): 
# # # binary_table = [] 
# # # for char in text: 
# # # binary_code = format(ord(char), '08b') 
# # # binary_table.append((char.upper(), binary_code)) 
# # # for _ in range(8 - len(text)): 
# # # binary_table.append(("SPASI", "00000000")) 
# # # return binary_table 
# # # text = "marto" 
# # # binary_table = text_to_binary_table(text) 
# # # print("Key (huruf kecil)\tBiner") 
# # # for key, biner in binary_table: 
# # # print(f"{key}\t\t{biner}") 

# # # PC_1 = [ 
# # #     57, 49, 41, 33, 25, 17, 9, 
# # #     1, 58, 50, 42, 34, 26, 18, 
# # #     10, 2, 59, 51, 43, 35, 27, 
# # #     19, 11, 3, 60, 52, 44, 36, 
# # #     63, 55, 47, 39, 31, 23, 15, 
# # #     7, 62, 54, 46, 38, 30, 22, 
# # #     14, 6, 61, 53, 45, 37, 29, 
# # #     21, 13, 5, 28, 20, 12, 4 
# # # ] 
 
# # # key_str = 
# # # "0110110101100001011100100111010001101111000000000000000000000
# # #  000" 
# # # key_bits = [int(bit) for bit in key_str] 
# # # permuted_key = [key_bits[pc - 1] for pc in PC_1] 
 
# # # C0 = permuted_key[:28] 
# # # D0 = permuted_key[28:] 
 
# # # print("Kunci Awal:") 
# # # for i in range(0, 64, 8): 
# # #     print(' '.join(map(str, key_bits[i:i + 8]))) 
 
# # # print("\nPermutasi PC-1 (Matriks 8x7):") 
# # # for i in range(0, 56, 7): 
# # #     print(' '.join(map(str, permuted_key[i:i + 7]))) 
 
# # # print("\nC0:") 
# # # for i in range(0, 28, 7): 
# # #     print(' '.join(map(str, C0[i:i + 7]))) 
 
# # # print("\nD0:") 
# # # for i in range(0, 28, 7): 
# # #     print(' '.join(map(str, D0[i:i + 7]))) 
    
# # # PC_1 = [ 
# # #     57, 49, 41, 33, 25, 17, 9, 
# # #     1, 58, 50, 42, 34, 26, 18, 
# # #     10, 2, 59, 51, 43, 35, 27, 
# # #     19, 11, 3, 60, 52, 44, 36, 
# # #     63, 55, 47, 39, 31, 23, 15, 
# # #     7, 62, 54, 46, 38, 30, 22, 
# # #     14, 6, 61, 53, 45, 37, 29, 
# # #     21, 13, 5, 28, 20, 12, 4 
# # # ] 
 
# # # key_str = 
# # # "0110110101100001011100100111010001101111000000000000000000000
# # #  000" 
# # # key_bits = [int(bit) for bit in key_str] 
# # # permuted_key = [key_bits[pc - 1] for pc in PC_1] 
 
# # # C0 = permuted_key[:28] 
# # # D0 = permuted_key[28:] 
 
# # # shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1] 
 
# # # C_values = [C0] 
# # # D_values = [D0] 
 
# # # for shift in shifts: 
# # #     C_prev = C_values[-1] 
# # #     D_prev = D_values[-1] 
     
# # #     C_new = C_prev[shift:] + C_prev[:shift] 
# # #     D_new = D_prev[shift:] + D_prev[:shift] 
     
# # #     C_values.append(C_new) 
# # #     D_values.append(D_new) 
 
# # # # Display C and D values 
# # # for i in range(17): 
# # #     print(f"C{i}:", ' '.join(map(str, C_values[i]))) 
# # #     print(f"D{i}:", ' '.join(map(str, D_values[i])))
    
# # # import numpy as np 
 
# # # PC_2 = np.array([ 
# # #     [14, 17, 11, 24, 1, 5], 
# # #     [3, 28, 15, 6, 21, 10], 
# # #     [23, 19, 12, 4, 26, 8], 
# # #     [16, 7, 27, 20, 13, 2], 
# # #     [41, 52, 31, 37, 47, 55], 
# # #     [30, 40, 51, 45, 33, 48], 
# # #     [44, 49, 39, 56, 34, 53], 
# # #     [46, 42, 50, 36, 29, 32] 
# # # ]) 
 
# # # C_sequences = np.array([ 
# # #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], 
# # #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
# # #     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
# # #     [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# # #     [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# # #     [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# # #     [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# # #     [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
# # #     [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], 
# # #     [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0], 
# # #     [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0], 
# # #     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1], 
# # #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1], 
# # #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0], 
# # #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0], 
# # #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
# # # ]) 
# # # D_sequences = np.array([ 
# # #     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
# # #     [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], 
# # #     [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1], 
# # #     [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1], 
# # #     [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0], 
# # #     [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], 
# # #     [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1], 
# # #     [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0], 
# # #     [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
# # #     [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0], 
# # #     [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0], 
# # #     [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0], 
# # #     [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 
# # #     [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1], 
# # #     [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0], 
# # #     [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0] 
# # # ]) 
 
# # # for i in range(16): 
# # #     combined = np.concatenate((C_sequences[i], 
# # # D_sequences[i]))  # Gabungkan C dan D 
# # # K = [combined[pos - 1] for pos in PC_2.flatten()]  # 
# # # Gunakan PC-2 untuk menghasilkan K 
# # # print(f"C{i+1} = {C_sequences[i]}") 
# # # print(f"D{i+1} = {D_sequences[i]}") 
# # # print(f"K{i+1} = {K}\n")


# import numpy as np

# def text_to_binary_table(text):
#     binary_table = []
#     for char in text:
#         binary_code = format(ord(char), '08b')
#         binary_table.append((char.upper(), binary_code))
#     for _ in range(8 - len(text)):
#         binary_table.append(("SPASI", "00000000"))
#     return binary_table

# def generate_permuted_key(key_str, PC_1):
#     key_bits = [int(bit) for bit in key_str]
#     permuted_key = [key_bits[pc - 1] for pc in PC_1]
#     return permuted_key

# def left_shift(C0, D0, shifts):
#     C_values = [C0]
#     D_values = [D0]
#     for shift in shifts:
#         C_prev = C_values[-1]
#         D_prev = D_values[-1]
#         C_new = C_prev[shift:] + C_prev[:shift]
#         D_new = D_prev[shift:] + D_prev[:shift]
#         C_values.append(C_new)
#         D_values.append(D_new)
#     return C_values, D_values

# def generate_K(C_values, D_values, PC_2):
#     K_values = []
#     for i in range(16):
#         combined = np.concatenate((C_values[i + 1], D_values[i + 1]))
#         K = [combined[pos - 1] for pos in PC_2.flatten()]
#         K_values.append(K)
#     return K_values

# # Input Kunci dari keyboard
# key_str = input("Masukkan kunci (64 bit): ")

# # Permutasi Pilihan 1 (PC-1)
# PC_1 = [
#     57, 49, 41, 33, 25, 17, 9, 
#     1, 58, 50, 42, 34, 26, 18, 
#     10, 2, 59, 51, 43, 35, 27, 
#     19, 11, 3, 60, 52, 44, 36, 
#     63, 55, 47, 39, 31, 23, 15, 
#     7, 62, 54, 46, 38, 30, 22, 
#     14, 6, 61, 53, 45, 37, 29, 
#     21, 13, 5, 28, 20, 12, 4 
# ]

# # Generate permutasi awal dengan PC-1
# permuted_key = generate_permuted_key(key_str, PC_1)
# C0 = permuted_key[:28]
# D0 = permuted_key[28:]

# # Tabel Shifts
# shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# # Generate C dan D values dengan left shift
# C_values, D_values = left_shift(C0, D0, shifts)

# # Permutasi Pilihan 2 (PC-2)
# PC_2 = np.array([
#     [14, 17, 11, 24, 1, 5],
#     [3, 28, 15, 6, 21, 10],
#     [23, 19, 12, 4, 26, 8],
#     [16, 7, 27, 20, 13, 2],
#     [41, 52, 31, 37, 47, 55],
#     [30, 40, 51, 45, 33, 48],
#     [44, 49, 39, 56, 34, 53],
#     [46, 42, 50, 36, 29, 32]
# ])

# # Generate nilai K
# K_values = generate_K(C_values, D_values, PC_2)

# # Tampilkan hasil
# print("\nKey (huruf kecil)\tBiner")
# binary_table = text_to_binary_table(key_str)
# for key, biner in binary_table:
#     print(f"{key}\t\t{biner}")

# print("\nKunci Awal:")
# for i in range(0, 64, 8):
#     print(' '.join(key_str[i:i + 8]))

# print("\nPermutasi PC-1 (Matriks 8x7):")
# for i in range(0, 56, 7):
#     print(' '.join(map(str, permuted_key[i:i + 7])))

# print("\nC dan D values setelah left shift:")
# for i in range(17):
#     print(f"C{i}: {' '.join(map(str, C_values[i]))}")
#     print(f"D{i}: {' '.join(map(str, D_values[i]))}")

# print("\nNilai K setelah permutasi PC-2:")
# for i, K in enumerate(K_values, start=1):
#     print(f"K{i} = {' '.join(map(str, K))}")

import numpy as np

def text_to_binary_table(text):
    binary_table = []
    for char in text:
        binary_code = format(ord(char), '08b')
        binary_table.append((char.upper(), binary_code))
    # Jika teks kurang dari 8 karakter, tambahkan "SPASI" dengan "00000000" untuk mencapai 64 bit
    for _ in range(8 - len(text)):
        binary_table.append(("SPASI", "00000000"))
    return binary_table

def generate_permuted_key(key_str, PC_1):
    key_bits = [int(bit) for bit in key_str]
    permuted_key = [key_bits[pc - 1] for pc in PC_1]
    return permuted_key

def left_shift(C0, D0, shifts):
    C_values = [C0]
    D_values = [D0]
    for shift in shifts:
        C_prev = C_values[-1]
        D_prev = D_values[-1]
        C_new = C_prev[shift:] + C_prev[:shift]
        D_new = D_prev[shift:] + D_prev[:shift]
        C_values.append(C_new)
        D_values.append(D_new)
    return C_values, D_values

def generate_K(C_values, D_values, PC_2):
    K_values = []
    for i in range(16):
        combined = np.concatenate((C_values[i + 1], D_values[i + 1]))
        K = [combined[pos - 1] for pos in PC_2.flatten()]
        K_values.append(K)
    return K_values

# Input kunci dari pengguna (teks, hingga 8 karakter)
key_text = input("Masukkan kunci teks (hingga 8 karakter): ")
binary_key = ''.join(format(ord(char), '08b') for char in key_text[:8])

# Tambahkan 0 untuk mengisi jika kunci kurang dari 64 bit
binary_key = binary_key.ljust(64, '0')

# Tampilkan tabel biner
binary_table = text_to_binary_table(key_text)
print("\nKey (huruf kecil)\tBiner")
for key, biner in binary_table:
    print(f"{key}\t\t{biner}")

# Permutasi Pilihan 1 (PC-1)
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

# Generate permutasi awal dengan PC-1
permuted_key = generate_permuted_key(binary_key, PC_1)
C0 = permuted_key[:28]
D0 = permuted_key[28:]

# Tabel Shifts
shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Generate C dan D values dengan left shift
C_values, D_values = left_shift(C0, D0, shifts)

# Permutasi Pilihan 2 (PC-2)
PC_2 = np.array([
    [14, 17, 11, 24, 1, 5],
    [3, 28, 15, 6, 21, 10],
    [23, 19, 12, 4, 26, 8],
    [16, 7, 27, 20, 13, 2],
    [41, 52, 31, 37, 47, 55],
    [30, 40, 51, 45, 33, 48],
    [44, 49, 39, 56, 34, 53],
    [46, 42, 50, 36, 29, 32]
])

# Generate nilai K
K_values = generate_K(C_values, D_values, PC_2)

# Tampilkan hasil
print("\nKunci Awal (dalam biner, 64 bit):")
for i in range(0, 64, 8):
    print(' '.join(binary_key[i:i + 8]))

print("\nPermutasi PC-1 (Matriks 8x7):")
for i in range(0, 56, 7):
    print(' '.join(map(str, permuted_key[i:i + 7])))

print("\nC dan D values setelah left shift:")
for i in range(17):
    print(f"C{i}: {' '.join(map(str, C_values[i]))}")
    print(f"D{i}: {' '.join(map(str, D_values[i]))}")

print("\nNilai K setelah permutasi PC-2:")
for i, K in enumerate(K_values, start=1):
    print(f"K{i} = {' '.join(map(str, K))}")

# import numpy as np

# def text_to_binary_table(text):
#     binary_table = []
#     for char in text:
#         binary_code = format(ord(char), '08b')
#         binary_table.append((char.upper(), binary_code))
#     # Jika teks kurang dari 8 karakter, tambahkan "SPASI" dengan "00000000" untuk mencapai 64 bit
#     for _ in range(8 - len(text)):
#         binary_table.append(("SPASI", "00000000"))
#     return binary_table

# def generate_permuted_key(key_str, PC_1):
#     key_bits = [int(bit) for bit in key_str]
#     permuted_key = [key_bits[pc - 1] for pc in PC_1]
#     return permuted_key

# def left_shift(C0, D0, shifts):
#     C_values = [C0]
#     D_values = [D0]
#     for shift in shifts:
#         C_prev = C_values[-1]
#         D_prev = D_values[-1]
#         C_new = C_prev[shift:] + C_prev[:shift]
#         D_new = D_prev[shift:] + D_prev[:shift]
#         C_values.append(C_new)
#         D_values.append(D_new)
#     return C_values, D_values

# def generate_K(C_values, D_values, PC_2):
#     K_values = []
#     for i in range(16):
#         combined = np.concatenate((C_values[i + 1], D_values[i + 1]))
#         K = [combined[pos - 1] for pos in PC_2.flatten()]
#         K_values.append(K)
#     return K_values

# # Input kunci dari pengguna (teks, hingga 8 karakter)
# key_text = input("Masukkan kunci teks (hingga 8 karakter): ")
# binary_key = ''.join(format(ord(char), '08b') for char in key_text[:8])

# # Tambahkan 0 untuk mengisi jika kunci kurang dari 64 bit
# binary_key = binary_key.ljust(64, '0')

# # Input plainteks dari pengguna (teks, hingga 8 karakter)
# plaintext_text = input("Masukkan plainteks (hingga 8 karakter): ")
# binary_plaintext = ''.join(format(ord(char), '08b') for char in plaintext_text[:8])

# # Tambahkan 0 untuk mengisi jika plainteks kurang dari 64 bit
# binary_plaintext = binary_plaintext.ljust(64, '0')

# # Tampilkan tabel biner untuk kunci
# binary_table = text_to_binary_table(key_text)
# print("\nKunci (huruf kecil)\tBiner")
# for key, biner in binary_table:
#     print(f"{key}\t\t{biner}")

# # Tampilkan tabel biner untuk plainteks
# binary_table_plaintext = text_to_binary_table(plaintext_text)
# print("\nPlainteks (huruf kecil)\tBiner")
# for key, biner in binary_table_plaintext:
#     print(f"{key}\t\t{biner}")

# # Permutasi Pilihan 1 (PC-1)
# PC_1 = [
#     57, 49, 41, 33, 25, 17, 9, 
#     1, 58, 50, 42, 34, 26, 18, 
#     10, 2, 59, 51, 43, 35, 27, 
#     19, 11, 3, 60, 52, 44, 36, 
#     63, 55, 47, 39, 31, 23, 15, 
#     7, 62, 54, 46, 38, 30, 22, 
#     14, 6, 61, 53, 45, 37, 29, 
#     21, 13, 5, 28, 20, 12, 4 
# ]

# # Generate permutasi awal dengan PC-1 untuk kunci
# permuted_key = generate_permuted_key(binary_key, PC_1)
# C0 = permuted_key[:28]
# D0 = permuted_key[28:]

# # Tabel Shifts
# shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# # Generate C dan D values dengan left shift
# C_values, D_values = left_shift(C0, D0, shifts)

# # Permutasi Pilihan 2 (PC-2)
# PC_2 = np.array([
#     [14, 17, 11, 24, 1, 5],
#     [3, 28, 15, 6, 21, 10],
#     [23, 19, 12, 4, 26, 8],
#     [16, 7, 27, 20, 13, 2],
#     [41, 52, 31, 37, 47, 55],
#     [30, 40, 51, 45, 33, 48],
#     [44, 49, 39, 56, 34, 53],
#     [46, 42, 50, 36, 29, 32]
# ])

# # Generate nilai K
# K_values = generate_K(C_values, D_values, PC_2)

# # Tampilkan hasil
# print("\nKunci Awal (dalam biner, 64 bit):")
# for i in range(0, 64, 8):
#     print(' '.join(binary_key[i:i + 8]))

# print("\nPlainteks Awal (dalam biner, 64 bit):")
# for i in range(0, 64, 8):
#     print(' '.join(binary_plaintext[i:i + 8]))

# print("\nPermutasi PC-1 (Matriks 8x7):")
# for i in range(0, 56, 7):
#     print(' '.join(map(str, permuted_key[i:i + 7])))

# print("\nC dan D values setelah left shift:")
# for i in range(17):
#     print(f"C{i}: {' '.join(map(str, C_values[i]))}")
#     print(f"D{i}: {' '.join(map(str, D_values[i]))}")

# print("\nNilai K setelah permutasi PC-2:")
# for i, K in enumerate(K_values, start=1):
#     print(f"K{i} = {' '.join(map(str, K))}")
