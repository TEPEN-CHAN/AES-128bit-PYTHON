def kalkulator(a, b, operator):

    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:  
            return a / b
        else:
            return "Error!"
    elif operator == '%':
        if b != 0:  
            return a % b
        else:
            return "Error!"
    else:
        return "Operator tidak valid!"

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

operator = input("Masukkan operator (+, -, *, /, %): ")
hasil = kalkulator(a, b, operator)

print(f"Hasil: {hasil}")
