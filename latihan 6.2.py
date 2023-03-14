def dinamis(n):
    for i in range(n, 0, -1):
        gas = 1
        for x in range(i, 0, -1):
            gas *= x
        print(gas, end=" ")
        for y in range(i, 0, -1):
            print(y, end=" ")
        print()

n = int(input("Masukkan nilai n: "))
dinamis(n)