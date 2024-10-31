print('\n====== no 2 ======')
jumlah = 0  # untuk menampung hasil jumlah
string = " "  # untuk menampung nilai jumlah dalam bentuk string
bilangan = 1

while bilangan <= 19:  # melakukan perulangan sebanyak <=19
    jumlah += bilangan
    string += str(bilangan)

    if bilangan < 19:  # Menambahkan tanda '+' hanya sampai bilangan sebelum 19
        string += " + "  # Menambahkan spasi di sekitar '+'

    bilangan += 2  # Menambah bilangan dengan 2 untuk mendapatkan bilangan ganjil berikutnya

print(f"{string} = {jumlah}")
