# # Program Kalkulator Sederhana

# # Input nilai a dan b dari user
# a = float(input("Masukkan nilai a: "))
# b = float(input("Masukkan nilai b: "))

# # Input operator dari user
# operator = input("Masukkan operator (+, -, *, /, %): ")

# # Proses perhitungan berdasarkan operator
# if operator == '+':
#     hasil = a + b
#     print(f"Hasil {a} + {b} = {hasil}")
# elif operator == '-':
#     hasil = a - b
#     print(f"Hasil {a} - {b} = {hasil}")
# elif operator == '*':
#     hasil = a * b
#     print(f"Hasil {a} * {b} = {hasil}")
# elif operator == '/':
#     if b != 0:  # Menghindari pembagian dengan 0
#         hasil = a / b
#         print(f"Hasil {a} / {b} = {hasil}")
#     else:
#         print("Error! Pembagian dengan 0 tidak diperbolehkan.")
# elif operator == '%':
#     if b != 0:  # Menghindari pembagian dengan 0
#         hasil = a % b
#         print(f"Hasil {a} % {b} = {hasil}")
#     else:
#         print("Error! Modulus dengan 0 tidak diperbolehkan.")
# else:
#     print("Operator tidak valid!")

# Program Kalkulator Sederhana Tanpa If

# Program Kalkulator Sederhana dengan Operasi Aritmatika

operasi_aritmatika = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
}

x = float(input("Masukkan angka pertama: "))
y = float(input("Masukkan angka kedua: "))
operasi_dipilih = input("Pilih operator aritmatika (+, -, *, /, %): ")
hasil = operasi_aritmatika.get(operasi_dipilih, lambda x, y: "Operator tidak dikenali")(x, y)

print(f"Hasil perhitungan: {hasil}")

