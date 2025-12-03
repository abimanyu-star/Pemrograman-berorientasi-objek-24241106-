class Kendaraan:
    def __init__(self, nama):
        # Konstruktor: dijalankan saat objek dibuat.
        # Menyimpan nama kendaraan dan menampilkan pesan saat objek dibuat.
        self.nama = nama
        print(f"Sebuah Kendaraan '{self.nama}' dibuat.")

    def maju(self):
        # Method untuk membuat kendaraan bergerak maju.
        print(f"{self.nama} bergerak maju.")

class Mobil(Kendaraan):
    # Class Mobil mewarisi semua atribut dan method dari class Kendaraan.

    def putar_AC(self):
        # Method khusus untuk Mobil.
        # Mensimulasikan fitur menyalakan AC pada mobil.
        print(f"{self.nama}: AC dinyalakan, sejuk!")

print("--- Membuat Object Mobil ---")
# Membuat objek Mobil dengan nama "Avanza Putih".
avanza = Mobil("Avanza Putih")

# Memanggil method 'maju' yang diwarisi dari class Kendaraan.
avanza.maju()

# Memanggil method khusus class Mobil.
avanza.putar_AC()
