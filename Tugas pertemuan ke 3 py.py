class Mahasiswa:
    def __init__(self, nama, nim, jurusan, nilai):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai = nilai
        self.kelas = "B"

    def cek_status(self):
        if self.nilai >= 75:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def tampilkan_profil(self):
        print("Nama       :", self.nama)
        print("NIM        :", self.nim)
        print("Jurusan    :", self.jurusan)
        print("Nilai      :", self.nilai)
        print("Status     :", self.cek_status())
        print("-" * 40)
    


# Membuat minimal 3 objek mahasiswa
mahasiswa1 = Mahasiswa(
    "Fandi Ahmad",
    "2595114028",
    "Teknik Informatika",
    85
)

mahasiswa2 = Mahasiswa(
    "Alvarado Vareza",
    "2595114025",
    "Teknik Informatika",
    72
)

mahasiswa3 = Mahasiswa(
    "Tangguh Gilang Saputra",
    "2595114026",
    "Teknik Informatika",
    90
)


# Menampilkan seluruh profil mahasiswa
print("=== SISTEM PENDATAAN MAHASISWA ===")
print()

mahasiswa1.tampilkan_profil()
mahasiswa2.tampilkan_profil()
mahasiswa3.tampilkan_profil() 


# Class Induk: Kendaraan
class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def tampilkan_info(self):
        print(f"Nama      : {self.nama}")
        print(f"Merk      : {self.merk}")
        print(f"Tahun     : {self.tahun}")
        print(f"Kecepatan : {self.kecepatan} km/jam")


# Turunan 1: Mobil (Mewarisi sifat dari Kendaraan)
class Mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        # Memanggil constructor class induk (Kendaraan)
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jml Kursi : {self.jumlah_kursi}")


# Turunan 2: Motor (Mewarisi sifat dari Kendaraan)
class Motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        # Memanggil constructor class induk (Kendaraan)[cite: 1]
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Tipe Motor: {self.tipe_motor}")


# --- Contoh Penggunaan ---
if __name__ == "__main__":
    print("=== DRAFT ARMADA RENTAL KENDARAAN ===\n")

    # Membuat objek Mobil[cite: 1]
    mobil1 = Mobil(
        nama="Avanza Veloz",
        merk="Toyota",
        tahun=2022,
        kecepatan=180,
        jumlah_kursi=7,
    )
    print("[ Data Mobil ]")
    mobil1.tampilkan_info()

    print("\n" + "=" * 35 + "\n")

    # Membuat objek Motor[cite: 1]
    motor1 = Motor(
        nama="NMAX 155",
        merk="Yamaha",
        tahun=2023,
        kecepatan=120,
        tipe_motor="Matik",
    )
    print("[ Data Motor ]")
    motor1.tampilkan_info() 

    # Class Induk 1: Informasi Dasar Pegawai
class Pegawai:
    def __init__(self, id_pegawai, nama):
        self.id_pegawai = id_pegawai
        self.nama = nama

    def tampilkan_pegawai(self):
        print(f"ID Pegawai : {self.id_pegawai}")
        print(f"Nama       : {self.nama}")


# Class Induk 2: Sistem Penggajian (Payroll)
class Gaji:
    def __init__(self, gaji):
        self.gaji = gaji

    def tampilkan_gaji(self):
        print(f"Gaji Utama : Rp {self.gaji:,.2f}")


# Class Induk 3: Pelaporan Proyek
class PegawaiProyek:
    def __init__(self, nama_proyek):
        self.nama_proyek = nama_proyek

    def tampilkan_proyek(self):
        print(f"Nama Proyek: {self.nama_proyek}")


# Class Turunan: Project Manager (Mewarisi 3 Class Induk)
class ProjectManager(Pegawai, Gaji, PegawaiProyek):
    def __init__(self, id_pegawai, nama, gaji, nama_proyek, tunjangan_manager=0):
        # Inisialisasi masing-masing class induk
        Pegawai.__init__(self, id_pegawai, nama)
        Gaji.__init__(self, gaji)
        PegawaiProyek.__init__(self, nama_proyek)
        self.tunjangan_manager = tunjangan_manager

    def tampilkan_info_lengkap(self):
        print("=== AGREGASI DATA PROJECT MANAGER ===")
        self.tampilkan_pegawai()
        self.tampilkan_proyek()
        self.tampilkan_gaji()
        if self.tunjangan_manager > 0:
            print(f"Tunjangan  : Rp {self.tunjangan_manager:,.2f}")
            total = self.gaji + self.tunjangan_manager
            print(f"Total Gaji : Rp {total:,.2f}")


# --- Contoh Penggunaan ---
if __name__ == "__main__":
    # Membuat objek ProjectManager
    pm1 = ProjectManager(
        id_pegawai="PM-2026-001",
        nama="Budi Santoso",
        gaji=15000000,
        nama_proyek="Migrasi Sistem Cloud",
        tunjangan_manager=3000000,
    )

    # Menampilkan agregasi data lengkap
    pm1.tampilkan_info_lengkap() 