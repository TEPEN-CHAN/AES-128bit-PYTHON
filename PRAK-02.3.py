# Fungsi untuk kalkulator yang memproses input dalam bentuk string
def kalkulator_string(x_str, y_str, z_str, operator):
    x = float(x_str)
    y = float(y_str)
    z = float(z_str)
    
    # Operasi aritmatika berdasarkan operator
    if operator == '+':
        return f"Hasil {x} + {y} + {z} = {x + y + z}"
    elif operator == '-':
        return f"Hasil {x} - {y} - {z} = {x - y - z}"
    elif operator == '*':
        return f"Hasil {x} * {y} * {z} = {x * y * z}"
    elif operator == '/':
        if y == 0 or z == 0:
            return "Error! Pembagian dengan 0 tidak diperbolehkan."
        else:
            return f"Hasil {x} / {y} / {z} = {x / y / z}"
    elif operator == '%':
        if y == 0 or z == 0:
            return "Error! Modulus dengan 0 tidak diperbolehkan."
        else:
            return f"Hasil {x} % {y} % {z} = {x % y % z}"
    else:
        return "Operator tidak valid!"

# Main loop program
ulang = 'y'
while ulang.lower() == 'y':
    # Input nilai x, y, dan z dari pengguna dalam bentuk string
    x_str = input("Masukkan nilai x (dalam bentuk string): ")
    y_str = input("Masukkan nilai y (dalam bentuk string): ")
    z_str = input("Masukkan nilai z (dalam bentuk string): ")

    # Input operator dari pengguna dalam bentuk string
    operator = input("Masukkan operator (+, -, *, /, %): ")

    # Panggil fungsi kalkulator dengan input string
    hasil = kalkulator_string(x_str, y_str, z_str, operator)

    # Tampilkan hasil
    print(hasil)

    # Menanyakan apakah ingin mengulang program
    ulang = input("Apakah Anda ingin mengulang program? [y/t]: ")

print("Program selesai.")

