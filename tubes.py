# File : Tubes.py 
# Penulis : 2472010 2472012 2472005
# Tujuan Program :
#
# Kamus Data :

import csv


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

def lihatbuku():
    # Disini saya gunakan array dua dimensi atau matriks sebagai menyimpan semua data dari file CSV
    # dengan format setiap: [Kategori, Judul, Stok, Aisle]
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

def lihatbukus():
    # Disini saya gunakan array dua dimensi atau matriks sebagai menyimpan semua data dari file CSV
    # dengan format setiap: [Kategori, Judul, Stok, Aisle]
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

def daftar():
    print("NRP anda belum terdaftar!") 
    print("Apakah anda ingin daftar?")
    print("==============================")
    nama_peminjam = str(input("Username: "))
    nrp_peminjam = int(input("Nrp: "))
    with open('Data_peminjam.csv', mode='a', newline='')as f:
        writer = csv.writer(f)
        writer.writerow([nama_peminjam, nrp_peminjam])
    print("==============================")
    print("Nama dan NRP anda sudah terdaftar")
    print()
    login()

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
        df = pd.read_csv('Peminjaman.csv')
        print(df)
        return
    elif pilihan == '2':
        print("Data Akun Peminjam:")
        df = pd.read_csv('Data_peminjam.csv')
        print(df)
        return
    elif pilihan == '0':
        print("Kembali berhasil. ke menu Staff.")
        menus()
    else:
        print("Pilihan tidak valid.")
        return

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