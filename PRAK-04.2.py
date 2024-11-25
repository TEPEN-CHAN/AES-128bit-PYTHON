# # Step 1: Substitution Cipher (Caesar Cipher with a shift of 3)
# def substitution_cipher(plaintext, shift=3):
#     ciphertext = ""
#     for char in plaintext:
#         if char.isalpha():  # Only shift letters
#             shift_base = 65 if char.isupper() else 97
#             ciphertext += chr((ord(char) - shift_base + shift) % 26 + shift_base)
#         else:
#             ciphertext += char  # Keep spaces and other characters unchanged
#     return ciphertext

# # Step 2: Transposition Cipher
# def transposition_cipher(plaintext):
#     part_length = len(plaintext) // 4
#     parts = [plaintext[i:i + part_length] for i in range(0, len(plaintext), part_length)]
    
#     ciphertext = ""
#     for col in range(4):
#         for part in parts:
#             if col < len(part):
#                 ciphertext += part[col]
#     return ciphertext

# # Step 3: Input Plaintext
# plaintext = "UNIKA SANTO THOMAS"

# # Step 4: Apply Substitution Cipher
# sub_ciphertext = substitution_cipher(plaintext)

# # Step 5: Apply Transposition Cipher
# final_ciphertext = transposition_cipher(sub_ciphertext)

# # Step 6: Output Results
# print("Input Plaintext:", plaintext)
# print("Substitution Ciphertext:", sub_ciphertext)
# print("Substitution + Transposition Ciphertext:", final_ciphertext)

# def transposisi_cipher(plaintext):
#     part_length = len(plaintext) // 4
#     parts = [plaintext[i:i + part_length] for i in range(0, len(plaintext), part_length)]
    
#     print("Bagian plaintext:")
#     for i, part in enumerate(parts):
#         print(f"Bagian {i + 1}: '{part}'")
    
#     ciphertext = ""  
    
#     for col in range(4):
#         for part in parts:
#             if col < len(part):
#                 ciphertext += part[col]
#                 print(f"Menambahkan '{part[col]}' dari Bagian {parts.index(part) + 1} ke ciphertext.")
    
#     return ciphertext

# plaintext = input("Masukkan plaintext: ")
# ciphertext = transposisi_cipher(plaintext)
# print(f"Ciphertext: '{ciphertext}'")

# Step 1: Substitution Cipher (Caesar Cipher with a shift of 3)
def substitution_cipher(plaintext, shift=3):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Only shift letters
            shift_base = 65 if char.isupper() else 97
            ciphertext += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            ciphertext += char  # Keep spaces and other characters unchanged
    return ciphertext

# Step 2: Transposition Cipher with Process Display
def transposition_cipher(plaintext):
    part_length = len(plaintext) // 4
    parts = [plaintext[i:i + part_length] for i in range(0, len(plaintext), part_length)]
    
    print("Bagian plaintext:")
    for i, part in enumerate(parts):
        print(f"Bagian {i + 1}: '{part}'")
    
    ciphertext = ""
    for col in range(4):
        for part in parts:
            if col < len(part):
                ciphertext += part[col]
                print(f"Menambahkan '{part[col]}' dari Bagian {parts.index(part) + 1} ke ciphertext.")
    return ciphertext

# Step 3: Input Plaintext
plaintext = input("Masukkan plaintext: ")

# Step 4: Apply Substitution Cipher
sub_ciphertext = substitution_cipher(plaintext)
print("\nSubstitution Ciphertext:", sub_ciphertext)

# Step 5: Apply Transposition Cipher
final_ciphertext = transposition_cipher(sub_ciphertext)

# Step 6: Output Final Ciphertext
print(f"\nSubstitution + Transposition Ciphertext: '{final_ciphertext}'")
