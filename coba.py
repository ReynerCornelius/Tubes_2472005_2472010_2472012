    # Program Manajemen Perpustakaan Sederhana untuk Pemula
# Fitur:
# - Login Peminjam dan Staff
# - Melihat daftar buku
# - Peminjam bisa pinjam buku dan pinjam ruangan
# - Staff bisa tambah buku dan lihat data peminjam

import datetime

# Data buku awal (kumpulan buku)
books = {
    "Science": [
        {"judul": "Fisika Dasar", "stok": 5, "aisle": "A1", "nomor_seri": "S001"},
        {"judul": "Kimia Organik", "stok": 3, "aisle": "A2", "nomor_seri": "S002"},
    ],
    "Sejarah": [
        {"judul": "Sejarah Indonesia", "stok": 4, "aisle": "B1", "nomor_seri": "H001"},
        {"judul": "Perang Dunia II", "stok": 2, "aisle": "B2", "nomor_seri": "H002"},
    ],
    "Novel": [
        {"judul": "Laskar Pelangi", "stok": 6, "aisle": "C1", "nomor_seri": "N001"},
        {"judul": "Bumi Manusia", "stok": 1, "aisle": "C2", "nomor_seri": "N002"},
    ],
    "Majalah": [
        {"judul": "Tempo", "stok": 10, "aisle": "D1", "nomor_seri": "M001"},
        {"judul": "Globe Asia", "stok": 7, "aisle": "D2", "nomor_seri": "M002"},
    ],
}

# Data ruangan
rooms = [
    {"nama": "Ruang A", "tersedia": True},
    {"nama": "Ruang B", "tersedia": True},
    {"nama": "Ruang C", "tersedia": False},
]

# Data peminjam awal
borrowers = [
    {"nrp": "2472005", "nama": "Reyner", "pinjam": []},
    {"nrp": "2472012", "nama": "Jason", "pinjam": []},
]

# Kode khusus staff
staff_code = "123456"

def clear_screen():
    print("\n" * 5)

def menampilkan_buku():
    print("\nDaftar Buku Per Kategori:")
    for kategori, buku_list in books.items():
        print(f"\nKategori: {kategori}")
        print(f"{'Judul':30} {'Stok':5} {'Aisle':5} {'Nomor Seri'}")
        for b in buku_list:
            print(f"{b['judul'][:30]:30} {b['stok']:5} {b['aisle']:5} {b['nomor_seri']}")

def cari_buku_dengan_nomor_seri(nomor_seri):
    for kategori, buku_list in books.items():
        for b in buku_list:
            if b["nomor_seri"].lower() == nomor_seri.lower():
                return b
    return None

def cari_peminjam_dengan_nrp(nrp):
    for b in borrowers:
        if b["nrp"] == nrp:
            return b
    return None

def pinjam_ruangan():
    print("\nDaftar Ruangan:")
    for i, r in enumerate(rooms, start=1):
        status = "Tersedia" if r["tersedia"] else "Tidak Tersedia"
        print(f"{i}. {r['nama']} - {status}")
    try:
        pilihan = int(input("Pilih nomor ruangan yang ingin dipinjam (0 untuk batal): "))
        if pilihan == 0:
            return
        if 1 <= pilihan <= len(rooms):
            if rooms[pilihan-1]["tersedia"]:
                rooms[pilihan-1]["tersedia"] = False
                print(f"Ruangan {rooms[pilihan-1]['nama']} berhasil dipinjam!")
            else:
                print("Ruangan tidak tersedia!")
        else:
            print("Pilihan tidak valid!")
    except:
        print("Input tidak valid!")

def pinjam_buku(peminjam):
    menampilkan_buku()
    nomor_seri = input("\nMasukkan nomor seri buku yang ingin dipinjam: ")
    buku = cari_buku_dengan_nomor_seri(nomor_seri)
    if buku is None:
        print("Buku tidak ditemukan.")
        return
    if buku["stok"] <= 0:
        print("Stok buku habis.")
        return
    tanggal = input("Masukkan tanggal peminjaman (YYYY-MM-DD): ")
    # Cek format tanggal sederhana
    try:
        datetime.datetime.strptime(tanggal, "%Y-%m-%d")
    except:
        print("Format tanggal salah!")
        return
    buku["stok"] -= 1
    peminjam["pinjam"].append({"nomor_seri": buku["nomor_seri"], "tanggal": tanggal})
    print("\nBerhasil meminjam buku!")
    print(f"Judul : {buku['judul']}")
    print(f"Nomor Seri : {buku['nomor_seri']}")
    print(f"Tanggal : {tanggal}")

def menu_peminjam(peminjam):
    while True:
        print(f"\nMenu Peminjam - {peminjam['nama']} (NRP: {peminjam['nrp']})")
        print("1. Tampilkan buku dan stok per kategori")
        print("2. Peminjaman ruangan diskusi")
        print("3. Pinjam buku")
        print("0. Logout")
        pilihan = input("Pilihan: ")
        if pilihan == "1":
            menampilkan_buku()
        elif pilihan == "2":
            pinjam_ruangan()
        elif pilihan == "3":
            pinjam_buku(peminjam)
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")
        input("Tekan Enter untuk melanjutkan...")

def tambah_buku_baru():
    print("\nTambah Buku Baru")
    print("Kategori tersedia:")
    kategori_list = list(books.keys())
    for i, k in enumerate(kategori_list, start=1):
        print(f"{i}. {k}")
    try:
        kat_pilih = int(input("Pilih nomor kategori: "))
        if 1 <= kat_pilih <= len(kategori_list):
            kategori = kategori_list[kat_pilih-1]
        else:
            print("Kategori tidak valid!")
            return
    except:
        print("Input tidak valid!")
        return
    judul = input("Masukkan judul buku: ")
    nomor_seri = input("Masukkan nomor seri: ")
    # Cek apakah nomor seri sudah ada
    if cari_buku_dengan_nomor_seri(nomor_seri):
        print("Nomor seri sudah ada di database!")
        return
    # Tambah stok awal 1 dan aisle "-"
    books[kategori].append({
        "judul": judul,
        "stok": 1,
        "aisle": "-",
        "nomor_seri": nomor_seri,
    })
    print("Buku berhasil ditambahkan!")

def tampilkan_data_peminjam():
    inp = input("\nMasukkan NRP peminjam (00 untuk semua): ")
    if inp == "00":
        for p in borrowers:
            print(f"\nNRP: {p['nrp']}, Nama: {p['nama']}")
            if p["pinjam"]:
                print("Buku yang dipinjam:")
                for pb in p["pinjam"]:
                    buku = cari_buku_dengan_nomor_seri(pb["nomor_seri"])
                    judul = buku["judul"] if buku else "Buku tidak ditemukan"
                    print(f" - {judul} (No Seri: {pb['nomor_seri']}) tgl: {pb['tanggal']}")
            else:
                print("Belum meminjam buku.")
    else:
        p = cari_peminjam_dengan_nrp(inp)
        if p is None:
            print("Peminjam tidak ditemukan.")
            return
        print(f"\nNRP: {p['nrp']}, Nama: {p['nama']}")
        if p["pinjam"]:
            print("Buku yang dipinjam:")
            for pb in p["pinjam"]:
                buku = cari_buku_dengan_nomor_seri(pb["nomor_seri"])
                judul = buku["judul"] if buku else "Buku tidak ditemukan"
                print(f" - {judul} (No Seri: {pb['nomor_seri']}) tgl: {pb['tanggal']}")
        else:
            print("Belum meminjam buku.")
        
def menu_staff():
    while True:
        print("\nMenu Staff")
        print("1. Tampilkan buku dan stok per kategori")
        print("2. Tambah buku baru")
        print("3. Tampilkan data peminjam")
        print("0. Logout")
        pilihan = input("Pilihan: ")
        if pilihan == "1":
            menampilkan_buku()
        elif pilihan == "2":
            tambah_buku_baru()
        elif pilihan == "3":
            tampilkan_data_peminjam()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")
        input("Tekan Enter untuk melanjutkan...")

def login_peminjam():
    nrp = input("Masukkan NRP Anda: ")
    nama = input("Masukkan nama Anda: ")
    peminjam = cari_peminjam_dengan_nrp(nrp)
    if peminjam and peminjam["nama"].lower() == nama.lower():
        print(f"Selamat datang, {peminjam['nama']}!")
        menu_peminjam(peminjam)
    else:
        print("NRP atau nama tidak cocok.")

def login_staff():
    kode = input("Masukkan kode khusus staff: ")
    if kode == staff_code:
        print("Login Staff berhasil!")
        menu_staff()
    else:
        print("Kode salah!")

def menu_utama():
    while True:
        clear_screen()
        print("=== Manajemen Perpustakaan ===")
        print("1. Login Peminjam")
        print("2. Login Staff")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            login_peminjam()
        elif pilihan == "2":
            login_staff()
        elif pilihan == "0":
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid!")
        input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    menu_utama()