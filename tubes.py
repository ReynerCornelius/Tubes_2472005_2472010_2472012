# File : Tubes.py 
# Penulis : 2472010 2472012 2472005
# Tujuan Program :
#
# Kamus Data :
#
def peminjam(cek):
    kita = 3
    peminjam_nama = kita * [None]
    peminjam_nama[0] = "Jason"
    peminjam_nama[1] = "Reyner"
    peminjam_nama[2] = "Jonathan"
    peminjam_nrp = kita * [None]
    peminjam_nrp[0] = 2472012
    peminjam_nrp[1] = 2472005
    peminjam_nrp[2] = 2472010
    nrp = int(input("Nrp :"))
    indeks = cari_peminjam(nrp)
    if nrp == peminjam_nrp[indeks]:
        print(f"Selamat datang {peminjam_nama[indeks]} - {peminjam_nrp[indeks]}")
    else:
        print("Nrp tidak terdaftar")
        return 0
        
def cari_peminjam(nrp):
    kita = 3
    peminjam_nrp = kita * [None]
    peminjam_nrp[0] = 2472012
    peminjam_nrp[1] = 2472005
    peminjam_nrp[2] = 2472010
    for i in range (0,kita,1):
        if nrp == peminjam_nrp[i]:
            return i
    return 0

# def daftar(cek):

def main():
# Perintah Input
    cek = int(input("Apakah anda Exit/Peminjam/Staff (0,1,2) :"))
    if cek == 1:
        peminjam(cek)
    # elif cek == 2:

        
# Perintah Proses
    
# Perintah Output
    return 0
if __name__ == '__main__':    
    main()   