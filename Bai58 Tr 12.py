n = int(input('Nhap n: '))
print('S = 1 +', end=' ')
tong = 1

print('Cach 1:')
for i in range (1, n + 1):
    m = str(f'(2*{i} + 1)')
    print(m, end=' ')
    tong += eval(m)
    if i != n:
        print('+', end=' ')
    else:
        print('=', tong)

print('Cach 2:')
k = sum(i for i in range(1, 2*n+2) if i % 2 != 0)
print('Tong: ', k)
