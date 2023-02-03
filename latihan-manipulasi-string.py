# Nama : Galih Setioko
# instagram.com/galihstyoko

print('\n')
# 1. Menyambung string (concatenate)
namaAwal = "Toni"
namaAkhir = "Sucipto"
namaLengkap = namaAwal + " " + namaAkhir
print(namaLengkap)

# 2. Menghitung panjang suatu string
print("Panjang nama",namaLengkap,"adalah",len(namaLengkap))

# 3. Operator untuk string

# mengecek apakah ada komponen krakter di dalam suatu string
stat = "u" in namaLengkap
print("Apakah huruf u ada di dalam nama",namaLengkap,"?", stat)
stat1 = "o" not in namaLengkap
print("Apakah huruf o tidak ada di dalam nama",namaLengkap,"?", stat1)

# mengulang string
print('Character o x 12 = '+'o'*12)

# indexing / mengambil / memotong character di dalam string
print('Karakter ke - 2 di dalam nama',namaLengkap,"adalah",namaLengkap[2])
# jika nomor index diisi dengan negatif , maka akan dihitung dari kanan atau belakang
print('Karakter ke - 3 di dalam nama',namaLengkap,"adalah",namaLengkap[-3])
# jika karakter yang diinginkan dalam bentuk range dari 0 sampai 2
print('Karakter ke 0 - 3 di dalam nama',namaLengkap,"adalah",namaLengkap[0:3])
# mengambil karakter dengan indeks yang memiliki jeda tertentu
print('Karakter ke 0 , 2 , 4 , 8 , 6 , 10 dalam nama',namaLengkap,"adalah",namaLengkap[0:10:2])

# mencari item paling kecil 
print('Karakter paling kecil di',namaLengkap,"adalah",min(namaLengkap))

# mencari karakter paling besar
print('Karakter paling besar di',namaLengkap,'adalah',max(namaLengkap))

# mencari karakter ASCII
data = "p"
print("Code ASCII dari karakter",data,"adalah",ord(data))
code = 112
print("Karakter dari kode ASCII",code,"adalah",chr(code))


# 4. operator dalam bentuk method

# mencari data menggunakan method count()
siswa = 'Naura ramadani'
print('Jumlah karakter a di dalam string',siswa,"adalah",siswa.count('a'))