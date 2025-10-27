# # def menu ():
# #     print('=== MENU UTAMA ===')
# #     print('[1] Tambah Data')
# #     print('[2] Hapus Data')
# #     print('[3] Lihat Data')
# #     print('[4] Keluar')
# #     pilihan = input('Pilih menu: ')
# #     return pilihan


# # def tambah_data():


# # def luas_persegi_panjang(p, l):
# #     luas = p * l 
# #     print("luas persegi panjang adalah:", luas)

# # luas_persegi_panjang(10, 5)

# def luas_persegi(s):
#     luas = s * s

# print("luas persegi adalah:", luas(8))

# nama = "Daffa"

# def salam():
#     nama = "Pernanda"
#     print("Halo, " + nama)

# print(nama)
# salam()

# def tambah(a, b):
#     return a + b

# tambahlagi = tambah(3, 4)
# print(tambahlagi)

# tambahlagi += 10
# print(tambahlagi)

# def l_persegi(s):
#     s = s * s

# print(l_persegi(4))

# def l_persegi(s):
#     s = s * s
#     return s
# print(l_persegi(4))

# def l_persegi():
#     sisi = 4
#     luas = sisi * sisi
#     return luas

# print(l_persegi())

# angka = int(input('Masukkan Angka : '))
# print(angka) 

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else:
#     print("angka yang anda masukkan adalah :", angka)

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else :
#     print(f'Angka yang kamu input : {angka}')
# finally :
#     print('Blok Try Selesai')

try:
    usn = input('Username yang diinginkan : ')
    if len(usn) < 5:
        raise ValueError('Nama Minimal Memiliki 5 karakter')
except ValueError as e:
    print(e)