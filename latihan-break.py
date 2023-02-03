# Nama : Galih Setioko
# Instagram : instagram.com/galihstyoko

''' 
Dengan break , looping akan berhenti , ketika bertemu dengan statement yang bernilai true

'''

num = 0
while num < 10:
    num += 1
    if num == 6:
        print(f"Angka nomor {num} sudah ditemukan , Program berhenti...")
        break # <--- Jika syntax break dihapus , maka perulangan akan terus sampai angka 10
    print(f"Perulangan berjalan di angka - {num} ")