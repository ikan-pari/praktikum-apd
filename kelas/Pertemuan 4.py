#for i in range (1,10):
#   print(f'Perulangan ke {i}')

#    mahasiswa = ['Andi', 'Budi', 'Caca', 10,  'Dodi']

#   for i in mahasiswa:
#        print(i)

#for i in range(1, 10):
#    for j in range(1, i+1):
#        print("ini akmal", end=" dan ")
#    print("ini doni")

#jawab = 'hooh'
#hitung = 0
#while(jawab == 'hooh'):
#    hitung += 1
#print(f"Total perulangan: {hitung}")

#angka = [2, 5, 8, 12, 15, 7, 20]
#print("Mencari angka pertama yang lebih besar dari 10...")
#for n in angka:
#    print(f"Sekarang memeriksa angka: {n}")
#    if n > 10:
#        print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
#        break
#print("Program selesai.")

for i in range(1, 11):
#    if i % 2 != 0:
#        continue
#    print(f"Angka genap ditemukan: {i}")
#    
#print("\nProgram selesai.")


while True:    
    print("Menu")
    print("1. Option 1")
    print("2. Option 2")
    opsi = int(input("Pilih opsi (1 atau 2): "))
    if opsi == 1:
        print("Anda memilih Option 1")
    elif opsi == 2:
        print("Anda memilih Option 2")
    elif opsi == 3:
        break
    else:
        print("Opsi tidak valid, silakan coba lagi.")