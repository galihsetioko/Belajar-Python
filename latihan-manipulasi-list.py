# Nama : Galih Setyoko
# INstagram : instagram.com/galihstyoko

# Disini kita akan memodifikasi list
nama = ['irfan', 'indra', 'udin', 'maman']

# mengambil string 'indra'
print('Mengambil indeks ke - 1 : ',nama[1])
print('Mengambil indeks ke - 2 : ', nama[-2])

# menambahkan item di list
print('List sebelum ditambahkan : ',nama)
nama.insert(3, 'dika')
print('List sesudah ditambahkan : ',nama)

# menambhkan item di akhir list
nama.append('Asep')
print('List ketika ditambahkan di akhir : ',nama)

# memasukan list baru ke dalam list lama
nama_baru = ['rina', 'tia', 'mila', 'naura']
nama.extend(nama_baru)
print("List baru ditambah list lama menjadi : \n\t",nama)

# mengganti item di dalam list
nama[4] = 'Ramos'
print(f"Daftar list ketika diganti indeks ke -4 nya : {nama}")

# meremove data
nama.remove('udin')
print(f"Daftar list ketika dihapus item 'udin' : {nama}")

# meremove data dari belakang
nama.pop()
print(f"Daftar list ketika dihapus item paling belakangnya : {nama}")
