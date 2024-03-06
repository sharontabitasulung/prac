import random
angka_komputer = random.randint(0,10)
percobaan = 3
while True:
    angka_kita = int(input(f"Masukkan angka dari 0 sampai 9:  "))
    if angka_kita != angka_komputer:
        percobaan -= 1  
        if angka_kita < angka_komputer:
            print("Tebakan terlalu kecil")
        if angka_kita > angka_komputer:
            print("Tebakan terlalu besar")
    else:
        print(f"Jawaban benar, anda menang pada percobaan yang ke-{percobaan}")
        break
    if percobaan == 0:
        print("Anda kalah, Game Over!")
        break