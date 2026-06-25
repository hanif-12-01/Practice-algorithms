total=[]
for i in range (5):
    nilai=int(input("Masukkan nilai: "))
    total.append(nilai)
for i in total:
    print("Nilai yang dimasukkan:", i)
    print ("rata-rata nilai:", sum(total)/len(total)) 