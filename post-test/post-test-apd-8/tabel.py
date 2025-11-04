from prettytable import PrettyTable

def tampilkan_tabel(data_dict):
    if not data_dict:
        print("Belum ada data mainan.\n")
        return

    table = PrettyTable()
    table.field_names = ["No", "Nama", "Jenis", "Harga (Rp)", "Kondisi"]
    for i, data in data_dict.items():
        table.add_row([i, data["nama"], data["jenis"], f"{data['harga']:,}", data["kondisi"]])
    print(table)
    print()