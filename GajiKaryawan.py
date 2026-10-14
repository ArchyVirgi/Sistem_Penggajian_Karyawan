class Karyawan:
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: float):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.__gaji_pokok = gaji_pokok  # Private attribute

    # Getter untuk gaji_pokok
    @property
    def gaji_pokok(self):
        return self.__gaji_pokok

    # Setter untuk gaji_pokok
    @gaji_pokok.setter
    def gaji_pokok(self, nilai_baru):
        if nilai_baru <= 0:
            print(f"[PERINGATAN] Gaji pokok untuk {self.nama} harus lebih dari 0!")
        else:
            self.__gaji_pokok = nilai_baru

    def hitung_gaji_total(self):
        return self.__gaji_pokok

    def tampilkan_info(self):
        print(f"ID Karyawan : {self.id_karyawan}")
        print(f"Nama        : {self.nama}")
        print(f"Gaji Pokok  : Rp{self.__gaji_pokok:,.2f}")


class KaryawanTetap(Karyawan):
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: float, tunjangan: float):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan  # Public attribute

    # Overriding method hitung_gaji_total
    def hitung_gaji_total(self):
        return self.gaji_pokok + self.tunjangan

    # Overriding method tampilkan_info
    def tampilkan_info(self):
        print("=== DATA KARYAWAN TETAP ===")
        super().tampilkan_info()
        print(f"Tunjangan   : Rp{self.tunjangan:,.2f}")
        print(f"Total Gaji  : Rp{self.hitung_gaji_total():,.2f}")
        print("-" * 30)


class KaryawanKontrak(Karyawan):
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: float, jam_lembur: int, tarif_lembur: float):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.jam_lembur = jam_lembur      # Public attribute
        self.tarif_lembur = tarif_lembur  # Public attribute

    # Overriding method hitung_gaji_total
    def hitung_gaji_total(self):
        return self.gaji_pokok + (self.jam_lembur * self.tarif_lembur)

    # Overriding method tampilkan_info
    def tampilkan_info(self):
        print("=== DATA KARYAWAN KONTRAK ===")
        super().tampilkan_info()
        print(f"Lembur      : {self.jam_lembur} jam (Tarif: Rp{self.tarif_lembur:,.2f}/jam)")
        print(f"Total Gaji  : Rp{self.hitung_gaji_total():,.2f}")
        print("-" * 30)


# ==========================================
# KETENTUAN PENGUJIAN KODE (MAIN PROGRAM)
# ==========================================

# 1. Membuat objek KaryawanTetap dan KaryawanKontrak
karyawan1 = KaryawanTetap("Damian Ragil", "T001", 5500000, 2000000)
karyawan2 = KaryawanKontrak("Khayla Putri", "K002", 3800000, 15, 60000)

# 2. Menyimpan kedua objek ke dalam list bernama daftar_karyawan
daftar_karyawan = [karyawan1, karyawan2]

# 3. Demonstrasi Polymorphism dengan looping
print("=== DEMONSTRASI POLYMORPHISM ===")
for karyawan in daftar_karyawan:
    karyawan.tampilkan_info()

# 4. Demonstrasi Encapsulation
print("\n=== DEMONSTRASI ENCAPSULATION ===")
# Mengubah gaji pokok dengan nilai tidak valid (<= 0)
print(f"Mencoba mengubah gaji pokok {karyawan1.nama} dengan nilai tidak valid (-500000):")
karyawan1.gaji_pokok = -500000

# Mengubah gaji pokok dengan nilai valid, lalu menampilkan ulang hasilnya
print(f"\nMencoba mengubah gaji pokok {karyawan1.nama} dengan nilai valid (6500000):")
karyawan1.gaji_pokok = 6500000

print(f"\nMenampilkan ulang info {karyawan1.nama} setelah perubahan gaji pokok:")
karyawan1.tampilkan_info()
