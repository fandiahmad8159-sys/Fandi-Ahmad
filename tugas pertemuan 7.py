"""
Latihan Python Date and Time
Solusi untuk 8 soal latihan. Jalankan: python latihan_datetime.py
"""

import time
from datetime import date, datetime, timedelta

HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
         "Agustus", "September", "Oktober", "November", "Desember"]


def judul(nomor, teks):
    print(f"\n=== Soal {nomor}: {teks} ===")


# Soal 1: tanggal hari ini, format "24 Oktober 2026"
def soal1():
    judul(1, "Tanggal hari ini (bulan bahasa Indonesia)")
    hari_ini = date.today()
    print(f"{hari_ini.day} {BULAN[hari_ini.month - 1]} {hari_ini.year}")


# Soal 2: nama hari kelahiran
def soal2():
    judul(2, "Nama hari kelahiran")
    lahir = datetime(2005, 8, 17)  # ganti dengan tanggal lahir Anda
    print(f"{lahir.strftime('%d-%m-%Y')} jatuh pada hari {HARI[lahir.weekday()]}")


# Soal 3: hitung hari menuju ujian akhir semester
def soal3():
    judul(3, "Hari menuju ujian akhir semester")
    ujian = date(2027, 1, 18)  # ganti dengan tanggal ujian Anda
    sisa = (ujian - date.today()).days
    if sisa >= 0:
        print(f"{sisa} hari lagi menuju ujian")
    else:
        print(f"Ujian sudah lewat {-sisa} hari yang lalu")


# Soal 4: input tanggal DD-MM-YYYY, tampilkan hari, tangani format salah
def soal4():
    judul(4, "Hari dari tanggal input")
    teks = input("Tanggal (24-10-2026): ")
    try:
        tgl = datetime.strptime(teks, "%d-%m-%Y")
        print("Hari:", HARI[tgl.weekday()])
    except ValueError:
        print("Format tanggal tidak valid. Contoh yang benar: 24-10-2026")


# Soal 5: 100 hari dari sekarang dan 100 hari yang lalu
def soal5():
    judul(5, "100 hari ke depan dan ke belakang")
    hari_ini = date.today()
    print("100 hari lagi  :", hari_ini + timedelta(days=100))
    print("100 hari lalu  :", hari_ini - timedelta(days=100))


# Soal 6: timestamp 1700000000 menjadi tanggal dan jam
def soal6():
    judul(6, "Timestamp ke tanggal dan jam")
    ts = 1700000000
    w = datetime.fromtimestamp(ts)  # zona waktu lokal komputer
    print(f"Timestamp {ts} = {w.strftime('%d-%m-%Y %H:%M:%S')} (waktu lokal)")


# Soal 7: hitung mundur 10 detik
def soal7():
    judul(7, "Hitung mundur 10 detik")
    for sisa in range(10, 0, -1):
        print(f"Sisa {sisa} detik")
        time.sleep(1)
    print("Selesai!")


# Soal 8: ukur durasi sebuah proses
def soal8():
    judul(8, "Durasi proses")
    mulai = time.time()
    print("Waktu mulai  :", datetime.fromtimestamp(mulai).strftime("%H:%M:%S"))

    total = sum(i * i for i in range(5_000_000))  # contoh proses

    selesai = time.time()
    print("Waktu selesai:", datetime.fromtimestamp(selesai).strftime("%H:%M:%S"))
    print(f"Hasil proses : {total}")
    print(f"Durasi       : {selesai - mulai:.3f} detik")


if __name__ == "__main__":
    soal1()
    soal2()
    soal3()
    soal4()
    soal5()
    soal6()
    soal7()
    soal8()
