Wilayah=[]
for i in range (5):
    nama_wilayah=input("Masukkan nama wilayah: ")
    kemacetan=float(input("Masukkan persentase kemacetan(%): "))
    sampah=float(input("Masukkan persentase sampah(%): "))

    if kemacetan>=80 or sampah>=85:
        print("pritoritas tinggi")
    else:
        print("pritoritas rendah")
    Wilayah.append((nama_wilayah,kemacetan,sampah))
    

