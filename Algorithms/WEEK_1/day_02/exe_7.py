wilayah=input("Masukkan nama wilayah: ")
kemacetan=int(input("Masukkan angka kemacetan: "))
sampah=int(input("Masukkan jumlah sampah: "))
lampu_mati=input("Apakah lampu mati? (ya/tidak): ")

print("Prioritas penanganan untuk wilayah", wilayah)

if kemacetan >= 80 and sampah >= 85:
    print("Prioritas sangat tinggi")
elif kemacetan >= 80 or sampah >= 85:
    print("Prioritas tinggi")
elif lampu_mati == "ya":
    print("Prioritas sedang")
else:
    print("Prioritas rendah")