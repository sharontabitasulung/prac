import random

angka_rahasia = random.randint(1, 100)
while True:
  jawaban = int(input('\nMasukkan angka: '))

  if jawaban == angka_rahasia:
    print('Selamat, tebakanmu benar!')
    break # berhenti paksa
  else:
    print(
      'Tebakanmu terlalu',
      'kecil' if jawaban < angka_rahasia else 'besar'
    )