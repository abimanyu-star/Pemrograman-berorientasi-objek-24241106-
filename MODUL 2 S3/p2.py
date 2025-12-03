class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama          # Public attribute (boleh diakses luar class)
        self.__saldo = saldo      # Private attribute (tidak boleh diakses langsung)

    

# --- Bagian program utama ---
akun_budi = RekeningBank("Budi", 1000000)

print(f"Nama pemilik rekening: {akun_budi.nama}")  # ✅ Bisa diakses

# Berikut ini akan ERROR karena saldo bersifat private
print(f"Saldo awal Budi: {akun_budi.__saldo}")     # ❌ ERROR
