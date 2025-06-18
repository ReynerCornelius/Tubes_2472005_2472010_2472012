# File : Tubes.py 
# Penulis : 2472010 2472012 2472005
# Tujuan Program :
# Program ini adalah sistem perpustakaan sederhana yang memungkinkan peminjam untuk melihat buku, meminjam buku, dan staff untuk menambah buku serta melihat data peminjaman.
# Kamus Data :
# nama : str untuk nama peminjam atau staff
# nrp : str untuk NRP peminjam
# kode : str untuk kode staff
# pilihan : str untuk pilihan menu yang dipilih user
# kategori : str untuk kategori buku
# judul : str untuk judul buku
# stok : int untuk jumlah stok buku
# aisle : str untuk lokasi rak buku
# matriks_buku : list untuk list 2 dimensi berisi data buku [kategori, judul, stok, aisle]
# peminjam_terakhir : list untuk data peminjam terakhir yang login
# rows : list untuk menyimpan data buku sementara
# found : bool untuk penanda buku ditemukan/tidak
# df : pandas.DataFrame - dataFrame untuk menampilkan data csv
# reader : csv.reader untuk reader untuk membaca file csv
# writer : csv.writer untuk writer untuk menulis file csv
# f : file object untuk operasi file
# cek : str untuk pilihan menu utama
import csv # untuk operasi file CSV
# Modul ini digunakan untuk membaca dan menulis file CSV yang berisi data peminjam, staff, buku, dan peminjaman.
# csv ini juga digunakan untuk menyimpan data peminjam yang telah login ke file Login.csv.
# csv ini digunakan untuk menyimpan data buku yang telah ditambahkan ke file Buku.csv.
# csv ini juga digunakan untuk menyimpan data peminjaman yang telah dilakukan ke file Peminjaman.csv.
# csv ini digunakan untuk menyimpan data staff yang telah ditambahkan ke file Data_staff.csv.
# csv digunakan untuk menyimpan data peminjam yang telah didaftarkan ke file Data_peminjam.csv.

# ============================================================
# Kamus Data untuk fungsi login() UNTUK PEMINJAM:
# nama   : str - Nama peminjam yang dimasukkan oleh user
# nrp    : str - NRP peminjam yang dimasukkan oleh user
# f      : file object - File 'Data_peminjam.csv' yang dibuka untuk membaca data peminjam
# reader : csv.reader - Objek untuk membaca baris-baris pada file CSV
# row    : list - Baris data tunggal dari file CSV
# writer : csv.writer - Objek untuk menulis data ke file 'Login.csv'
# ============================================================
def login():
    print("Silahkan masukkan Nama dan NRP anda:")
    print("==============================")
    nama = input('Nama: ')
    nrp = input("Nrp : ")
    print("==============================")
    with open('Data_peminjam.csv', mode='r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if (row[0] == nama and row[1] == nrp):
                print('Selamat datang', nama, 'di perpustakaan Maranatha')
                with open('Login.csv', mode='a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([nama, nrp])
                menu()
                break
        else:
            print("Data tidak ditemukan.")
            daftar()
    
# ============================================================
# Kamus Data untuk fungsi logins() UNTUK STAFF:
# kode    : str - Kode staff yang dimasukkan oleh user
# f       : file object - File 'Data_staff.csv' yang dibuka untuk membaca data staff
# reader  : csv.reader - Objek untuk membaca baris-baris pada file CSV
# row     : list - Baris data tunggal dari file CSV
# ============================================================
def logins():
    print("Silahkan masukkan kode staff :")
    print("==============================")
    kode = input("Kode Staff :")
    print("==============================")
    with open('Data_staff.csv', mode='r', newline='')as f:
        reader = csv.reader(f)    
        for row in reader :
            if (row[1] == kode):
                print('Selamat datang',row[0],'(staff) di perpustakaan maranatha')
                menus()
                break
        else:
            print("Data tidak ditemukan.")
            daftars()

# ============================================================
# Kamus Data untuk fungsi menu() UNTUK PEMINJAM:
# pilihan : str - Pilihan menu yang dimasukkan oleh user ('1' untuk lihat buku, '2' untuk meminjam buku, '0' untuk logout)
# ============================================================
def menu():
    print("==============================")
    print("Selamat datang di Menu untuk Peminjam")
    print("1. Lihat Buku")
    print("2  Meminjam Buku")
    print("0. Logout")
    print("==============================")
    pilihan = input("Masukkan pilihan (1/2/0): ")
    if pilihan == '1':
        lihatbuku()
        print()
    elif pilihan == '2':
        pinjamBuku()
        print()
    elif pilihan == '0':
        print("Logout berhasil. Kembali ke menu utama.")
        main()
    else:
        print("Pilihan tidak valid.")

# ============================================================
# Kamus Data untuk fungsi menus() UNTUK STAFF:
# pilihan : str - Pilihan menu yang dimasukkan oleh user ('1' untuk lihat buku, '2' untuk tambah buku, '3' untuk lihat peminjaman, '0' untuk logout)
# ============================================================
def menus():
    print("==============================")
    print("Selamat datang di Menu untuk Staff")
    print("1. Lihat Buku")
    print("2. Tambah Buku")
    print("3. Lihat Peminjaman")
    print("0. Logout")
    print("==============================")
    pilihan = input("Masukkan pilihan (1/2/0): ")
    if pilihan == '1':
        lihatbukus()
        print()
    elif pilihan == '2':
        tambahBuku()
        print()
    elif pilihan == '3':
        Peminjaman()
        print()
    elif pilihan == '0':
        print("Logout berhasil. Kembali ke menu utama.")
        main()
    else:
        print("Pilihan tidak valid.")
# ============================================================
# Kamus Data untuk fungsi lihatbuku():
# matriks_buku   : list of list - Matriks berisi data buku, format: [kategori, judul, stok, aisle]
# reader         : csv.reader   - Objek pembaca file CSV
# row            : list         - Baris data dari file CSV, berisi [kategori, judul, stok, aisle]
# kategori       : str          - Nama kategori buku (misal: 'Science', 'Sejarah', 'Novel', 'Majalah')
# judul          : str          - Judul buku
# stok           : int          - Jumlah stok buku yang tersedia
# aisle          : str          - Lokasi rak/aisle buku
# kategori_list  : list of str  - Daftar kategori buku yang akan ditampilkan
# total_stok     : int          - Total stok buku untuk setiap kategori
# pilihan        : str          - Input dari pengguna untuk memilih aksi selanjutnya (meminjam buku atau kembali ke menu utama)
# ============================================================
# Disini saya gunakan array dua dimensi atau matriks sebagai menyimpan semua data dari file CSV
# dengan format setiap: [Kategori, Judul, Stok, Aisle]
def lihatbuku():
    
    matriks_buku = []
    with open('Buku.csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)  
        for row in reader:
            kategori = row[0]
            judul = row[1]
            stok = int(row[2]) 
            aisle = row[3]
            matriks_buku.append([kategori, judul, stok, aisle])
    kategori_list = ['Science', 'Sejarah', 'Novel', 'Majalah']
    print("\n===== DAFTAR BUKU PER KATEGORI (Matriks) =====")
    for kategori in kategori_list:
        print()
        print(f"KATEGORI: {kategori}")
        print("====================================")
        print("Judul Buku - Stok - Aisle")
        print("------------------------------------")
        total_stok = 0 
        for row in matriks_buku:
            kategori_buku = row[0]
            judul = row[1]
            stok = row[2]
            aisle = row[3]
            if kategori_buku == kategori:
                print(f"{judul} - {stok} - {aisle}")
                total_stok += stok
        print("------------------------------------")
        print(f"Total Stok buku yang ada di Kategori {kategori}: {total_stok}")
    print("=========================================")
    print("Berikut adalah daftar buku yang tersedia:")
    print("Apakah anda ingin meminjam buku? Atau ingin kembali ke menu utama?")
    print("1. Pinjam Buku")
    print("0. Kembali")
    print("==============================")
    pilihan = input("Masukkan pilihan (0/1): ")
    if pilihan == '1':
        pinjamBuku()
        print()
    elif pilihan == '0':
        print("Kembali berhasil. ke menu peminjam.")
        menu()
    else:
        print("Pilihan tidak valid.")

# ============================================================
# Kamus Data untuk fungsi lihatbukus() UNTUK STAFF:
# matriks_buku   : list of list - Matriks berisi data buku, format: [kategori, judul, stok, aisle]
# kategori_list  : list of str  - Daftar kategori buku yang tersedia, misal: ['Science', 'Sejarah', 'Novel', 'Majalah']
# kategori       : str          - Nama kategori buku yang sedang diproses pada iterasi
# row            : list         - Baris data buku dari file CSV, berisi [kategori, judul, stok, aisle]
# kategori_buku  : str          - Kategori dari buku pada baris tertentu
# judul          : str          - Judul buku pada baris tertentu
# stok           : int          - Jumlah stok buku pada baris tertentu
# aisle          : str          - Letak rak buku pada baris tertentu
# total_stok     : int          - Total stok buku dalam satu kategori
# pilihan        : str          - Input dari pengguna untuk memilih aksi selanjutnya (tambah buku atau kembali ke menu)
# ============================================================
# Disini saya gunakan array dua dimensi atau matriks sebagai menyimpan semua data dari file CSV
# dengan format setiap: [Kategori, Judul, Stok, Aisle]
def lihatbukus():
    matriks_buku = []
    with open('Buku.csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)  
        for row in reader:
            kategori = row[0]
            judul = row[1]
            stok = int(row[2]) 
            aisle = row[3]
            matriks_buku.append([kategori, judul, stok, aisle])
    kategori_list = ['Science', 'Sejarah', 'Novel', 'Majalah']
    print("===== DAFTAR BUKU PER KATEGORI (Matriks) =====")
    for kategori in kategori_list:
        print()
        print(f"KATEGORI: {kategori}")
        print("====================================")
        print("Judul Buku - Stok - Aisle")
        print("------------------------------------")
        total_stok = 0 
        for row in matriks_buku:
            kategori_buku = row[0]
            judul = row[1]
            stok = row[2]
            aisle = row[3]
            if kategori_buku == kategori:
                if int(stok) == 0:
                    print(f"{judul} - {stok} - {aisle} (Stok Habis)")
                else:
                    print(f"{judul} - {stok} - {aisle}")
                total_stok += int(stok)
        print("------------------------------------")
        print(f"Total Stok buku yang ada di Kategori {kategori}: {total_stok}")
    print("=========================================")
    print("Berikut adalah daftar buku yang tersedia:")
    print("Apakah anda ingin menambahkan buku? Atau ingin kembali ke menu utama?")
    print("0. Kembali")
    print("1. Tambah Buku")
    print("==============================")
    pilihan = input("Masukkan pilihan (0/1): ")
    if pilihan == '1':
        tambahBuku()
        print()
    elif pilihan == '0':
        print("Kembali berhasil. ke menu Staff.")
        menus()
    else:
        print("Pilihan tidak valid.")

# ============================================================
# Kamus Data untuk fungsi daftar():
# nama_peminjam : str - Username yang dimasukkan oleh pengguna
# nrp_peminjam  : int - NRP yang dimasukkan oleh pengguna
# pilihan       : str - Pilihan menu yang dimasukkan oleh pengguna ('0' untuk logout, '1' untuk daftar)
# ============================================================
def daftar():
    print("NRP anda belum terdaftar!") 
    print("Apakah anda ingin daftar?")
    print("0. Log Out")
    print("1. Daftar Akun Peminjam")
    pilihan = input("Masukkan pilihan (0/1):")
    print("==============================")
    if pilihan =='1':
        nama_peminjam = str(input("Username: "))
        nrp_peminjam = int(input("Nrp: "))
        with open('Data_peminjam.csv', mode='a', newline='')as f:
            writer = csv.writer(f)
            writer.writerow([nama_peminjam, nrp_peminjam])
    elif pilihan == '0':
        print("Terima kasih telah menggunakan layanan kami.")
    else:
        print("Pilihan tidak valid.")

    print("==============================")
    print("Nama dan NRP anda sudah terdaftar")
    print()
    login()

# ============================================================
# Kamus Data untuk fungsi daftars():
# nama_staff  : str - Nama staff yang akan didaftarkan
# kode_staff  : int - Kode unik staff
# f           : file object - File 'Data_staff.csv' yang dibuka untuk menambah data
# writer      : csv.writer - Objek untuk menulis data ke file CSV
# ============================================================
def daftars():
    print("Kode staff anda belum terdaftar!") 
    print("Apakah anda ingin daftar?")
    print("==============================")
    nama_staff= str(input("Nama :"))
    kode_staff = int(input("Kode Staff :"))
    with open('Data_staff.csv', mode='a', newline='')as f:
        writer = csv.writer(f)
        writer.writerow([nama_staff, kode_staff])
    print("==============================")
    print("Nama dan Kode Staff anda sudah terdaftar")
    print()
    logins()
    
# ============================================================
# Kamus Data untuk fungsi pinjamBuku():
# judul   : str - judul buku yang ingin dipinjam
# stok    : int - jumlah buku yang ingin dipinjam
# rows    : list - daftar seluruh baris data buku dari 'Buku.csv' (stok diperbarui jika peminjaman berhasil)
# found   : bool - penanda apakah buku ditemukan dan stok mencukupi
# reader  : csv.reader - pembaca file CSV
# row     : list - baris data tunggal dari file CSV
# new_stok: int - sisa stok buku setelah dipinjam
# peminjam_terakhir : list - data pengguna terakhir yang login (baris terakhir 'Login.csv')
# nama    : str - nama peminjam (dari 'Login.csv')
# nrp     : str - NRP peminjam (dari 'Login.csv')
# pilihan : str - input pilihan dari pengguna untuk melanjutkan peminjaman atau kembali ke menu utama
# ============================================================
def pinjamBuku():
    print("Silahkan masukkan data buku yang ingin dipinjam:")
    print("==============================")
    judul = input("Judul: ")
    stok = int(input("Jumlah: "))
    rows = []
    found = False
    with open('Buku.csv', mode='r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == judul and int(row[2]) >= stok:
                new_stok = int(row[2]) - stok
                row[2] = str(new_stok)
                print(f"Buku {judul} berhasil dipinjam. Stok tersisa: {new_stok}")
                found = True
            rows.append(row)
    if (found != True):
        print("Buku tidak ditemukan atau stok tidak mencukupi.")

    with open('Buku.csv', mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    
    with open('Login.csv', mode='r', newline='') as f:
        reader = csv.reader(f)
        peminjam_terakhir = None
        for row in reader:
            peminjam_terakhir = row
        if peminjam_terakhir:
            nama = peminjam_terakhir[0]
            nrp = peminjam_terakhir[1]
            with open('Peminjaman.csv', mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([nama, nrp, judul, stok])
    print("=========================================")
    print("Apakah anda ingin meminjam buku lain? Atau ingin kembali ke menu utama?")
    print("1. Pinjam Buku")
    print("0. Kembali")
    print("==============================")
    pilihan = input("Masukkan pilihan (1/0): ")
    if pilihan == '1':
        pinjamBuku()
        print()
    elif pilihan == '0':
        print("Kembali berhasil. ke menu peminjam.")
        menu()
    else:
        print("Pilihan tidak valid.")

# ============================================================
# Kamus Data untuk fungsi tambahBuku():
# kategori : str - Kategori buku yang akan ditambahkan
# judul    : str - Judul buku yang akan ditambahkan
# stok     : int - Jumlah stok buku yang akan ditambahkan
# aisle    : str - Lokasi rak/aisle buku di perpustakaan
# pilihan  : str - Pilihan menu lanjutan setelah menambah buku
# ============================================================
def tambahBuku():
    print("Silahkan masukkan data buku yang ingin ditambahkan:")
    print("==============================")
    kategori = input("Kategori: ")
    judul = input("Judul: ")
    stok = int(input("Stok: "))
    aisle = input("Aisle: ")
    with open('Buku.csv', mode='a', newline='')as f:
        writer = csv.writer(f)
        writer.writerow([kategori, judul, stok, aisle])
    print("=========================================")
    print("Buku telah berhasil ditambahkan.")
    print("=========================================")
    print("Apakah anda ingin menambahkan buku baru? Atau ingin kembali ke menu utama?")
    print("1. Tambah Buku")
    print("0. Kembali")
    print("==============================")
    pilihan = input("Masukkan pilihan (1/2/0): ")
    if pilihan == '1':
        tambahBuku()
        print()
    elif pilihan == '0':
        print("Kembali berhasil. ke menu Staff.")
        menus()
    elif pilihan == '2':
        lihatbukus()
    else:
        print("Pilihan tidak valid.")

# ============================================================
# Kamus Data dari fungsi Peminjaman():
# pd: modul pandas untuk membaca file csv
# pilihan: str - Pilihan menu yang dimasukkan user
# df: pandas.DataFrame - DataFrame untuk menampilkan data csv
# ============================================================
def Peminjaman():
    import pandas as pd
    print("Silahkan input data yang ingin ditampilkan:")
    print("1. Data Peminjaman")
    print("2. Data Akun Peminjam")
    print("0. Kembali ke menu Staff")
    print("==============================")
    pilihan = input("Masukkan pilihan 1/2/0: ")
    if pilihan == '1':
        print("Data Peminjaman:")
        # Menggunakan pandas untuk membaca file csv dan menampilkannya dalam bentuk tabel
        df = pd.read_csv('Peminjaman.csv')
        print(df)
        print("==============================")
        Peminjaman()
        return
    elif pilihan == '2':
        print("Data Akun Peminjam:")
        # Menggunakan pandas untuk membaca file csv dan menampilkannya dalam bentuk tabel
        df = pd.read_csv('Data_peminjam.csv')
        print(df)
        print("==============================")
        Peminjaman()
        return
    elif pilihan == '0':
        print("Kembali berhasil. ke menu Staff.")
        menus()
    else:
        print("Pilihan tidak valid.")
        return
    
# ============================================================
# Nama File: Tubes.py
# Deskripsi: Program ini adalah sistem perpustakaan sederhana yang memungkinkan peminjam untuk melihat buku, meminjam buku, dan staff untuk menambah buku serta melihat data peminjaman.
# Penulis: 2472010, 2472012, 2472005
# Tanggal Pembuatan: 2025-05-26
# Versi: 1.0    
# Kamus Data:
# nama: str - Nama peminjam atau staff
# nrp: str - NRP peminjam
# kode: str - Kode staff
# pilihan: str - Pilihan menu yang dipilih user
# kategori: str - Kategori buku
# judul: str - Judul buku
# stok: int - Jumlah stok buku
# aisle: str - Lokasi rak buku
# matriks_buku: list - List 2 dimensi berisi data buku [kategori, judul, stok, aisle]
# peminjam_terakhir: list - Data peminjam terakhir yang login
# rows: list - Menyimpan data buku sementara
# found: bool - Penanda buku ditemukan/tidak
# df: pandas.DataFrame - DataFrame untuk menampilkan data csv
# reader: csv.reader - Reader untuk membaca file csv
# writer: csv.writer - Writer untuk menulis file csv
# f: file object - Untuk operasi file
# cek: str - Pilihan menu utama
# ============================================================
# Fungsi main() berikut merupakan kode pembuka untuk login.
# Pengguna akan disambut dan diminta memilih login sebagai
# peminjam, staff, atau keluar dari aplikasi perpustakaan.
# ============================================================
def main():
    # Perintah Input
    print("Selamat Datang di Perpustakaan Maranatha!!")
    print("Apakah anda ingin login?")
    print("==============================")
    print("1. Login sebagai Peminjam")
    print("2. Login sebagai Staff")
    print("0. Keluar")
    print("==============================")
    cek = input("Masukkan pilihan anda (1/2/0): ")
    print("==============================")
    if cek == '1':
        login()
    elif cek == '2':
        logins()
    elif cek == '0':
        print("Terima kasih telah menggunakan layanan kami.")
    else:
        print("Pilihan tidak valid.")
    # Perintah Proses

    # Perintah Output
    return 0
if __name__ == '__main__':    
    main()   