# Fungsi untuk kalkulator dan operasi perbandingan yang memproses input dalam bentuk string
def kalkulator_dan_perbandingan(x_str, y_str, z_str, operator):
    # Ubah string input ke tipe float
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

    # Operasi perbandingan
    elif operator == '>':
        return f"{x} > {y} dan {x} > {z} = {x > y and x > z}"
    elif operator == '<':
        return f"{x} < {y} dan {x} < {z} = {x < y and x < z}"
    elif operator == '==':
        return f"{x} == {y} == {z} = {x == y == z}"
    elif operator == '!=':
        return f"{x} != {y} dan {x} != {z} = {x != y and x != z}"
    elif operator == '>=':
        return f"{x} >= {y} dan {x} >= {z} = {x >= y and x >= z}"
    elif operator == '<=':
        return f"{x} <= {y} dan {x} <= {z} = {x <= y and x <= z}"
    
    # Jika operator tidak valid
    else:
        return "Operator tidak valid!"

# Input nilai x, y, dan z dari pengguna dalam bentuk string
x_str = input("Masukkan nilai x (dalam bentuk string): ")
y_str = input("Masukkan nilai y (dalam bentuk string): ")
z_str = input("Masukkan nilai z (dalam bentuk string): ")

# Input operator dari pengguna dalam bentuk string
operator = input("Masukkan operator (+, -, *, /, %, >, <, ==, !=, >=, <=): ")

# Panggil fungsi kalkulator dan perbandingan dengan input string
hasil = kalkulator_dan_perbandingan(x_str, y_str, z_str, operator)

# Tampilkan hasil
print(hasil)