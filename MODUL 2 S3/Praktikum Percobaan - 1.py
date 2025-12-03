class Hero:

    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        self.__private = 'private'
        self.__protected = 'protected'

hero_1 = Hero('Atsu', 100)

print(hero_1.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah)





#Perbedaan jumlah dan __privateJumlah
#jumlah → variabel publik, bisa diakses langsung (Hero.jumlah).
#__privateJumlah → variabel private, tidak bisa diakses langsung karena Python menyembunyikannya (jadi _Hero__privateJumlah).

#Penjelasan tiga perintah print
#print(hero_1.__dict__)
#→ Menampilkan semua atribut milik objek hero_1.
#print(Hero.__dict__)
#→ Menampilkan semua atribut dan fungsi milik kelas Hero.
#Termasuk:
#jumlah, _Hero__privateJumlah, dan __init__.
#print(Hero.__privateJumlah)
#❌ Error, karena __privateJumlah disembunyikan oleh Python.
#Cara benar mengaksesnya:
#print(Hero._Hero__privateJumlah)