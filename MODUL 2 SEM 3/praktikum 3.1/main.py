class Mobil:
    #kelas variabel
    total_mobil_dibuat = 0

    #konstruktor
    def __init__(self, nama):
        #atribbut objek
        self.nama = nama 
        #mengakses atribut class
        Mobil.total_mobil_dibuat += 1 

    def nyalakan_mesin(self):
        print(f"Mesin {self.nama} menyala!")

    @classmethod
    def get_total_produksi(cls):
        print(f"Pabrik telah memproduksi {cls.total_mobil_dibuat} unit mobil.")


Mobil.get_total_produksi() 

print("--- Membuat mobil ---")
avanza = Mobil("Avanza")
xenia = Mobil("Xenia")
print("---------------------")

Mobil.get_total_produksi()