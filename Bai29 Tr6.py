a = int(input('Nhap so bat dau: '))
q = int(input('Nhap so cong boi: '))
n = 0
while n <= 0:
    n = int(input('Nhap cap so nhan: '))
    if n <= 0:
        print('Nhap sai! Nhap lai!')

print('Cap so nhan:')
i = 1
while i <= n:
    print(a, end=' ')
    a *= q
    i += 1

r = a * q**(n - 1)
print(f'\nCap so nhan a{n} la: {r}')