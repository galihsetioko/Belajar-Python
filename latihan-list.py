# Nama : Galih Setioko
# Instagram : instagram.com/galihstyoko

# list kosong
list_buku = []
print(f'PROGRAM BUKU SEDERHANA'.center(50, '='))
print('\n')

while True:
    buku = input("Masukkan judul buku : ")
    penulis = input("Masukkan judul penulis : ")
    list_buku.append([buku, penulis])
    # print(list_buku)
    print('\n')
    for index,buku in enumerate(list_buku):
        print(f'{index+1}. | {buku[0]} | {buku[1]} ')
    answer =  input(f'Apakah anda ingin melanjutkan ? (y/n)')
    if answer == 'n' :
        break
