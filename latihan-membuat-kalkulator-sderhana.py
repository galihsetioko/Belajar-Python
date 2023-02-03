# Nama : Galih Setyoko
# Instagram : instagram.com/galihstyoko

# Membuat aplikasi kalkulator sederhana

# 1. Meminta input angka user
print('\n')
print("CALCULATOR".center(30, '='))
angka1 = float(input("Masukkan angka 1 : "))
operasi = input("Masukkan operasi (+ / - *) : ")
angka2 = float(input("Masukkan angka 2 : "))

if (operasi == '+'):
    hasil = angka1 + angka2
    print("Hasilnya adalah :",hasil)
elif (operasi == '-'):
    hasil = angka1 - angka2
    print("Hasilnya adalah :",hasil)
elif (operasi == '/'):
    hasil = angka1 / angka2
    print("Hasilnya adalah :",hasil)
elif (operasi == '*'):
    hasil = angka1 * angka2
    print("Hasilnya adalah :",hasil)
else :
    print("Tidak bisa menjalankan program...")