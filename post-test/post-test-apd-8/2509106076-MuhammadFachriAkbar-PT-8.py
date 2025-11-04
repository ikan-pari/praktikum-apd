from auth_module import registrasi, login, users, clear
from opsi_mainan import tampilkan_mainan, tambah_mainan, ubah_mainan, hapus_mainan

clear()
print("""
=======================================================
|     Selamat Datang di Aplikasi Manajemen Mainan     |
|         LEGO & Action Figure Collection App         |
=======================================================
""")

registrasi()
user_login = login()

if user_login:
    while True:
        print("\n=== Menu Utama ===")
        print("1. Tampilkan Mainan")
        print("2. Tambah Mainan")
        print("3. Ubah Mainan")
        print("4. Hapus Mainan")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_mainan()
        elif pilihan == "2":
            tambah_mainan()
        elif pilihan == "3":
            ubah_mainan()
        elif pilihan == "4":
            hapus_mainan()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid.")
