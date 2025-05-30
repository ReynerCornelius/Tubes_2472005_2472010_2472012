# File : Tubes.py 
# Penulis : 2472010 2472012 2472005
# Tujuan Program :
#
# Kamus Data :
import csv

def login():
    print("Silahkan masukan Nama dan NRP anda:")
    print("==============================")
    nama = input('Nama: ')
    nrp = input("Nrp : ")
    print("==============================")
    with open('Data_peminjam.csv', mode='r', newline='')as f:
        reader = csv.reader(f)    
        for row in reader :
            if (row[0] == nama and row[1] == nrp):
                print('Hi')
                menu()
        else:
            print()
            daftar()
            
def menuPeminjam():
    print("|                                |")
    
    
    
    
    
    
    
    
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
    
def main():
# Perintah Input
    print("Selamat Datang di Perpustakaan Maranatha!!")
    print("Apakah anda ingin login?")
    print("==============================")
    cek = int(input("Ingin login sebagai apa? Exit/Peminjam/Staff (0,1,2) :"))
    print("==============================")
    if cek == 1:
        login()
    # elif cek == 2:

        
# Perintah Proses
    
# Perintah Output
    return 0
if __name__ == '__main__':    
    main()   