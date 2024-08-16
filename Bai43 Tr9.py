import math

n = int(input('Nhap n: '))

print('Cach 1:')
dem = 0
for i in range (2, n + 1):
    if n % i == 0:
        dem += 1
if dem > 2:
    print(f'{n} khong phai so nguyen to')
else:
    print(f'{n} la so nguyen to')

print('Cach 2:')
if n < 1:
    print(f'{n} khong phai so nguyen to')
else:
    LaSoNguyenTo = True
    for i in range (2, n):
        if (n % i == 0):
            LaSoNguyenTo = False
            break
    if LaSoNguyenTo == True:
        print(f'{n} la so nguyen to')
    else:
        print(f'{n} khong phai so nguyen to')
