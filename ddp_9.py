print('---n/celcius ke fahrenhet---')
def celcius_ke_fahrenheit(celcius):
    print(celcius * 9/5 + 32)
celcius_ke_fahrenheit(0)

print("/n---mencari bilangan genap---")
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

print("/n---keterangan lulus dan tidak lulus---")
# rata rata nilai kelulusan
def skor(nilai):
    if nilai >= 70:
        print("lulus")
    else:
        print('gagal')

skor(70)
skor(40)

print("\n--- Mencetak Bilangan Ganjil ---")

def bil_ganjil(ganjil):
    print(f"Bilangan ganjil dari 1 hingga {ganjil}:")
    for i in range(1, ganjil + 1, 2):  # Iterasi dengan langkah 2
        print(i)

# Memanggil fungsi bil_ganjil
bil_ganjil(20)  # Contoh: Cetak bilangan ganjil dari 1 hingga 10
