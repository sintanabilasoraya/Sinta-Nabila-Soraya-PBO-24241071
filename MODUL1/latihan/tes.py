class PersegiPanjang:
    def __init__(self, panjang, lebar):
        """
        Konstruktor untuk menginisialisasi panjang dan lebar persegi panjang.
        """
        self.panjang = panjang
        self.lebar = lebar
    
    def hitung_luas(self):
        """
        Metode untuk menghitung luas persegi panjang (panjang * lebar).
        """
        return self.panjang * self.lebar
    
    def hitung_keliling(self):
        """
        Metode untuk menghitung keliling persegi panjang (2 * (panjang + lebar)).
        """
        return 2 * (self.panjang + self.lebar)

# Program utama

# Input dari pengguna
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))
    
# Membuat objek dari kelas PersegiPanjang
persegi = PersegiPanjang(panjang, lebar)
    
# Menghitung dan menampilkan hasil
luas = persegi.hitung_luas()
keliling = persegi.hitung_keliling()
    
print(f"\nLuas persegi panjang: {luas}")
print(f"Keliling persegi panjang: {keliling}")
