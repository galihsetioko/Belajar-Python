# Nama : Galih Setioko
# Instagram.com/galihstyoko

''' 
Syntax pass dalam konteks perulangan tidak dieksekusi oleh komputer

sedangkan perintah continue akan membuat program melompat atau melewati syntax selanjutnya

'''

num = 1
while num < 7:
    if num == 5:
        print('Perulangan angka 5 akan dilewati..')
        num += 1
        continue
    print(f"Ini adalah perulangan yang ke-{num}")
    num += 1