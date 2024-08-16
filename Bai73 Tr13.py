# s = str(input('Nhap chuoi: '))
s = 'HeLlO PyThoN 1234 !@#'
print('Uppercase: ', s.upper())
print('Lowercase: ', s.lower())
print('Capitalize: ', s.capitalize())
print('Title: ', s.title())
print('Swapcase: ', s.swapcase())
# ch = str(input('Nhap ky tu: '))
ch = 'o'
dem = 0
for i in range(0, len(s)):
    if s[i] == ch:
        dem += 1
print(f'So lan ky tu {ch} xuat hien: ', dem, 'lan')
print(s.count(ch, 0, len(s)))
print('So luong ky tu: ', len(s))
kyso = 0
inhoa = 0
kytuthuong = 0
kytukhac = 0
nguyenam = 0
phuam = 0
dsphuam = 'bcdfghjklmnpqrstvwxyz'
for i in range(0, len(s)):
    if s[i].isnumeric() == True:
        kyso += 1
    if s[i].isupper() == True:
        inhoa += 1
    if s[i].islower() == True:
        kytuthuong += 1
    if s[i].isalnum() == False and s[i] != ' ':
        kytukhac += 1
    if s[i] == 'a' or s[i] == 'i' or s[i] == 'u' or s[i] == 'e' or s[i] == 'o':
        nguyenam += 1
    if s[i] in dsphuam:
        phuam += 1
print('So ky so: ', kyso)
print('So in hoa: ', inhoa)
print('So ky tu thuong: ', kytuthuong)
print('So ky tu khac: ', kytukhac)
print('So nguyen am: ', nguyenam)
print('So phu am: ', phuam)
