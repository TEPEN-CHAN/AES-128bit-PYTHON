import itertools

# Fungsi untuk menginput data dari keyboard (baik angka atau huruf)
def input_data():
    data = input("Masukkan elemen-elemen (pisahkan dengan spasi): ").split()
    return data  # Tidak mengubah ke integer agar bisa memasukkan huruf

# Permutasi menyeluruh
def permutasi_menyeluruh(arr):
    return list(itertools.permutations(arr))

# Permutasi sebagian
def permutasi_sebagian(arr, k):
    return list(itertools.permutations(arr, k))

# Permutasi keliling
def permutasi_keliling(arr):
    if len(arr) == 1:
        return [arr]
    pertama = arr[0]
    permutasi_penuh = list(itertools.permutations(arr[1:]))
    return [[pertama] + list(perm) for perm in permutasi_penuh]

# Permutasi berkelompok
def permutasi_berkelompok(grup):
    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for hsl in hasil:
            for perm in itertools.permutations(kelompok):
                hasil_baru.append(hsl + list(perm))
        hasil = hasil_baru
    return hasil

# Program utama
while True:
    print("\nPilih jenis permutasi:")
    print("1. Permutasi menyeluruh")
    print("2. Permutasi sebagian")
    print("3. Permutasi keliling")
    print("4. Permutasi berkelompok")
    print("5. Keluar")
    
    pilihan = input("Masukkan pilihan (1-5): ")

    if pilihan == '1':
        data = input_data()
        print("Permutasi menyeluruh:", permutasi_menyeluruh(data))
    
    elif pilihan == '2':
        data = input_data()
        k = int(input("Masukkan nilai k (panjang permutasi): "))
        print("Permutasi sebagian:", permutasi_sebagian(data, k))
    
    elif pilihan == '3':
        data = input_data()
        print("Permutasi keliling:", permutasi_keliling(data))
    
    elif pilihan == '4':
        grup = []
        banyak_grup = int(input("Masukkan jumlah grup: "))
        for i in range(banyak_grup):
            kelompok = input(f"Masukkan elemen-elemen grup {i+1} (pisahkan dengan spasi): ").split()
            grup.append(kelompok)  # Tidak diubah ke integer agar bisa memasukkan huruf
        print("Permutasi berkelompok:", permutasi_berkelompok(grup))

    elif pilihan == '5':
        print("Keluar dari program.")
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

        
#Program Python untuk Menghitung dan Mencetak Semua Cara Mengatur Buku
import itertools

def generate_arrangements(n, r):
    """
    Menghasilkan semua cara mengatur n buku ke dalam r bagian rak.
    
    Args:
        n (int): Jumlah buku.
        r (int): Jumlah bagian rak.
    
    Returns:
        List[List[List[str]]]: List dari semua pengaturan, 
                               di mana setiap pengaturan adalah list 
                               yang berisi r sublist buku.
    """
    # Membuat daftar buku
    books = [f"Book{i+1}" for i in range(n)]
    
    # Membuat daftar bagian rak
    sections = [f"Section{j+1}" for j in range(r)]
    
    # Menghasilkan semua kombinasi penempatan buku ke bagian rak
    # itertools.product menghasilkan Cartesian product dari r pilihan untuk setiap buku
    all_combinations = itertools.product(range(r), repeat=n)
    
    arrangements = []
    
    for combination in all_combinations:
        # Inisialisasi list untuk setiap bagian rak
        current_arrangement = [[] for _ in range(r)]
        
        # Menempatkan setiap buku ke bagian rak yang ditentukan oleh kombinasi
        for book, section_index in zip(books, combination):
            current_arrangement[section_index].append(book)
        
        arrangements.append(current_arrangement)
    
    return arrangements

def display_arrangements(arrangements, sections):
    """
    Mencetak semua pengaturan buku ke dalam bagian rak.
    
    Args:
        arrangements (List[List[List[str]]]): Semua pengaturan yang dihasilkan.
        sections (List[str]): Nama-nama bagian rak.
    """
    for idx, arrangement in enumerate(arrangements, 1):
        print(f"Cara {idx}:")
        for section, books in zip(sections, arrangement):
            print(f"  {section}: {books}")
        print()

def main():
    print("=== Program Pengaturan Buku di Rak ===")
    
    while True:
        try:
            # Memasukkan jumlah buku
            n = int(input("Masukkan jumlah buku (n): "))
            if n <= 0:
                print("Jumlah buku harus positif. Silakan coba lagi.")
                continue
        except ValueError:
            print("Input tidak valid. Masukkan angka positif untuk jumlah buku.")
            continue
        
        try:
            # Memasukkan jumlah bagian rak
            r = int(input("Masukkan jumlah bagian rak (r): "))
            if r <= 0:
                print("Jumlah bagian rak harus positif. Silakan coba lagi.")
                continue
        except ValueError:
            print("Input tidak valid. Masukkan angka positif untuk jumlah bagian rak.")
            continue
        
        # Menghasilkan semua pengaturan
        arrangements = generate_arrangements(n, r)
        total = len(arrangements)
        
        print(f"\nTotal cara mengatur {n} buku ke dalam {r} bagian rak: {total}\n")
        
        # Membuat daftar nama bagian rak
        sections = [f"Section{j+1}" for j in range(r)]
        
        # Menampilkan pengaturan
        # Untuk nilai n dan r yang besar, mencetak semua pengaturan mungkin tidak praktis
        # Oleh karena itu, batasi jumlah pengaturan yang ditampilkan jika n * r > 20
        if total > 20:
            print("Jumlah pengaturan sangat besar. Menampilkan 20 pengaturan pertama:\n")
            display_arrangements(arrangements[:20], sections)
            print(f"... dan {total - 20} pengaturan lainnya tidak ditampilkan.")
        else:
            display_arrangements(arrangements, sections)
        
        # Menanyakan apakah pengguna ingin melakukan operasi lagi
        lanjut = input("Apakah Anda ingin mengatur buku lagi? (y/n): ").strip().lower()
        if lanjut != 'y':
            print("Terima kasih! Program selesai.")
            break

if __name__ == "__main__":
    main()

