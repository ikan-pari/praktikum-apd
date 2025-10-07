print("===== SELAMAT DATANG DI BIOSKOP XX0 =====")

nama_pengguna = "Muhammad Fachri Akbar"
nim_pengguna = "2509106076"
percobaan = 0
login_berhasil = False
pilihan = 0
jenis_tiket = ""
harga_tiket = 0
jumlah_tiket = 0
total_bayar = 0
potongan = 0
bonus = ""
total_akhir = total_bayar - potongan

while percobaan < 3 and login_berhasil == False:
    print("\n=== LOGIN ===")
    nama_input = input("Masukkan Nama Pengguna: ")
    nim_input = input("Masukkan NIM: ")

    if nama_input == nama_pengguna and nim_input == nim_pengguna:
        print("\nLogin Berhasil! Selamat datang", nama_pengguna)
        login_berhasil = True
    else:
        percobaan += 1
        print("Login Gagal! Percobaan ke-", percobaan)

if login_berhasil == False:
    print("\nLogin ditolak. Anda telah gagal login sebanyak 3 kali.")
else:
    while pilihan != 4:
        print("\n=== MENU PEMBELIAN TIKET BIOSKOP XX0 ===")
        print("1. Tiket Reguler  - Rp 50.000")
        print("2. Tiket VIP      - Rp 100.000")
        print("3. Tiket VVIP     - Rp 150.000")
        print("4. Keluar")

        pilihan = int(input("Pilih jenis tiket (1-4): "))

        if pilihan == 1 or pilihan == 2 or pilihan == 3:
            if pilihan == 1:
                jenis_tiket = "Reguler"
                harga_tiket = 50000
            elif pilihan == 2:
                jenis_tiket = "VIP"
                harga_tiket = 100000
            elif pilihan == 3:
                jenis_tiket = "VVIP"
                harga_tiket = 150000

            jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
            total_bayar = harga_tiket * jumlah_tiket
            potongan = total_bayar * 0.12 if total_bayar >= 300000 else total_bayar * 0.08 if total_bayar >= 200000 else 0
            bonus = "Poster Film Eksklusif" if total_bayar >= 150000 and total_bayar < 200000 else ""
            total_akhir = total_bayar - potongan

            print("\n===== STRUK PEMBELIAN =====")
            print("Nama Pembeli   :", nama_pengguna)
            print("Jenis Tiket    :", jenis_tiket)
            print("Jumlah Tiket   :", jumlah_tiket)
            print("Total Bayar    : Rp", total_bayar)

            if potongan > 0:
                print("Potongan Harga : Rp", int(potongan))
                print("Total Akhir    : Rp", int(total_akhir))
            elif bonus != "":
                print("Bonus          :", bonus)
            else:
                print("Tidak ada potongan atau bonus.")
            print("=============================")

        elif pilihan == 4:
            print("\nTerima kasih telah menggunakan layanan Bioskop XX0!")
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
