# Galih Setioko
# https://instagram.com/galihstyoko

data_dict = {
    'gs':'galih setioko',
    'imc':'ibrahimovic',
    'emv':'egy maulana vikri',
}

# menampilkan dict_items menggunakan get()
print(f'Mengambil items {data_dict.get("gs")}')

# mengecek item di dalam dictionary
print(f"Items 'gs' apakah ada di dalam dictionary ? {'gs' in data_dict}")

# mengupdate data menggunakan update()
data_dict.update({'man':'maman suherman'})
print(f'{data_dict}')

# menghapus items di dalam dictionary
del data_dict['man']
print(data_dict)
