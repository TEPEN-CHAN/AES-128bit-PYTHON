def s_box(input_bytes):
    """Fungsi Substitusi S-Box"""
    sbox = [
        0x6, 0x4, 0xC, 0x5, 0x0, 0x7, 0x2, 0xE,
        0xF, 0x1, 0xA, 0x9, 0xB, 0x3, 0x8, 0xD
    ]
    substituted = []
    for byte in input_bytes:
        high = (byte >> 4) & 0xF  # 4-bit tinggi
        low = byte & 0xF          # 4-bit rendah
        # Substitusi menggunakan S-Box
        new_byte = (sbox[high] << 4) | sbox[low]
        substituted.append(new_byte)
    return substituted

def p_box(input_bytes):
    """Fungsi Permutasi P-Box"""
    permutation = [7, 6, 5, 4, 3, 2, 1, 0]  # Permutasi bit (posisi sederhana)
    permuted = []
    for byte in input_bytes:
        permuted_byte = 0
        for i, bit_pos in enumerate(permutation):
            bit = (byte >> bit_pos) & 0x1
            permuted_byte |= (bit << (7 - i))
        permuted.append(permuted_byte)
    return permuted

def round_processing(input_bytes, rounds):
    """Proses S-Box dan P-Box untuk beberapa ronde"""
    result = input_bytes
    for rnd in range(1, rounds + 1):
        print(f"\n--- Round {rnd} ---")
        # S-Box
        result = s_box(result)
        print(f"After S-Box: {[hex(b) for b in result]}")
        # P-Box
        result = p_box(result)
        print(f"After P-Box: {[hex(b) for b in result]}")
    return result

# Input plainteks
plainteks = "UNIKA   "
print("Plainteks:", plainteks)

# Konversi plainteks ke nilai ASCII
ascii_values = [ord(c) for c in plainteks]
print("\nNilai ASCII awal:", ascii_values)

# Jumlah ronde
num_rounds = 16

# Proses ronde
final_result = round_processing(ascii_values, num_rounds)

# Hasil akhir
print("\n--- Hasil Akhir Setelah 16 Ronde ---")
print("Nilai Akhir (Decimal):", final_result)
print("Nilai Akhir (Hex):", [hex(b) for b in final_result])