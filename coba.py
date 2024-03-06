import random
angka_komputer = random.randint(1,10)

percobaan = 4
angka_kita = int(input("Masukkan angka: "))
while percobaan < 4:
    print (percobaan)
    percobaan =- 1
    if angka_kita == angka_komputer:
        print('Selamat, anda menang!')
        print(f'Kamu sudah mencoba {percobaan}')
        continue
    else:
        print('Tebakanmu terlalu','kecil' 
        if angka_kita < angka_komputer else 'besar')
    break
percobaan =-1
print (f"Game Over")




