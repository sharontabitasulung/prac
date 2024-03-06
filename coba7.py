def Terbilang(bil):
    angka = ["","Satu","Dua","Tiga","Empat","Lima","Enam",
             "Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    Hasil = " "
    n = int(bil)
    if n>= 0 and n <= 11:
        Hasil = angka[n]
    elif n <20:
        Hasil = Terbilang (n-10) + " Belas "
    elif n <100:
        Hasil = Terbilang (n/10) + " Puluh " + Terbilang (n%10)
    else:
        Hasil = "Angka hanya sampai 99"

    return Hasil
a=1
while a!= 0:
    a = input('\nMasukkan Angka (antara 0 - 99) : ')
    huruf = Terbilang(a)
    print (' Terbilang ---- '+huruf+ ' Rupiah ----')
    continue
#if __name__ == "__main__":
   # bil = int(input("\nMasukkan Angka (antara 0 - 99) : "))
   # bilangan = Terbilang(bil)
   # print ("Terbilang : ")