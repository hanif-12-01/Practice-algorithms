angka=int(input("Masukkan angka: "))
def genap (n):
    if n % 2 == 0:
        print(f"{n} adalah bilangan genap")
    else:
        print(f"{n} adalah bilangan ganjil")
    

genap(angka)