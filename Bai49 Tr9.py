def nhapn():
    n = int(input('Nhap n: '))
    while n < 2:
        print("Nhap sai! Nhap lai!")
        n = int(input('Nhap n: '))
    return n

def checksnt(n):
    dem = 0
    for i in range(1, n+1):
        if n % i == 0:
            dem += 1
    if dem != 2:
        return False
    else:
        return True

def tsnt(n):
    chuoi = ''
    for i in range(1, 1000):
        if checksnt(i) == True and n % i == 0:
            while n % i == 0:
                if chuoi != '':
                    chuoi += f'x {i} '
                else:
                    chuoi += f'{i} '
                n /= i
        if n == 1: return chuoi

n = nhapn()
print(str(n) + ' = ' + tsnt(n))