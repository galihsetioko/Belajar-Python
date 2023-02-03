# Nama : Galih Setioko
# Instagram : instagram.com/galihstyoko

''' 
Di python tidak ada array melainkan hanya ada list

'''

# kumpulan data numbers
data_angka = [1,2,3]
print(data_angka)

# kumpulan data string
data_string = ['toni', 'risma', 'naura']
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True]
print(data_boolean)

# Kumpulan data campuran
data_campuran = [1, 'galih', True, False]
print(data_campuran)

# Cara alternatif membuat range
data_range = range(0, 5) #range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list menggunakan for loop comprehensive
list_for = [i**2 for i in range(0, 10)]
print(list_for)

# membuat list menggunakan for if
list_if = [i for i in range(0, 10) if (i % 2 != 0)]
print(list_if)
