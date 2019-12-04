list_data = [94,92,96,70,83,87,84,80]
nilai_terkecil = list_data[0]
nilai_terbesar = list_data[0]
nilai_rata_rata = 0
jumlah_nilai = 0
jumlah_elemen = 0

for nilai in list_data:
  jumlah_elemen = jumlah_elemen + 1
  jumlah_nilai = jumlah_nilai + nilai
  if nilai_terbesar < nilai:
    nilai_terbesar = nilai
  if nilai_terkecil > nilai:
    nilai_terkecil = nilai

nilai_rata_rata = jumlah_nilai / jumlah_elemen

print('isi list: ', list_data)
print('nilai terbesar pada list: ',nilai_terbesar)
print('nilai terkecil pada list: ',nilai_terkecil)
print('Jumlah elemen pada list: ',jumlah_elemen)
print('Akumulasi jumlah nilai elemen pada list: ',jumlah_nilai)
print('rata-rata nilai pada list: ',nilai_rata_rata)
