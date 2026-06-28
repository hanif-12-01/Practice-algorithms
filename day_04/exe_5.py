def rata_rata(total, jumlah):
    return total / jumlah

jumlah_angka= int(input("Berapa jumlah angka yang ingin dimasukkan? "))
total = 0
for i in range(jumlah_angka):
    nilai = int(input("Masukkan nilai: "))
    total += nilai

print(f"Rata-rata dari {jumlah_angka} angka yang dimasukkan adalah: {rata_rata(total,jumlah_angka)}")