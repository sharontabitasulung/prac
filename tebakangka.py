import random
angakacak = random.randint(0,9)

tebakan = input('Masukkan Angka: ')
tebakan = int(angakacak)
batas_percobaan = 6

if tebakan == angakacak:
    print("Maka anda menang")
elif tebakan > angakacak:
    print("Angka terlalu besar")
else:
    print("Angka terlalu kecil")

