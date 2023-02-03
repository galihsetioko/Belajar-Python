# Galih Setioko
# Instagram : instagram.com/galihstyoko

# Aplikasi sederhana untuk menghitung umur

import datetime as dt

print('\n')
tanggal = int(input("Masukkan tanggal :".ljust(25)))
bulan = int(input("Masukkan bulan   :".ljust(25)))
tahun = int(input("Masukkan tahun   :".ljust(25)))
hari_umur = dt.date(tahun, bulan, tanggal)
umur_total = dt.date.today() - hari_umur
print("\nUmur anda adalah :".ljust(20) + f"{umur_total.days // 365} tahun")

print('\n')