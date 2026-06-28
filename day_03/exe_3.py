daftar_nilai=[]   
for i in range (5):
    nilai=int(input("Masukkan nilai: "))
    daftar_nilai.append(nilai)

print("rata -rata:", sum(daftar_nilai)/len(daftar_nilai))

