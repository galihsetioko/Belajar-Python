# Nama : Galih Setioko
# Instagram : Intagram.com/galihstyoko

# merubah case character dari suatu string : uppercase , lowercase , capitalize , title
teks = 'Indonesia'
print('Teks :',teks)
# lowercase
print(teks.lower())
# uppercase
print(teks.upper())


# melakuakan pengecekan string menggunakan is Method
salam = 'assalamualaikum'
print("Salam",salam,"Apakah lowercase ?",str(salam.islower())) #menghasillkan boolean
print("Salam",salam,"Apakah uppercase ?",str(salam.isupper())) #menghasillkan boolean

# isalpha() -> Untuk mengecek semuanya huruf
# isalnum() -> Untuk mengecek huruf dan angka
# isdecimal() -> untuk mengecek semua angka
# isspace() -> Untuk mengecek apakah string kosong
# istitle() -> Untuk mengecek semua kata dimulai dengan huruf besar ( Selamat Pagi ) menghasilkan true

judul = "Saya Pergi Ke Rumah"
print("Apakah teks",judul,"sudah title() : ",judul.istitle())

# mengecek karakter menggunakan startswith() endwidth()
coba_with = 'Galih Setioko'
print('Apakah kata',coba_with,'diawali dengan GALIH ? ',coba_with.startswith('Galih'))
print('Apakah kata',coba_with,'diakhiri dengan GALIH ? ',coba_with.endswith('Galih'))

# penggabungan komponen mengunakan split() dan join()
# join() mengubah dari list menjadi string dengan menambahkan karakter di setiap selingannya , ini adalah method dari string 
daftar_list = ['galih', 'febby', 'annaurah']
print("List akan diubah menjadi :",' + '.join(daftar_list))
# split() akan mengubah string menjadi list dengan menggunakan karakter pemisah di dalam string menjadi acuannya
daftar_string = 'nama saya galih'
print("String akan diubah menjadi list :",daftar_string.split())

# alokasi karakter
print("Galih".upper().center(50, '-'))
print("Galiha".upper().rjust(50, '-'))
print("Galihak".upper().ljust(50, '-'))

# menghilangkan karakter tertentu menggunakan strip()
kata = '====ini galih'
print(kata.strip('='))
