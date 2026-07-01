def tambah_angka(a, b):
    return a + b
def kurang_angka(a, b):
    return a - b
def kali_angka(a, b):
    return a * b
def bagi_angka(a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak bisa membagi dengan nol"  
    
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
pilihan = input("Pilih operasi (+, -, *, /): ")

if pilihan == "+" or pilihan == "1":
    hasil = tambah_angka(angka1, angka2)
elif pilihan == "-" or pilihan == "2":
    hasil = kurang_angka(angka1, angka2)
elif pilihan == "*" or pilihan == "3":
    hasil = kali_angka(angka1, angka2)
elif pilihan == "/" or pilihan == "4":
    hasil = bagi_angka(angka1, angka2)
else:
    hasil = "Pilihan operasi tidak valid"

print(f"Hasil: {hasil}")