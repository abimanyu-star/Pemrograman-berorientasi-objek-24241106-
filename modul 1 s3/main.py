# Class atribute / class objek
jumlah_mahasiswa = 0

# konstruktor
def  __init__(self,nama,nim,prodi):
    #
    self,nama=nama
    self,nim=nim
    self,prodi=prodi
    mahasiswa, jumlah_mahasiswa += 1
    print(f"membuat objek mahasiswa dengan nama"+ self.nama)

# membuat objek 
mhs1 = jumlah_mahasiswa("sandi", "24241019","pti")

