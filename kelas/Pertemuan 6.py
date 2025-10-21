#buah ={"mangga", "apel", "jeruk", "apel"}
#print(buah)

#angka_ganjil = {1,3,5,7,9}
#for angka in angka_ganjil:
#    print(angka)
#print("menambahkan angka 11 ke dalam set")
#angka_ganjil.add(11)
#for angka in angka_ganjil:
#    print(angka)

#Daftar_buku = {
#"Buku1" : "Bumi Manusia",
#"Buku2" : "Laut Bercerita"
#}
#print(Daftar_buku["Buku1"])
#print(Daftar_buku)

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {
#     "Instagram" : "daffahrhap"
# }
# print(Biodata)

# list_mahasiswa = dict(nama="Dapupu", Jurusan="Informatika")

# Nilai = {
# "Matematika": 80,
# "B. Indonesia": 90,
# "B. Inggris": 81,
# "Kimia": 78,
# "Fisika": 80
# }
# # Tanpa menggunakan items()
# for i in Nilai:
#     print(i)
# print("") # pemisah
# # Menggunakan items()
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})
# print("") 
# #Setelah Ditambah
# print("setelah ditambah")
# print(Film)

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# del data["Nama"]
# #Setelah diubah
# print(data)
# #memanggil data yang telah dihapus
# print(data.get("Nama"))

key = "apel", "jeruk", "mangga"
value = 1
buah = dict.fromkeys(key, value)
print(buah)
