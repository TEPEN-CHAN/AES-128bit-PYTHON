# #Konversi Bilangan Biner ke Desimal, Oktal, dan Heksadesimal
# def konversi_biner():
#     biner = input("Masukkan bilangan biner: ")
#     desimal = int(biner, 2)
#     oktal = oct(desimal)[2:]
#     heksadesimal = hex(desimal)[2:]
    
#     print(f"Biner: {biner}")
#     print(f"Desimal: {desimal}")
#     print(f"Oktal: {oktal}")
#     print(f"Heksadesimal: {heksadesimal}")

# konversi_biner()

# # Konversi Bilangan Oktal ke Desimal, Biner, dan Heksadesima

# def konversi_oktal():
#     oktal = input("Masukkan bilangan oktal: ")
#     desimal = int(oktal, 8)
#     biner = bin(desimal)[2:]
#     heksadesimal = hex(desimal)[2:]
    
#     print(f"Oktal: {oktal}")
#     print(f"Desimal: {desimal}")
#     print(f"Biner: {biner}")
#     print(f"Heksadesimal: {heksadesimal}")

# konversi_oktal()

# Konversi Bilangan Heksadesimal ke Desimal, Biner, dan Oktal
def konversi_heksadesimal():
    heksadesimal = input("Masukkan bilangan heksadesimal: ")
    desimal = int(heksadesimal, 16)
    biner = bin(desimal)[2:]
    oktal = oct(desimal)[2:]
    
    print(f"Heksadesimal: {heksadesimal}")
    print(f"Desimal: {desimal}")
    print(f"Biner: {biner}")
    print(f"Oktal: {oktal}")

konversi_heksadesimal()
