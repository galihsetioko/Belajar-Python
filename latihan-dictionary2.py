# Galih Setioko
# https://instagram.com/galihstyoko

import os , random, string
dict_template = {
    'nama':'user',
    'id_num':'00000',
    'plant':'unknown',
    'source':'unknown'
}

os.system('cls')
data_thumbnail = dict(dict_template.fromkeys(dict_template.keys()))
data = {}
print('-'*70)
print(f"{'MAIN PROGRAM':^70}")
print('-'*70)

while True:
    nama_user = input('Masukkan Nama : ')
    id_num_user = input('Masukkan ID Number 00000 : ')
    plant_user = input('Masukkan Lokasi Plant (Sunter/Karawang) : ')
    source_user = input('Masukkan Source (BKK/Disnaker) : ')

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_thumbnail['nama'] = nama_user
    data_thumbnail['id_num'] = id_num_user
    data_thumbnail['plant'] = plant_user
    data_thumbnail['source'] = source_user

    data.update({KEY:data_thumbnail})

    print('\n')
    print(f"{'KEY':<8}{'NAMA':<16} {'ID':<5} {'PLANT':<9} {'SOURCE':<9}")
    for i in data:
        print(f"{i:<7}{data[i]['nama']:<16} {data[i]['id_num']:<5} {data[i]['plant']:<9} {data[i]['source']:<9}")
    print('\n')
    answer = input('Lanjutkan mengisi data ? (y/n)')
    if answer == 'n':
        break

print('Akhir dari Program...')
