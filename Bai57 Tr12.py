n = int(input('Nhap n: '))
print('S =', end=' ')
tong = 0
print('Cach 1:')
for i in range (1, n + 1):
    print(i, end=' ')
    tong += i
    if i != n:
        print('+', end=' ')
    else:
        print('=', tong)

print('Cach 2:')
k = sum(i for i in range(1, n + 1))
print('Tong: ', k)
