print('Cau a:')
s = input('Nhap day so cach nhau boi khoang trang: ')
l = list(map(int, s.split()))
print(l)
print(s)

print('Cau b:')
tong = 0
for item in l:
    tong += item
print('Cach 1: Tong = ', tong)
print('Cach 2: Tong = ', sum(l))

print('Cau c:')
import math
tich = 1
for item in l:
    tich *= item
print('Cach 1: Tich = ', tich)
print('Cach 2: Tich = ', math.prod(l))

print('Cau d:')
nho = l[0]
for item in l:
    if item < nho:
        nho = item
print('Cach 1: Min = ', nho)
print('Cach 1: Min = ', min(l))