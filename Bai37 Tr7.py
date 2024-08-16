n = int(input('Nhap n: '))
tong = 0
tich = 1
while n > 1:
    a = n % 10
    print(a, n)
    tong += a
    tich *= a
    n //= 10
    print(a, n)
print('Tong: ', tong)
print('Tich: ', tich)
