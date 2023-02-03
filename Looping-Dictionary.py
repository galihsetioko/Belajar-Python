# Galih Setioko
# Instagram.com/galihstyoko

teman = {
    'man':"maman suherman",
    'tia':"Tia arumi",
    'Ita':"Ita mariska",
    'Lua':"Lukman saputra",
}

# mengambil keys dictionary menggunakan keys()
for i in teman.keys():
    print(f"Keys nya adalah : {i}")

# mengambil values menggunakan values()
for i in teman.values():
    print(f'Values dari item nya adalah : {i}')

# mengambil full item menggunakan items()
for i in teman.items():
    print(f"Items nya adalah : {i}")

# mengambil key dan values nya
for key, data in teman.items():
    print(f"Key nya adalah : {key} & Values nya adalah : {data}")