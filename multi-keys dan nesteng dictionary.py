# Galih setyoko
# Instagram : instagram.com/galihstyoko

mahasiswa1 = {
    'nama':'Galih Setioko',
    'bahasa':'Python',
    'jurusan':'Tehnik Mesin',
}
mahasiswa2 = {
    'nama':'Ika',
    'bahasa':'Matlab',
    'jurusan':'Tehnik Elektro',
}
mahasiswa3 = {
    'nama':'Tia',
    'bahasa':'Javascript',
    'jurusan':'Tehnik Geologi',
}

datamas = {
    'MH001':mahasiswa1,
    'MH002':mahasiswa2,
    'MH003':mahasiswa3,
}

print('\n')
print(f"{'KEY':<6} {'NAMA':<14} {'BAHASA':<13} {'JURUSAN':<15}")
print("".center(45,'-'))

for i in datamas:
    KEY = i
    NAMA = datamas[i]['nama']
    BAHASA = datamas[i]['bahasa']
    JURUSAN = datamas[i]['jurusan']
    # print(NAMA)
    print(f"{KEY:<6} {NAMA:<14} {BAHASA:<13} {JURUSAN:<15}")
