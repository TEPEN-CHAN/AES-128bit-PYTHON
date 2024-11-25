import itertools

# Fungsi faktorial
def faktorial(x):
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

# Fungsi kombinasi
def kombinasi(n, r):
    if r > n:
        return 0
    faktorial_n = faktorial(n)
    faktorial_r = faktorial(r)
    faktorial_n_r = faktorial(n - r)
    return faktorial_n // (faktorial_r * faktorial_n_r)

# Program utama
n = int(input("Masukkan jumlah total objek (n): "))
r = int(input("Masukkan jumlah objek yang dipilih (r): "))

# Menghitung jumlah kombinasi
hasil = kombinasi(n, r)
print(f"Jumlah kombinasi C({n}, {r}) adalah: {hasil}")

# Mengambil huruf sesuai dengan jumlah objek n
huruf = [chr(i) for i in range(65, 65 + n)]  # Mengambil huruf 'A', 'B', 'C', dll.

# Menampilkan semua kombinasi huruf
kombinasi_huruf = itertools.combinations(huruf, r)
print(f"Kombinasi huruf yang dipilih dari {huruf} adalah:")
for comb in kombinasi_huruf:
    print("".join(comb))
