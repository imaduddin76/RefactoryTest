kalimat = 'kasur ini rusak'
kalimat_dibalik = kalimat[::-1]
if kalimat == kalimat_dibalik:
  print('kalimat:"{}" merupakan palindrome'.format(kalimat))
else:
  print('kalimat:"{}" bukan merupakan palindrome'.format(kalimat))