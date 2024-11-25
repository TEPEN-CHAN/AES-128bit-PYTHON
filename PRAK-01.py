#a= 1
#b= 2
#if b > a:
    #print ("b lebih besar dari a") 10% 30% 35% 25%, 80-100 (a) 70-79(b) 60-69(c) 50-59(d) 40-49(e)
    
#a= 1
#b= 2
#c= a+b
#print(a+b)
# kap = float(input("nilai sikap:"))
# uas = float(input("nilai uas:"))
# uts = float(input("nilai uts:"))
# tgs = float(input("nilai tugas:"))

# na = (10/100 * kap) + (30/100 * uas) + (35/100 * uts) + (25/100 * tgs)
# if na <= 100 and na >=80:
#     nf='A'
# elif na <=79 and na >=70:
#     nf='B'
# elif na <=69 and na >=60:
#     nf='C'
# elif na <=59 and na >=50:
#     nf='D'
# else:
#     nf='E'   
# print("Nilai Akir = %0.2f" % na)
# print("Nilai Huruf = %c" % nf)
# if nf <= 'C' and nf >='':
#     print("lulus")
# else:
#     print("tidak lulus")
    
# pil = float(print(input("apakah anda ingin melanjutkan program Y/T?: ")))
#   if pil == 'Y'

def hitung_nilai():
    kap = float(input("Nilai sikap: "))
    uas = float(input("Nilai UAS: "))
    uts = float(input("Nilai UTS: "))
    tgs = float(input("Nilai tugas: "))

    na = (10/100 * kap) + (30/100 * uas) + (35/100 * uts) + (25/100 * tgs)

    if na <= 100 and na >= 80:
        nf = 'A'
    elif na <= 79 and na >= 70:
        nf = 'B'
    elif na <= 69 and na >= 60:
        nf = 'C'
    elif na <= 59 and na >= 50:
        nf = 'D'
    else:
        nf = 'E'

    print("Nilai Akhir = %0.2f" % na)
    print("Nilai Huruf = %c" % nf)

    if nf <= 'C' and nf >= 'A':
        print("Lulus")
    else:
        print("Tidak lulus")

# Fungsi untuk menanyakan apakah ingin mengulang
def ulangi_program():
    while True:
        hitung_nilai()
        ulang = input("Apakah Anda ingin mengulang? (Y/T): ").strip().lower()
        if ulang == 't':
            print("Program berhenti.")
            break
        elif ulang != 'y':
            print("Input tidak valid. Silakan masukkan 'Y' untuk Ya atau 'T' untuk Tidak.")
            
# Memulai program
ulangi_program()
