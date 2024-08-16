S = str(input('Nhap chuoi: '))
word = str(input('Nhap word: '))
hoa = 0
thuong = 0
print('So lan xuat hien co phan biet hoa thuong: ', S.count(word, 0, len(S)))
print('So lan xuat hien khong phan biet hoa thuong: ', S.lower().count(word.lower(), 0, len(S)))
