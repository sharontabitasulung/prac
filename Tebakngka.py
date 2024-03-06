import random
angka_komputer = random.randint(0,10)
percobaan = 3
print("=" * 24)
print("||Permainan Tebak Angka||")
print("=" * 24)
while True:
    angka_kita = int(input("Masukkan angka tebakan:  "))
    if angka_kita != angka_komputer:
        percobaan -= 1 
        print('Tebakanmu terlalu','kecil' 
        if angka_kita < angka_komputer else 'besar')
    else:
        print(f"Jawaban benar, Anda menang pada percobaan ke-{percobaan}")
        break
    if percobaan == 0:
        print("Anda Kalah,Game Over!")
        break
