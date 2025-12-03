class Kendaraan:
    def __init__(self, nama):
        # Konstruktor (parent class)
        # Dipanggil ketika objek dibuat.
        # Menampilkan bahwa konstruktor parent dijalankan.
        print("-> (Parent __init__ dipanggil)")

        # Menyimpan nama kendaraan ke dalam atribut objek.
        self.nama = nama


class Mobil(Kendaraan):
    def __init__(self, nama, jumlah_pintu):
        # Konstruktor (child class)
        # Menampilkan bahwa konstruktor child dijalankan.
        print("-> (Child __init__ dipanggil)")

        # Memanggil konstruktor parent (Kendaraan)
        # Agar atribut 'nama' dapat diinisialisasi oleh parent.
        super().__init__(nama)

        # Menambahkan atribut baru: jumlah pintu
        self.jumlah_pintu = jumlah_pintu

        # Menampilkan informasi mobil yang berhasil dibuat
        print(f"   -> Mobil {self.nama} dengan {self.jumlah_pintu} pintu dibuat.")


# Membuat objek Mobil bernama "Xenia Hitam" dengan 4 pintu.
xenia = Mobil("Xenia Hitam", 4)

# Menampilkan nama object yang telah disimpan dari parent class.
print(f"Nama object: {xenia.nama}")
