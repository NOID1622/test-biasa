def tampilan_deret(tinggi, lebar):
    gas = 1
    for x in range(tinggi):
        for y in range(lebar):
            print(gas, end=" ")
            gas += 1
        print()

tinggi = int(input("Masukkan tinggi: "))
lebar = int(input("Masukkan lebar: "))
tampilan_deret(tinggi, lebar)