class Pegawai:
    # constructor pegawai
    def __init__(self, nama: str, nip: str, gaji_pokok: int):
        self.nama = nama
        self.nip = nip
        self.__gaji_pokok = int(gaji_pokok)

        #getter gaji pokok
    def get_gaji_pokok(self) -> int:
        return self.__gaji_pokok

    # bonus default
    def hitung_bonus(self) -> int:
        return 0

    #hitung gaji total
    def get_gaji_total(self) -> int:
        return self.__gaji_pokok + self.hitung_bonus()

    #tampilkan info pegawai
    def tampilkan_info(self) -> str:
        return f"Nama: {self.nama}, NIP: {self.nip}\nGaji Pokok: {format_rp(self.__gaji_pokok)}"

#class maneger (tururnan pegawai)
class Manager(Pegawai):
    def __init__(self, nama: str, nip: str, gaji_pokok: int, tunjangan_jabatan: int):
        super().__init__(nama, nip, gaji_pokok)
        self.tunjangan_jabatan = int(tunjangan_jabatan)

    # override hitung_bonus()
    def hitung_bonus(self) -> int:
        return int(self.get_gaji_pokok() * 0.15)

    #override tampilkan info
    def tampilkan_info(self) -> str:
        base = super().tampilkan_info()
        return base + f"\nTunjangan: {format_rp(self.tunjangan_jabatan)}"

#class staffteknis (turunan pegawai)
class StaffTeknis(Pegawai):
    def __init__(self, nama: str, nip: str, gaji_pokok: int, jumlah_proyek: int):
        super().__init__(nama, nip, gaji_pokok)
        self.jumlah_proyek = int(jumlah_proyek)

# override hitung bonus
    def hitung_bonus(self) -> int:
        return 500_000 * self.jumlah_proyek

#override tampilkan info                                                                                                                                                                                    
    def tampilkan_info(self) -> str:
        base = super().tampilkan_info()
        return base + f"\nJumlah Proyek: {self.jumlah_proyek}"

#function format_rp()
def format_rp(amount: int) -> str:
    return "Rp " + format(int(amount), ",d")

if __name__ == '__main__':

#membuat objek
    manager = Manager("Budi Hartono", "M-001", 10_000_000, tunjangan_jabatan=5_000_000)
    staff = StaffTeknis("Susi Susanti", "S-001", 6_000_000, jumlah_proyek=3)

    # Output Manager
    print("--- Info Manager ---")
    print(manager.tampilkan_info())
    print(f"Gaji Total Manager: {format_rp(manager.get_gaji_total())}\n")

    print("==============================\n")

    # Output Staff Teknis
    print("--- Info Staff Teknis ---")
    print(staff.tampilkan_info())
    print(f"Gaji Total Staff: {format_rp(staff.get_gaji_total())}\n")

    print("==============================\n")

    print("--- Tes Keamanan (Encapsulasi) ---")
    
    #tes keamanan (encapsulasi)
    try:

        print(staff.__gaji_pokok)  
    except AttributeError as e:
        print(f"ERROR: {e}")
        print("-> TIDAK BISA diakses langsung dari luar!")

    print(f"Gaji Total Susi (tetap): {format_rp(staff.get_gaji_total())}")