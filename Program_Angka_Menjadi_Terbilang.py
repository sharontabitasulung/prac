#Sharon Tabita Sulung
#PYTN-KS10-017

#Program Angka menjadi Terbilang
def Terbilang(bil):
    angka = ("","Satu","Dua","Tiga","Empat","Lima","Enam","Tujuh","Delapan",
             "Sembilan","Sepuluh","Sebelas")

    hasil = ""
    n = int (bil)
    if n >= 0 and n <= 11 :
        hasil = angka[n]
    elif n < 20:
        hasil= Terbilang(n-10)+'belas'
    elif n < 100:
        hasil= Terbilang(n/10)+'puluh'+Terbilang(n%10)
    else:
        hasil = "Angka hanya sampai 99"
    return hasil

a = 1
while a != 0:
    a = input("\nMasukkan Angka (antara 0 - 99) : ")
    huruf = Terbilang(a)
    print('Terbilang : '+huruf)
    continue
    


