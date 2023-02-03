# Nama : Galih Setioko
# Instagram : instagram.com/galihstyoko

# Membuat gambar segitiga menggunakan looping

num = 0
# model segitiga 1
while num < 10:
    num += 1
    print("*" * num)

num = 10
# model segitiga 2
print('\n'*2)
while num > 0:
    num -= 1
    print("*" * num)

num = 0
# model segitiga 3
print('\n'*2)
while num < 10:
    num += 1
    if num == 10:
        while num > 0:
            num -= 1
            print("*"*num)
    print("*"*num)
    if num == 0:
        break

num = 1
# model segitiga 4
print('\n'*2)
while num < 15:
    num += 1
    print(("*" * num).center(50))
