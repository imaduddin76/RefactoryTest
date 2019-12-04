def reverse(kalimat):
    kata = ""
    panjang = len(kalimat) - 1
    while panjang >= 0:
        kata = kata + kalimat[panjang]
        panjang -= 1
    return kata

input_kalimat = input("Masukkan Kalimat : ")
print(reverse(input_kalimat))