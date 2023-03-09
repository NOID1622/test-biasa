#input
jumlah_matkul = int(input("mamsukkan banyak matkul: "))
# listNilai = []
# totalNilai = 0
jumlah_nilai=0
#proses
for i in range (jumlah_matkul):
    nilai = (input(f"masukkan matkul : "))
    # nilai.lower()
    # listNilai.append (nilai)
# for i in range (jumlah_matkul):
    if nilai  == "A" :
        totalNilai = totalNilai + 4
    elif nilai == "B" :
        totalNilai = totalNilai + 3
    elif nilai  == "C" :
        totalNilai = totalNilai + 2
    elif nilai  == "D" :
        totalNilai = totalNilai + 1

print(f"IPS : {(jumlah_nilai/jumlah_matkul):.3}")

