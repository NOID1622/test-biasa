def prima(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def prima_terdekat(x):
    while x > 2:
        x -= 1
        if prima(x):
            return x
    return 2

n = int(input("Masukkan suatu angka: "))
b_prima = prima_terdekat(n)

print("Bilangan prima terdekat < ", n, " adalah ", b_prima)