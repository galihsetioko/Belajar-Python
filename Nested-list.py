# Nama : Galih Setioko
# Instagram : instagram.com/galihstyoko

# Nested list artinya list di dalam list , atau biasa disebut juga dengan list 2 dimensi
# Fungsinya adalah untuk menampilkan atau menyimpan data yang lebih komplek/ber seri
# Contohnya adalah data nama , umur , gender dsb

data_siswa = [
    ['Galih', 18, 'Pria'],
    ['Maman', 23, 'Pria'],
    ['Mutia', 19, 'Wanita'],
]

print('\n')
# kita akan menampilkan data siswa mengunakan looping
for i in data_siswa : 
    print(f"Nama : {i[0]}")
    print(f"Umur : {i[1]}")
    print(f"Gender : {i[2]}\n")

# PERMASALAHAN REFERENCE DI LIST 2 DIMENSI
# Jika kamu menduplikat list 2 dimensi menggunakan method copy() untuk menhindari reference , kamu salah
# Karena list yang bersarang didalam , masih jadi referensi dari variabel list yang lama, jadi hanya address nya saja yang dicopy

# import modul deepcopy
from copy import deepcopy
# menginisialisasi variabel data baru menggunakn deepcopy
data_siswa_baru = deepcopy(data_siswa)

# Cari tau addresnya
print('ADDRESS DATA_SISWA'.center(40, '='))
print(f'Address list nama data_siswa : {hex(id(data_siswa))}')
print(f'Address member data_siswa : {hex(id(data_siswa[0]))}')

print('ADDRESS DATA_SISWA_BARU'.center(40, '='))
print(f'Address list nama data_siswa_baru : {hex(id(data_siswa_baru))}')
print(f'Address member data_siswa_baru : {hex(id(data_siswa_baru[0]))}')
