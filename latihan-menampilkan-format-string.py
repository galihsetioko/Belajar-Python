# Nama : Galih Setioko
# instagram : @galihstyoko

print("\n")
# Menambahkan teks ke dalam teks
teks = 'galih'
format_str = f"Hello {teks}"
print(format_str)

# angka
teks = 90
format_str = f"Ini angka anda {teks}"
print(format_str)

#boolean
teks = True
format_str = f"Ini adalah boolean : {teks}"
print(format_str)


# Bilangan ribuan
teks = 200000
format_str = f"Ini adalah bilangan ribuan {teks:,}"
print(format_str)


# bilangan desimal
teks = 2005.54321
format_str = f"Ini adalah bilangan ribuan {teks:.2f}"
print(format_str)

# menampilkan leading zero
# leading zero adalah angka didepan koma
teks = 2005.54321
format_str = f"Ini adalah bilangan ribuan {teks:08.2f}"
print(format_str)
