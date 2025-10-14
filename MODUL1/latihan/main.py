# TUGAS PRAKTIKUM MODUL 1
# Program menghitung luas dan keliling persegi panjang dengan konsep OOP

class PersegiPanjang:
    # Konstruktor untuk inisialisasi atribut panjang dan lebar
    def _init_(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    # Method untuk menghitung luas
    def hitung_luas(self):
        return self.panjang * self.lebar

    # Method untuk menghitung keliling
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

# Program utama

print("=== Program Menghitung Luas dan Keliling Persegi Panjang ===")

# Input data dari pengguna
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

# Membuat objek dari kelas PersegiPanjang
persegi_panjang = PersegiPanjang(panjang, lebar)

# Menampilkan hasil perhitungan
print(f"\nLuas Persegi Panjang = {persegi_panjang.hitung_luas()}")
print(f"Keliling Persegi Panjang = {persegi_panjang.hitung_keliling()}")