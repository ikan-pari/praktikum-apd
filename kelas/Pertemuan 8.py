# pilihan = input('apakah anda ingin lanjut? (ya/tidak)' ).lower()

# if pilihan == 'ya':
#     print("terimakasih telah menggunakan program ini")
# elif pilihan == 'tidak':
#     print("lanjutkan program")
# else:
#     print("inputnya salah kocak")

# import math as fr
# print(fr.sqrt(16))
# print(fr.factorial(4))

import random
#print(random.randint(1, 5)) # menghasilkan angka random dari 1 - 4

#pilih_acak = ["pisang", "rambutan", "manggis"]
# acak = "apcb"
#print(random.choice(pilih_acak)) # memilih 1 element secara acak pada list
# print(random.choice(acak)) # memilih 1 karakter acak pada string
# memasukkan satu persatu nilai dari kumpulan_angka
# ke dalam variabel hasil dengan isinya 4 karakter hasil randomize
# kumpulan_angka = "1234567890"
# hasil = ""
# for i in range(4):
#     hasil += random.choice(kumpulan_angka)
# print(hasil)

acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
random.shuffle(acak_kartu) # kocok kartu, output berupa urutan list yang
# berubah
print(acak_kartu)