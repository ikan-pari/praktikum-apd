print("===== SELAMAT DATANG DI BIOSKOP XX0 =====")

nama_pengguna = "Muhammad Fachri Akbar"
nim_pengguna = "2509106076"
percobaan = 0
login_sukses = False

while percobaan < 3 and login_sukses == False:
    print("\n=== LOGIN ===")
    nama_input = input("Masukkan Nama Pengguna: ")
    nim_input = input("Masukkan NIM: ")
    if nama_input == nama_pengguna and nim_input == nim_pengguna:
        print("\nLogin Berhasil! Selamat datang", nama_pengguna)
        login_sukses = True
    else:
        percobaan += 1
        print("Login Gagal! Percobaan ke-", percobaan)

if login_sukses == False:
    print("\nLogin ditolak. Anda telah gagal login sebanyak 3 kali.")
else:
    pilihan = 0
    while pilihan != 4:
        print("\n=== MENU PEMBELIAN TIKET BIOSKOP XX0 ===")
        print("1. Tiket Reguler  - Rp 50.000")
        print("2. Tiket VIP      - Rp 100.000")
        print("3. Tiket VVIP     - Rp 150.000")
        print("4. Keluar")

        pilihan = int(input("Pilih jenis tiket (1-4): "))

        if pilihan == 1:
            jenis_tiket = "Reguler"
            harga_tiket = 50000
        elif pilihan == 2:
            jenis_tiket = "VIP"
            harga_tiket = 100000
        elif pilihan == 3:
            jenis_tiket = "VVIP"
            harga_tiket = 150000
        elif pilihan == 4:
            print("\nTerima kasih telah menggunakan layanan Bioskop XX0!")
            break
        else:
            print("Pilihan tidak valid.")
            continue

        jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))

        total_bayar = 0
        for i in range(jumlah_tiket):
            total_bayar += harga_tiket

        if total_bayar >= 300000:
            potongan = total_bayar * (12/100)
            total_akhir = total_bayar - potongan
            bonus = "-"
        elif total_bayar >= 200000:
            potongan = total_bayar * (8/100)
            total_akhir = total_bayar - potongan
            bonus = "-"
        elif total_bayar >= 150000:
            potongan = 0
            total_akhir = total_bayar
            bonus = "Poster Film Eksklusif"
        else:
            potongan = 0
            total_akhir = total_bayar
            bonus = "-"

        print("\n===== STRUK PEMBELIAN =====")
        print("Nama Pembeli   :", nama_pengguna)
        print("Jenis Tiket    :", jenis_tiket)
        print("Jumlah Tiket   :", jumlah_tiket)
        print("Total Bayar    : Rp", total_bayar)
        print("Potongan Harga : Rp", int(potongan))
        print("Bonus          :", bonus)
        print("Total Akhir    : Rp", int(total_akhir))
        print("=============================")
