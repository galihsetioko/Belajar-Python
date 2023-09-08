# Galih Setioko
# Instagram : https://instagram.com/galihstyoko
# Menggunakan function untuk menjalankan tiap operasi matematika

import os

def screen():
    print("".center(50, '-'))
    print("CALCULATOR APP".center(50))
    print("".center(50, '-'))

def tambah(value1:float, value2:float) -> float:
    return value1 + value2
def kurang(value1:float, value2:float) -> float:
    return value1 - value2
def perkalian(value1:float, value2:float) -> float:
    return value1 * value2
def pembagian(value1:float, value2:float) -> float:
    return value1 / value2

def main():
    while True:
        os.system('cls')
        screen()
        angka1 = float(input("Masukkan angka 1 : "))
        angka2 = float(input("Masukkan angka 2 : "))
        operasi = input("Masukkan operasi matematika + / * - : ")
        if operasi == '+':
            print(f'Hasil nya adalah : {tambah(angka1, angka2)}')
        elif operasi == '-':
            print(f'Hasil nya adalah : {kurang(angka1, angka2)}')
        elif operasi == '*':
            # perkalian(angka1, angka2)
            print(f'Hasil nya adalah : {perkalian(angka1, angka2)}')
        elif operasi == '/':
            # pembagian(angka1, angka2)
            print(f'Hasil nya adalah : {pembagian(angka1, angka2)}')
        else:
            print("Operasi tidak diketahui")
        
        answer = input("Apakah anda ingin berhitung kembali ? (y/n)")
        if answer == 'n':
            break
        
main()