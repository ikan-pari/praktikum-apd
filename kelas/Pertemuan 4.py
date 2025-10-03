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

angka = [2, 5, 8, 12, 15, 7, 20]
print("Mencari angka pertama yang lebih besar dari 10...")
for n in angka:
    print(f"Sekarang memeriksa angka: {n}")
    if n > 10:
        print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
        break
print("Program selesai.")