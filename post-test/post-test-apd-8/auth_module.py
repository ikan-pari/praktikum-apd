import os

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "fachri": {"password": "123", "role": "pengguna"}
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def login():
    kesempatan = 0
    while kesempatan < 3:
        u = input("Masukkan Username : ").strip()
        p = input("Masukkan Password : ").strip()
        if u in users and users[u]["password"] == p:
            print(f"\nSelamat datang, {u} sebagai {users[u]['role']}!\n")
            return u
        else:
            print("Login gagal\n")
            kesempatan += 1
    print("Anda gagal login 3 kali.")
    return None
