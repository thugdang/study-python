n = int(input('Nhap n: '))
print('S = 1 +', end=' ')
tong = 1

print('Cach 1:')
for i in range (2, n + 1):
    m = str(f'1/{i}')
    print(m, end=' ')
    tong += eval(m)
    if i != n:
        print('+', end=' ')
    else:
        print('=', tong)

print('Cach 2:')
k = sum(1/i for i in range(1, n+1))
print('Tong: ', k)
