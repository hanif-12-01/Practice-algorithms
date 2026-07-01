daftar_wilayah=[]
jumlah_wilayah=int(input("Masukkan jumlah wilayah: "))
for i in range (1, jumlah_wilayah+1):
    nama_wilayah=input("Masukkan nama wilayah: ")
    kemacetan=float(input("Masukkan persentase kemacetan(%): "))
    sampah=float(input("Masukkan persentase sampah(%): "))

    if kemacetan>=80 or sampah>=85:
        prioritas="prioritas tinggi"
    else:
        prioritas="prioritas rendah"
    daftar_wilayah.append((nama_wilayah,kemacetan,sampah,prioritas))

print("===ringkasan data wilayah===")
for wilayah in daftar_wilayah:
    print(f"Wilayah: {wilayah[0]}, Kemacetan: {wilayah[1]}%, Sampah: {wilayah[2]}%,prioritas:{wilayah[3]}%")
