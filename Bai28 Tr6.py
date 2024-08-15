a = int(input('Nhap so bat dau: '))
d = int(input('Nhap so cong sai: '))
n = 0
while n <= 0:
    n = int(input('Nhap cap so cong: '))
    if n <= 0:
        print('Nhap sai! Nhap lai!')

print('Cap so cong:')
i = 1
while i <= n:
    print(a, end=' ')
    a += d
    i += 1

r = a + (n - 1) * d
print(f'\nCap so cong a{n} la: {r}')
