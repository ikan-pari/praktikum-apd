nama_terdaftar = "Muhammad Fachri Akbar"
nim_terdaftar = "2509106076"

nama_pengguna = input("Masukkan Nama: ")
nim_pengguna = input("Masukkan NIM: ")

pilihan_paket = input("Masukkan pilihan paket (1/2/3/4): ")
biaya_langganan = 1500000

if nama_pengguna == nama_terdaftar and nim_pengguna == nim_terdaftar:
    print("\nLogin berhasil! Silakan pilih paket langganan:\n")
    print("1. Paket Bronze (Biaya admin 1%) - Akses dasar ke lagu-lagu populer")
    print("2. Paket Silver (Biaya admin 3%) - Akses lagu premium dan playlist kustom")
    print("3. Paket Gold (Biaya admin 5%) - Akses lagu premium, playlist kustom, dan mode offline")
    print("4. Paket Platinum (Biaya admin 7%) - Semua fitur termasuk konten eksklusif artis\n")



    if pilihan_paket == "1":
        total_bayar = biaya_langganan + biaya_langganan * 1/100
        print("\n--- Paket Bronze ---")
        print("Total Bayar: Rp", int(total_bayar))
        print("Keuntungan: Akses dasar ke lagu-lagu populer")

    elif pilihan_paket == "2":
        total_bayar = biaya_langganan + biaya_langganan * 3/100
        print("\n--- Paket Silver ---")
        print("Total Bayar: Rp", int(total_bayar))
        print("Keuntungan: Akses lagu premium dan playlist kustom")

    elif pilihan_paket == "3":
        total_bayar = biaya_langganan + biaya_langganan * 5/100
        print("\n--- Paket Gold ---")
        print("Total Bayar: Rp", int(total_bayar))
        print("Keuntungan: Akses lagu premium, playlist kustom, dan mode offline")

    elif pilihan_paket == "4":
        total_bayar = biaya_langganan + biaya_langganan * 7/100
        print("\n--- Paket Platinum ---")
        print("Total Bayar: Rp", int(total_bayar))
        print("Keuntungan: Semua fitur, playlist kustom, mode offline, konten eksklusif artis")

    else:
        print("Pilihan Invalid.")
else:
    print("\nLogin gagal! Nama atau NIM tidak sesuai.")
