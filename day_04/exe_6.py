def hitung_skor(kemacetan,sanpah,lampu_mati):
    skor=(kemacetan*0.5)+(sanpah*0.3)+(lampu_mati*0.2)
    return skor

def tentukan_prioritas(skor):
    if skor >= 80 and skor <= 100:
        return "Prioritas Tinggi"
    elif skor >= 60 and skor < 80:
        return "Prioritas Sedang"
    else:
        return "Prioritas Rendah"

def tampilkan_hasil(wilayah, kemacetan, sampah, lampu_mati, skor, prioritas):
    print("\n=== HASIL ANALISIS SMARTFLOW ===")
    print("Wilayah    :", wilayah)
    print("Kemacetan  :", kemacetan, "%")
    print("Sampah     :", sampah, "%")
    print("Lampu Mati :", lampu_mati, "titik")
    print("Skor       :", skor)
    print("Prioritas  :", prioritas)

wilayah = input("Masukkan nama wilayah: ")
kemacetan = float(input("Masukkan persentase kemacetan (%): "))
sampah = float(input("Masukkan persentase sampah (%): "))
lampu_mati = int(input("Masukkan jumlah lampu mati: "))
skor = hitung_skor(kemacetan, sampah, lampu_mati)
prioritas = tentukan_prioritas(skor)
tampilkan_hasil(wilayah, kemacetan, sampah, lampu_mati, skor, prioritas)