nama = input("Masukkan Nama Lengkap: ")
nim = int(input("Masukkan NIM: "))
harga = int(input("Masukkan Harga Menu Makanan (Rp): "))

pajak_pecel = harga * (5/100)
total_pecel = harga + pajak_pecel

pajak_mie = harga * (8/100)
total_mie = harga + pajak_mie

pajak_padang = harga * (10/100)
total_padang = harga + pajak_padang

print("\n Hasil Perhitungan Pajak ")
print(f"{nama} dengan NIM {nim} ingin membeli makanan seharga Rp {int(harga)}")
print(f"Jika membeli Pecel Lele, maka harus membayar Rp {int(total_pecel)} setelah mendapat pajak 5%.")
print(f"Jika membeli Mie Ayam, maka harus membayar Rp {int(total_mie)} setelah mendapat pajak 8%.")
print(f"Jika membeli Nasi Padang, maka harus membayar Rp {int(total_padang)} setelah mendapat pajak 10%.")

#tabel output
print("\n===========================================")
print("Nama :", nama)
print("NIM  :", nim)
print("Harga Makanan (Rp):", harga)
print("===========================================")
print("| Menu         \t| Harga (Rp) \t| Total Bayar (Rp) |")
print("-------------------------------------------")
print("| Pecel Lele   \t|", int(harga), "\t\t|", int(total_pecel), "\t|")
print("| Mie Ayam     \t|", int(harga), "\t\t|", int(total_mie), "\t|")
print("| Nasi Padang  \t|", int(harga), "\t\t|", int(total_padang), "\t|")
print("===========================================")