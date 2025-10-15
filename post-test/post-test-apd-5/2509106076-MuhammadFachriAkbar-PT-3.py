print("""
=======================================================
|     Selamat Datang di Aplikasi Manajemen Mainan     |
|         LEGO & Action Figure Collection App         |
=======================================================
""")

users = [["admin", "admin123", "admin"], ["fachri", "123", "pengguna"]]
mainan = [
    ["LEGO Star Wars Millennium Falcon", "LEGO", "Rp1500000", "Baru"],
    ["Iron Man Mark 85", "Action Figure", "Rp350000", "Bekas"]
]

while True:
    print("Silakan Registrasi!")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    role = input("Masukkan role (admin/pengguna): ")

    if role not in ["admin", "pengguna"]:
        print("Role harus 'admin' atau 'pengguna'.")
        continue

    duplikat = False
    for u in users:
        if u[0] == username:
            print("Username sudah terdaftar.")
            duplikat = True
            break

    if not duplikat:
        users.append([username, password, role])
        print("Registrasi berhasil!\n")
        break

login = 0
while login < 3:
    print("=============== LOGIN ===============")
    username_in = input("Masukkan Username : ")
    password_in = input("Masukkan Password : ")

    masuk = False
    for u in users:
        if username_in == u[0] and password_in == u[1]:
            role_in = u[2]
            masuk = True
            print(f"\nSelamat datang, {username_in} sebagai {role_in}!\n")
            break

    if masuk:
        while True:
            print("""
[           ===MENU PENGELOLAAN MAINAN===            ]
[1] Tambah Mainan
[2] Lihat Koleksi
[3] Ubah Mainan
[4] Hapus Mainan
[5] Lihat User (Admin Saja)
[6] Logout
""")
            menu = input("Pilih menu: ")

            if menu == "1":
                nama = input("Nama Mainan: ")
                jenis = input("Jenis (LEGO/Action Figure): ")
                harga = "Rp" + input("Harga (tanpa Rp): ")
                kondisi = input("Kondisi (Baru/Bekas): ")
                mainan.append([nama, jenis, harga, kondisi])
                print("Data berhasil ditambahkan!\n")

            elif menu == "2":
                print("\n=== Koleksi Mainan ===")
                for i in range(len(mainan)):
                    print(f"{i+1}. {mainan[i][0]} | {mainan[i][1]} | {mainan[i][2]} | {mainan[i][3]}")
                print("")

            elif menu == "3":
                nama_lama = input("Masukkan nama mainan yang ingin diubah: ")
                ada = False
                for i in range(len(mainan)):
                    if nama_lama == mainan[i][0]:
                        ada = True
                        mainan[i][0] = input("Nama baru: ")
                        mainan[i][1] = input("Jenis baru: ")
                        mainan[i][2] = "Rp." + input("Harga baru (tanpa Rp): ")
                        mainan[i][3] = input("Kondisi baru: ")
                        print("Data mainan berhasil diubah!\n")
                        break
                if not ada:
                    print("Mainan tidak ditemukan!\n")

            elif menu == "4":
                nama_hapus = input("Masukkan nama mainan yang ingin dihapus: ")
                hapus = False
                for i in range(len(mainan)):
                    if nama_hapus == mainan[i][0]:
                        del mainan[i]
                        hapus = True
                        print("Data berhasil dihapus!\n")
                        break
                if not hapus:
                    print("Mainan tidak ditemukan!\n")

            elif menu == "5":
                if role_in == "admin":
                    print("\n=== DAFTAR USER TERDAFTAR ===")
                    for i in range(len(users)):
                        print(f"{i+1}. Username: {users[i][0]} | Role: {users[i][2]}")
                    print("")
                else:
                    print("Hanya admin yang bisa melihat data user.\n")

            elif menu == "6":
                print("Terima kasih telah menggunakan Aplikasi Manajemen Mainan!\n")
                break

            else:
                print("Pilihan tidak valid.\n")

        break

    else:
        print("Login gagal. Username atau password salah.\n")
        login += 1

else:
    print("\nAnda gagal login 3 kali.")
    print("Terima kasih telah menggunakan Aplikasi Manajemen Mainan!\n")