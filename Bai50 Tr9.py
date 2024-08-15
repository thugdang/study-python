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
            mu = 0
            m = n
            while m % i == 0:
                mu += 1
                m /= i
            if mu == 1:
                if chuoi != '':
                    chuoi += f'x {i} '
                else:
                    chuoi += f'{i} '
            else:
                if chuoi != '':
                    chuoi += f'x {i}^{mu} '
                else:
                    chuoi += f'{i}^{mu} '
            n /= i
        # if n == 1: return chuoi
    print(chuoi)

n = nhapn()
# print(str(n) + ' = ' + tsnt(n))
print(str(n) + ' = ', end='')
tsnt(n)