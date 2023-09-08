import os

# mambuat dan menulis data ke dalam file
TEMPLATE = """

1. Create Data
2. Read Data
3. Update Data
4. Delete Data

"""
# 1
#DATAS = []

def createData():
    print('\n')
    PENULIS = input('Masukkan nama penulis : ')
    JUDUL = input("Masukkan judul buku : ")
    TAHUN_TERBIT = input("Masukkan tahun terbit : ")
    DATAS = {"nama":PENULIS,"judul":JUDUL,"tahun":TAHUN_TERBIT}
    with open('data.txt', 'w+') as file:
        thumbnail = list(file.read())
        print(thumbnail)
        thumbnail.append(DATAS)
        print(thumbnail)
        file.write(str(thumbnail))

def readData():
    with open('data.txt', 'r') as file:
        data_read = file.read()
        for index , data in enumerate(data_read):
            print(f"Index ke - {index} adalah {data}")
        

while True:
    os.system('cls')
    print('\n')
    print(f"{''.center(60, '=')}")
    print(f"{'PROGRAM PERPUSTAKAAN'.center(60)}")
    print(f"{''.center(60, '=')}")
    print(TEMPLATE)
    choice = input("Masukkan Pilihan : ")
    if choice == '1':
        createData()
    elif choice == '2':
        readData()
    elif choice == '3':
        updateData()
    elif choice == '4':
        deleteData()
    else:
        print('\n[-] Masukkan data dengan benar.')
    
    answer = input("\n[?] Selesaikan Program ? (y/n)  ")
    if answer == 'y' or answer == "Y" or answer == 'yes':
        break


