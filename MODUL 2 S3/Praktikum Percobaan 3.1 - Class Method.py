class Mobil:
    
    total_mobil_dibuat = 0 

    def __init__(self, nama):
        self.nama = nama 
        Mobil.total_mobil_dibuat += 1 

    def nyalakan_mesin(self):
        print(f"Mesin {self.nama} menyala!")

    @classmethod
    def get_total_produksi(cls):
        print(f"Pabrik telah memproduksi {cls.total_mobil_dibuat} unit mobil.")

# akses metod dari class tanpa membuat objek
Mobil.get_total_produksi() 

print("--- Membuat mobil ---")
avanza = Mobil("Avanza")
xenia = Mobil("Xenia")
print("---------------------")

# akses metod dari class
Mobil.get_total_produksi()





#| Jenis              | Nama                         | Penjelasan                                |
#| ------------------ | ---------------------------- | ----------------------------------------- |
#| **Atribut class**  | `total_mobil_dibuat`         | Menghitung total mobil dibuat             |
#| **Atribut objek**  | `nama`                       | Menyimpan nama tiap mobil                 |
#| **Method objek**   | `nyalakan_mesin()`           | Menyalakan mesin mobil tertentu           |
#| **Class method**   | `get_total_produksi()`       | Menampilkan total produksi mobil          |
#| **Perintah class** | `Mobil.get_total_produksi()` | Menjalankan class method tanpa buat objek |
