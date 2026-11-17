from abc import ABC, abstractmethod

# Abstraction
class Karyawan(ABC):
    def __init__(self, nama, nip):
        self._nama = nama  
        self._nip = nip

    @abstractmethod
    def hitung_gaji(self):
        pass

    def get_info(self):
        return f"Nama: {self._nama}, NIP: {self._nip}"

# Inheritance & Encapsulation
class KaryawanTetap(Karyawan):
    def __init__(self, nama, nip, gaji_pokok):
        super().__init__(nama, nip)
        self.__gaji_pokok = gaji_pokok  

    def hitung_gaji(self):
        return self.__gaji_pokok

class KaryawanKontrak(Karyawan):
    def __init__(self, nama, nip, tarif_harian, jumlah_hadir):
        super().__init__(nama, nip)
        self.tarif_harian = tarif_harian
        self.jumlah_hadir = jumlah_hadir

    def hitung_gaji(self):
        return self.tarif_harian * self.jumlah_hadir

if __name__ == "__main__":
    k1 = KaryawanTetap("Budi", "101", 5000000)
    k2 = KaryawanKontrak("Siti", "102", 150000, 20)

    daftar_karyawan = [k1, k2]

    # Polymorphism
    print("--- Rincian Gaji Karyawan ---")
    for karyawan in daftar_karyawan:
        print(karyawan.get_info())
        print(f"Total Gaji: Rp {karyawan.hitung_gaji():,}\n")