import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear()
print("""
=======================================================
|     Selamat Datang di Aplikasi Manajemen Mainan     |
|         LEGO & Action Figure Collection App         |
=======================================================
""")

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "fachri": {"password": "123", "role": "pengguna"}
}

mainan = {
    1: {"nama": "LEGO Star Wars Millennium Falcon", "jenis": "LEGO", "harga": "Rp1500000", "kondisi": "Baru"},
    2: {"nama": "Iron Man Mark 85", "jenis": "Action Figure", "harga": "Rp350000", "kondisi": "Bekas"}
}

while True:
    print("Silakan Registrasi!")
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()
    role = input("Masukkan role (admin/pengguna): ").strip().lower()

    if role not in ["admin", "pengguna"]:
        print("Role harus 'admin' atau 'pengguna'.\n")
        continue

    if username in users:
        print("Username sudah terdaftar.\n")
        continue
    else:
        users[username] = {"password": password, "role": role}
        print("Registrasi berhasil!\n")
        break

clear()
login = 0
while login < 3:
    print("=============== LOGIN ===============")
    username_in = input("Masukkan Username : ").strip()
    password_in = input("Masukkan Password : ").strip()

    if username_in in users and users[username_in]["password"] == password_in:
        role_in = users[username_in]["role"]
        clear()
        print(f"Selamat datang, {username_in} sebagai {role_in}!\n")

        while True:
            print("""
[           === MENU PENGELOLAAN MAINAN ===            ]
[1] Tambah Mainan
[2] Lihat Koleksi
[3] Ubah Mainan
[4] Hapus Mainan
[5] Lihat User (Admin Saja)
[6] Logout
""")
            menu = input("Pilih menu: ").strip()
            clear()

            if menu == "1":
                nama = input("Nama Mainan: ")
                jenis = input("Jenis (LEGO/Action Figure): ")
                harga = "Rp" + input("Harga (tanpa Rp): ")
                kondisi = input("Kondisi (Baru/Bekas): ")
                mainan[len(mainan) + 1] = {"nama": nama, "jenis": jenis, "harga": harga, "kondisi": kondisi}
                print("Data berhasil ditambahkan!\n")

            elif menu == "2":
                print("\n=== Koleksi Mainan ===")
                for i, data in mainan.items():
                    print(f"{i}. {data['nama']} | {data['jenis']} | {data['harga']} | {data['kondisi']}")
                print("")

            elif menu == "3":
                nama_lama = input("Masukkan nama mainan yang ingin diubah: ")
                ditemukan = False
                for i, data in mainan.items():
                    if data["nama"].lower() == nama_lama.lower():
                        ditemukan = True
                        mainan[i]["nama"] = input("Nama baru: ")
                        mainan[i]["jenis"] = input("Jenis baru: ")
                        mainan[i]["harga"] = "Rp" + input("Harga baru (tanpa Rp): ")
                        mainan[i]["kondisi"] = input("Kondisi baru: ")
                        print("Data mainan berhasil diubah!\n")
                        break
                if not ditemukan:
                    print("Mainan tidak ditemukan!\n")

            elif menu == "4":
                nama_hapus = input("Masukkan nama mainan yang ingin dihapus: ")
                hapus = False
                for i, data in list(mainan.items()):
                    if data["nama"].lower() == nama_hapus.lower():
                        del mainan[i]
                        hapus = True
                        print("Data berhasil dihapus!\n")
                        break
                if not hapus:
                    print("Mainan tidak ditemukan!\n")

            elif menu == "5":
                if role_in == "admin":
                    print("\n=== DAFTAR USER TERDAFTAR ===")
                    for i, (user, info) in enumerate(users.items(), 1):
                        print(f"{i}. Username: {user} | Role: {info['role']}")
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
        clear()

else:
    print("\nAnda gagal login 3 kali.")
    print("Terima kasih telah menggunakan Aplikasi Manajemen Mainan!\n")