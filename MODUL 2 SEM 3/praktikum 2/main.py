class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo 


akun_budi = RekeningBank("Budi", 1000000)
akun_budi.saldo = -5000000

try:
    print(akun_budi.__saldo)
except AttributeError:
    print('error saldo tidak dapat di akses')