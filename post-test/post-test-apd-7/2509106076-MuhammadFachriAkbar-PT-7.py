import os

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "fachri": {"password": "123", "role": "pengguna"}
}

mainan = {
    1: {"nama": "LEGO Star Wars Millennium Falcon", "jenis": "LEGO", "harga": 1500000, "kondisi": "Baru"},
    2: {"nama": "Iron Man Mark 85", "jenis": "Action Figure", "harga": 350000, "kondisi": "Bekas"}
}

user_login = ""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""
=======================================================
|     Selamat Datang di Aplikasi Manajemen Mainan     |
|         LEGO & Action Figure Collection App         |
=======================================================
""")

def hitung_total_rekursif(keys, index=0):
    if index >= len(keys):
        return 0
    return mainan[keys[index]]["harga"] + hitung_total_rekursif(keys, index + 1)

def input_angka(teks):
    while True:
        try:
            return int(input(teks))
        except:
            print("Masukkan angka yang benar!")

def registrasi():
    print("Silakan Registrasi!")
    while True:
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()
        role = input("Masukkan role (admin/pengguna): ").strip().lower()

        if role not in ["admin", "pengguna"]:
            print("Role tidak valid\n")
            continue

        if username in users:
            print("Username sudah terdaftar\n")
            continue

        users[username] = {"password": password, "role": role}
        print("Registrasi berhasil!\n")
        break

def tampilkan_mainan():
    if len(mainan) == 0:
        print("Belum ada data mainan\n")
    else:
        print("\n=== Koleksi Mainan ===")
        for i, data in mainan.items():
            print(f"{i}. {data['nama']} | {data['jenis']} | Rp{data['harga']:,} | {data['kondisi']}")
        print("")

def menu_utama():
    while True:
        print("""
[           === MENU PENGELOLAAN MAINAN ===            ]
[1] Tambah Mainan
[2] Lihat Koleksi
[3] Ubah Mainan
[4] Hapus Mainan
[5] Lihat User (Admin Saja)
[6] Keluar
""")
        pilih = input("Pilih menu: ").strip()
        clear()

        if pilih == "1":
            tambah_mainan()
        elif pilih == "2":
            tampilkan_mainan()
            total = hitung_total_rekursif(list(mainan.keys()))
            print(f"Total Harga Semua Mainan: Rp{total:,}\n")
        elif pilih == "3":
            ubah_mainan()
        elif pilih == "4":
            hapus_mainan()
        elif pilih == "5":
            lihat_user()
        elif pilih == "6":
            print("Terima kasih telah menggunakan Aplikasi Manajemen Mainan!\n")
            input("Tekan Enter untuk keluar...")
            break
        else:
            print("Pilihan tidak valid\n")

def tambah_mainan():
    print("=== Tambah Mainan ===")
    nama = input("Nama: ")
    jenis = input("Jenis: ")
    harga = input_angka("Harga: ")
    kondisi = input("Kondisi: ")

    mainan[len(mainan) + 1] = {"nama": nama, "jenis": jenis, "harga": harga, "kondisi": kondisi}
    print("Mainan berhasil ditambahkan!\n")

def ubah_mainan():
    tampilkan_mainan()
    try:
        i = int(input("Masukkan nomor mainan: "))
        if i not in mainan:
            raise Exception("Mainan tidak ditemukan")
        mainan[i]["nama"] = input("Nama baru: ")
        mainan[i]["jenis"] = input("Jenis baru: ")
        mainan[i]["harga"] = input_angka("Harga baru: ")
        mainan[i]["kondisi"] = input("Kondisi baru: ")
        print("Berhasil diubah!\n")
    except Exception as e:
        print(e, "\n")

def hapus_mainan():
    tampilkan_mainan()
    try:
        i = int(input("Masukkan nomor mainan: "))
        if i not in mainan:
            raise Exception("Mainan tidak ditemukan")
        del mainan[i]
        print("Berhasil dihapus!\n")
    except Exception as e:
        print(e, "\n")

def lihat_user():
    if users[user_login]["role"] != "admin":
        print("Hanya admin yang bisa melihat data user.\n")
        return

    print("=== Daftar User ===")
    for u, d in users.items():
        print(f"Username: {u} | Role: {d['role']}")
    print()

clear()
banner()
registrasi()

kesempatan = 0
while kesempatan < 3:
    u = input("Masukkan Username : ").strip()
    p = input("Masukkan Password : ").strip()

    if u in users and users[u]["password"] == p:
        user_login = u
        clear()
        print(f"Selamat datang, {user_login} sebagai {users[user_login]['role']}!\n")
        menu_utama()
        break
    else:
        print("Login gagal\n")
        kesempatan += 1

if kesempatan == 3:
    print("Anda gagal login 3 kali.")