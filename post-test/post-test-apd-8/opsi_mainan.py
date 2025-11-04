from tabel import tampilkan_tabel

mainan = {
    1: {"nama": "LEGO Star Wars Millennium Falcon", "jenis": "LEGO", "harga": 1500000, "kondisi": "Baru"},
    2: {"nama": "Iron Man Mark 85", "jenis": "Action Figure", "harga": 350000, "kondisi": "Bekas"}
}

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

def tampilkan_mainan():
    tampilkan_tabel(mainan)
    if len(mainan) > 0:
        total = hitung_total_rekursif(list(mainan.keys()))
        print(f"Total Harga Semua Mainan: Rp{total:,}\n")

def tambah_mainan():
    print("=== Tambah Mainan ===")
    nama = input("Nama: ")
    jenis = input("Jenis: ")
    harga = input_angka("Harga: ")
    kondisi = input("Kondisi: ")
    mainan[len(mainan) + 1] = {"nama": nama, "jenis": jenis, "harga": harga, "kondisi": kondisi}
    print("Mainan berhasil ditambahkan!\n")

def ubah_mainan():
    tampilkan_tabel(mainan)
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
    tampilkan_tabel(mainan)
    try:
        i = int(input("Masukkan nomor mainan: "))
        if i not in mainan:
            raise Exception("Mainan tidak ditemukan")
        del mainan[i]
        print("Berhasil dihapus!\n")
    except Exception as e:
        print(e, "\n")