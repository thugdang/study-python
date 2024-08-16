n = int(input('Nhap so nguyen: '))

print('Cau a')
if n % 2 == 0:
    print(f'{n} la so chan')
else:
    print(f'{n} la so le')

print('Cau b')
if n % 4 == 0:
    print(f'{n} chia chan cho 4')
elif n % 2 == 0:
    print(f'{n} chia chan cho 2')

print('Cau c')
m = int(input('Nhap so chia: '))
if n % m == 0:
    print(f'{n} chia chan cho {m}')
else:
    print(f'{n} khong chia chan cho {m}')
