class Ayah:
    def __init__(self, nama_ayah):
        # Konstruktor class Ayah
        # Menyimpan nama ayah ke dalam atribut objek
        self.nama_ayah = nama_ayah
    
    def bekerja(self):
        # Method milik class Ayah
        # Menampilkan aktivitas ayah
        print(f"{self.nama_ayah} sedang bekerja.")


class Ibu:
    def __init__(self, nama_ibu):
        # Konstruktor class Ibu
        # Menyimpan nama ibu ke dalam atribut objek
        self.nama_ibu = nama_ibu

    def memasak(self):
        # Method milik class Ibu
        # Menampilkan aktivitas ibu
        print(f"{self.nama_ibu} sedang memasak.")


class Anak(Ayah, Ibu):
    # Class Anak melakukan multiple inheritance (mewarisi dari Ayah dan Ibu)

    def __init__(self, nama_anak, nama_ayah, nama_ibu):
        # Konstruktor class Anak
        # Memanggil konstruktor Ayah dan Ibu secara manual
        Ayah.__init__(self, nama_ayah)
        Ibu.__init__(self, nama_ibu)

        # Menambahkan atribut khusus anak
        self.nama_anak = nama_anak

    def bermain(self):
        # Method khusus milik class Anak
        print(f"{self.nama_anak} sedang bermain.")


# Membuat objek Anak yang mewarisi atribut & method dari Ayah dan Ibu
budi = Anak("Budi", "Hendra (Ayah)", "Wati (Ibu)")

# Memanggil method yang diwarisi dari parent Ayah
budi.bekerja()

# Memanggil method yang diwarisi dari parent Ibu
budi.memasak()

# Memanggil method milik class Anak
budi.bermain()
