
import random
angka_komputer = random.randint(0,10)
percobaan = 3
print("=" * 24)
print("||Permainan Tebak Angka||")
print("=" * 24)
while True:
    angka_kita = int(input("Masukkan angka tebakan:  "))
    if angka_kita == angka_komputer:
        print(f"Jawaban benar, Anda menang pada percobaan ke-{percobaan}")
        percobaan -= 1 
    else:
        if angka_kita < angka_komputer:
            print("Tebakan terlalu kecil")
        if angka_kita > angka_komputer:
            print("Tebakan terlalu besar")
        percobaan -= 1
        if percobaan == 0:
            print("Anda Kalah,Game Over!")
            break