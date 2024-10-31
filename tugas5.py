# Soal 1: Bilangan Genap atau Ganjil
print("===== Soal 1: Bilangan Genap atau Ganjil =====")
bilangan = int(input("Masukkan sebuah bilangan bulat: "))
if bilangan % 2 == 0:
    print("Bilangan tersebut adalah Genap.")
else:
    print("Bilangan tersebut adalah Ganjil.")
print("\n")

# Soal 2: Nilai Ujian
print("===== Soal 2: Nilai Ujian =====")
nilai_ujian = int(input("Masukkan nilai ujian: "))
if nilai_ujian >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")
print("\n")

# Soal 3: Cek Usia dan Status
print("===== Soal 3: Cek Usia dan Status =====")
usia = int(input("Masukkan usia Anda: "))
if usia >= 18:
    print("Dewasa")
elif 13 <= usia <= 17:
    print("Remaja")
else:
    print("Anak-anak")
print("\n")

# Soal 4: Cek Keanggotaan
print("===== Soal 4: Cek Keanggotaan =====")
status_keanggotaan = input("Masukkan status keanggotaan (gold/silver/bronze): ").lower()
if status_keanggotaan == "gold" or status_keanggotaan == "silver":
    print("Selamat! Anda mendapatkan diskon.")
else:
    print("Maaf, tidak ada diskon untuk keanggotaan ini.")
print("\n")

# Soal 5: Pembelian Diskon
print("===== Soal 5: Pembelian Diskon =====")
jumlah_pembelian = float(input("Masukkan jumlah pembelian: "))
total_harga = jumlah_pembelian * 0.9 if jumlah_pembelian > 100 else jumlah_pembelian
if jumlah_pembelian > 100:
    print(f"Anda mendapatkan diskon 10%! Total harga setelah diskon: {total_harga}")
else:
    print(f"Total harga tanpa diskon: {total_harga}")
