# Galih Setioko
# Instagram.com/galihstyoko

import os
dict_template = {
    'nama':'user',
    'desa':'unknown',
    'bahasa':'undefined',
}

os.system('cls')
print(f"{'DATA SCIENTIC':^40}")
print("-"*40)

while True:
    data = dict(dict_template.fromkeys(dict_template.keys()))
    print(data)
    NAMA_USER = input("Masukkan nama : ")
    NAMA_DESA = input("Masukkan desa : ")
    NAMA_BAHASA = input("Masukkan bahasa : ")
    data['nama'] = NAMA_USER
    data['desa'] = NAMA_DESA
    data['bahasa'] = NAMA_BAHASA
    print(data)
