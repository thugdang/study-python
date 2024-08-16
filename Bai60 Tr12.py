n = int(input('Nhap n: '))
print('S = 1 +', end=' ')
tong = 1

print('Cach 1:')
for i in range (2, n + 1):
    m = str(f'{i}/({i}*({i}+1))')
    print(m, end=' ')
    tong += eval(m)
    if i != n:
        print('+', end=' ')
    else:
        print('=', tong)

print('Cach 2:')
k = sum((i/i*(i+1)) for i in range(1, n+1))
print('Tong: ', k)
