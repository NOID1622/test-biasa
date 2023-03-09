#input 
batasBawah = int(input("masukkan batas bawah : "))
batasAtas = int(input ("masukkan batas atas  : "))

#proses
if batasBawah > batasAtas :
    for i in range (batasBawah+1, batasAtas, - 1): 
        if i % 2 == 1:
            if i == batasAtas or i == batasAtas + 1:
                print(i)
            else :
                print(i, end=", ")
else : 
    for i in range(batasBawah, batasAtas + 1):
        if i % 2 == 1:
            if i == batasAtas or i == batasAtas - 1:
                print(i)
            else:
                print(i, end=", ")   