from Gempa import Gempa

# Membuat daftar gempa
gempas = [
    Gempa("Banten", 1.2),
    Gempa("Palu", 6.1),
    Gempa("Cianjur", 5.6),
    Gempa("Jayapura", 3.3),
    Gempa("Garut", 4.0),
]

# Info gempa
print("## Gempa Bumi Info ##\n")

for gempa in gempas:
    print(f"Lokasi: {gempa.lokasi}")
    print(f"Skala: {gempa.skala}")
    print("Dampak: ", end="")
    gempa.dampak()
    print()  # Pemisah antar gempa
