total = int(input("Masukkan Total belanja  (Rp): "))

if total > 500000:
    print("Selamat Anda mendapatkan diskon 10%")
elif total > 100000:
    print("Selamat Anda mendapatkan diskon 20%")
else :
    print("Maaf Anda tidak mendapatkan diskon")