class Kalkulator:

    def __init__(self, nilai_awal):
        self.nilai = nilai_awal
    
    def tambah(self, angka):
        self.nilai += angka
        return self.nilai

    @staticmethod
    def kali(a, b):
        return a * b

calc = Kalkulator(10)
print(f"Hasil tambah: {calc.tambah(5)}") #menambah angka

print(f"Hasil kali: {Kalkulator.kali(5, 3)}") # mengalikan 2 angka



#🔹 print(f"Hasil tambah: {calc.tambah(5)}")
#➡️ Memanggil method objek tambah(), menambah nilai awal 10 + 5 = 15, lalu mencetak hasilnya.
#🔹 print(f"Hasil kali: {Kalkulator.kali(5, 3)}")
#➡️ Memanggil static method kali() langsung dari class, menghitung 5 × 3 = 15, lalu mencetak hasilnya.
#🔸 Perbedaannya:
#calc.tambah(5)	Kalkulator.kali(5, 3)
#Butuh objek (calc)	Tidak butuh objek
#Mengubah data objek	Hanya menghitung biasa
#Method objek	Static method