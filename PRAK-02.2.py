
def kalkulator_3_nilai(x, y, z, operator):

    if operator == '+':
        return x + y + z

    elif operator == '-':
        return x - y - z

    elif operator == '*':
        return x * y * z

    elif operator == '/':

        if y == 0 or z == 0:
            return "Error! Pembagian dengan 0 tidak diperbolehkan."
        else:
            return x / y / z
    elif operator == '%':
        if y == 0 or z == 0:
            return "Error! Modulus dengan 0 tidak diperbolehkan."
        else:
            return x % y % z
    else:
        return "Operator tidak valid!"
x = float(input("Masukkan nilai x: "))
y = float(input("Masukkan nilai y: "))
z = float(input("Masukkan nilai z: "))

operator = input("Masukkan operator (+, -, *, /, %): ")
hasil = kalkulator_3_nilai(x, y, z, operator)
print(f"Hasil: {hasil}")
