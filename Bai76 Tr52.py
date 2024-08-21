def nhapset():
    myset = set()
    while True:
        n = int(input('Nhap phan tu vao set, nhap -1 de dung: '))
        if n == -1:
            break
        else:
            myset.add(n)
    return myset

print('Cau a:')
myset1 = nhapset()
myset2 = nhapset()
print('Cau b:')
print('Set 1: ', myset1)
print('Set 2: ', myset2)
dem1 = 0
dem2 = 0
tong1 = sum(myset1)
tong2 = sum(myset2)
for i in myset1:
    dem1 += 1
for i in myset2:
    dem2 += 1
print('Cau c:')
print(f'So phan tu set 1: {dem1} phan tu')
print(f'So phan tu set 2: {dem2} phan tu')
print(f'Tong phan tu set 1: {tong1}')
print(f'Tong phan tu set 2: {tong2}')
print('Cau d:')
min1 = min(list(myset1))
max1 = max(list(myset1))
min2 = min(list(myset2))
max2 = max(list(myset2))
print(f'Phan tu nho nhat set 1: {min1}')
print(f'Phan tu lon nhat set 1: {max1}')
print(f'Phan tu nho nhat set 2: {min2}')
print(f'Phan tu lon nhat set 2: {max2}')
print('Cau e:')
print(myset1 | myset2)
print('Cau f:')
print(myset1 & myset2)
print('Cau g:')
print(myset1 - myset2)
print('Cau h:')
print(myset1 ^ myset2)
print('Cau i:')
print(sorted(myset1))
print(sorted(myset2))