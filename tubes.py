# File : Tubes.py 
# Penulis : 2472010 2472012 2472005
# Tujuan Program :
#
# Kamus Data :
import csv
# import pandas as pd
# df = pd.read_csv('Buku.csv')
# print(df)


def login():
    print("Silahkan masukkan Nama dan NRP anda:")
    print("==============================")
    nama = input('Nama: ')
    nrp = input("Nrp : ")
    print("==============================")
    with open('Data_peminjam.csv', mode='r', newline='')as f:
        reader = csv.reader(f)    
        for row in reader :
            if (row[0] == nama and row[1] == nrp):
                print('Selamat datang',nama,'di perpustakaan Maranatha')
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
                menu()
                break
        else:
            print("Data tidak ditemukan.")
            daftars()

def menu():
    print("==============================")
    print("Selamat datang di Menu untuk Peminjam")
    print("0. Logout")
    print("1. Lihat Buku")
    print("2. Pinjam Buku")
    print("3. Ruang Diskusi")
    print("==============================")
    pilihan = input("Masukkan pilihan (0/1/2/3): ")
    if pilihan == '1':
        lihatbuku()
        print()
    elif pilihan == '2':
        print("belum ada co")
    elif pilihan == '3':
        print("belum ada co")
    elif pilihan == '0':
        print("Logout berhasil. Kembali ke menu utama.")
        main()
    else:
        print("Pilihan tidak valid.")

def lihatbuku():
    # kategori buku
    # berdasarkan judul, stok, dan aisle nya
    kategori = 4
    science = [['Farmacy',2,'A1'],['Berserk',3,'A3'],['Berserk',3,'A3'],['Berserk',3,'A3']] 
    sejarah = [['Farmacy',2,'A1'],['Berserk',3,'A3'],['Berserk',3,'A3'],['Berserk',3,'A3']]
    novel = [['Farmacy',2,'A1'],['Berserk',3,'A3'],['Berserk',3,'A3'],['Berserk',3,'A3']]
    majalah = [['Farmacy',2,'A1'],['Berserk',3,'A3'],['Berserk',3,'A3'],['Berserk',3,'A3']]
    print()
    print("===== DAFTAR BUKU PER KATEGORI =====")
    print("KATEGORI: Science")
    print("====================================")
    print("stok = ",)
    print("====================================")
    for i in range(0, kategori, 1):
        print(science[i][0], "-", science[i][1], "-", science[i][2])
    print()
    print("KATEGORI: Sejarah")
    print("====================================")
    print("stok = ",)
    print("====================================")
    for i in range(0, kategori, 1):
        print(sejarah[i][0], "-", sejarah[i][1], "-", sejarah[i][2])
    print()
    print("KATEGORI: Novel")
    print("====================================")
    print("stok = ",)
    print("====================================")
    for i in range(0, kategori, 1):
        print(novel[i][0], "-", novel[i][1], "-", novel[i][2])
    print()
    print("KATEGORI: Majalah")
    print("====================================")
    print("stok = ",)
    print("====================================")
    for i in range(0, kategori, 1):
        print(majalah[i][0], "-", majalah[i][1], "-", majalah[i][2])
    print("________________________________________")
    
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
    return
def main():
# Perintah Input
    print("Selamat Datang di Perpustakaan Maranatha!!")
    print("Apakah anda ingin login?")
    print("==============================")
    print("0. Keluar")
    print("1. Login sebagai Peminjam")
    print("2. Login sebagai Staff")
    print("==============================")
    cek = input("Masukkan pilihan anda (0/1/2): ")
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