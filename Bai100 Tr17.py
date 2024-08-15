def cach1(n):
    tong = 0
    tich = 1
    max = 0
    chan = 0
    le = 0
    while n > 0:
        a = n % 10
        n //= 10
        if a > max:
            max = a
        if a % 2 == 0:
            chan += 1
        else:
            le += 1
        tong += a
        tich *= a
    return tong, tich, max, chan, le

def cach2(n):
    m = str(n)
    tong = 0
    tich = 1
    max = 0
    chan = 0
    le = 0
    for i in m:
        if max < int(i):
            max = int(i)
        if int(i) % 2 == 0:
            chan += 1
        else:
            le += 1
        tong += int(i)
        tich *= int(i)
    return tong, tich, max, chan, le

n = int(input('Nhap n: '))
tong, tich, max, chan, le = cach1(n)
print(f'Cach 1: Tong = {tong}; Tich = {tich}; Max = {max}; Chan = {chan}; Le = {le}')
tong, tich, max, chan, le = cach2(n)
print(f'Cach 2: Tong = {tong}; Tich = {tich}; Max = {max}; Chan = {chan}; Le = {le}')