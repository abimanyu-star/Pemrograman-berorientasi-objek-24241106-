class Pegawai:
    def __init__(self, nama: str, nip: str, gaji_pokok: int):
        # Konstruktor class Pegawai (parent)
        # Menyimpan nama, NIP, dan gaji pokok (bersifat private)
        self.nama = nama
        self.nip = nip
        self.__gaji_pokok = int(gaji_pokok)   # atribut private (encapsulation)

    def get_gaji_pokok(self) -> int:
        # Getter untuk mengambil nilai gaji pokok
        return self.__gaji_pokok

    def hitung_bonus(self) -> int:
        # Method default untuk menghitung bonus
        # Di parent class nilainya 0, nanti di-override oleh child
        return 0

    def get_gaji_total(self) -> int:
        # Menghitung total gaji = gaji pokok + bonus
        return self.__gaji_pokok + self.hitung_bonus()

    def tampilkan_info(self) -> str:
        # Menampilkan informasi dasar pegawai
        return f"Nama: {self.nama}, NIP: {self.nip}\nGaji Pokok: {format_rp(self.__gaji_pokok)}"


class Manager(Pegawai):
    def __init__(self, nama: str, nip: str, gaji_pokok: int, tunjangan_jabatan: int):
        # Memanggil konstruktor parent (Pegawai) agar nama, NIP, gaji pokok terisi
        super().__init__(nama, nip, gaji_pokok)
        # Menambahkan atribut khusus Manager
        self.tunjangan_jabatan = int(tunjangan_jabatan)

    def hitung_bonus(self) -> int:
        # Override method bonus di parent
        # Manager mendapatkan bonus 15% dari gaji pokok
        return int(self.get_gaji_pokok() * 0.15)

    def tampilkan_info(self) -> str:
        # Override tampilkan_info dengan menambah info tunjangan jabatan
        base = super().tampilkan_info()
        return base + f"\nTunjangan: {format_rp(self.tunjangan_jabatan)}"


class StaffTeknis(Pegawai):
    def __init__(self, nama: str, nip: str, gaji_pokok: int, jumlah_proyek: int):
        # Memanggil konstruktor parent
        super().__init__(nama, nip, gaji_pokok)
        # Atribut khusus staff teknis
        self.jumlah_proyek = int(jumlah_proyek)

    def hitung_bonus(self) -> int:
        # Override: staff teknis dapat bonus 500 ribu per proyek
        return 500_000 * self.jumlah_proyek

    def tampilkan_info(self) -> str:
        # Menambahkan info jumlah proyek
        base = super().tampilkan_info()
        return base + f"\nJumlah Proyek: {self.jumlah_proyek}"


def format_rp(amount: int) -> str:
    # Format angka menjadi format Rupiah
    return "Rp " + format(int(amount), ",d")


if __name__ == '__main__':

    # Membuat objek Manager
    manager = Manager("Budi Hartono", "M-001", 10_000_000, tunjangan_jabatan=5_000_000)

    # Membuat objek Staff Teknis
    staff = StaffTeknis("Susi Susanti", "S-001", 6_000_000, jumlah_proyek=3)

    # Output untuk Manager
    print("--- Info Manager ---")
    print(manager.tampilkan_info())
    print(f"Gaji Total Manager: {format_rp(manager.get_gaji_total())}\n")

    print("==============================\n")

    # Output untuk Staff Teknis
    print("--- Info Staff Teknis ---")
    print(staff.tampilkan_info())
    print(f"Gaji Total Staff: {format_rp(staff.get_gaji_total())}\n")

    print("==============================\n")

    print("--- Tes Keamanan (Encapsulasi) ---")
    try:
        # Mencoba mengakses atribut private (akan error)
        print(staff.__gaji_pokok)
    except AttributeError as e:
        # Menunjukkan bahwa atribut private tidak bisa diakses langsung
        print(f"ERROR: {e}")
        print("-> TIDAK BISA diakses langsung dari luar!")

    # Mengakses melalui method resmi (getter)
    print(f"Gaji Total Susi (tetap): {format_rp(staff.get_gaji_total())}")
