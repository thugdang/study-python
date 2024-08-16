def nhapn():
    n = int(input('Nhap n: '))
    if n > 0:
        return n
    else:
        print("Nhap sai! Nhap lai!")
        nhapn()

def tonguocso(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return sum

def sophongphu(n):
    if tonguocso(n) > n:
        return True
    else:
        return False

def sohoanhao(n):
    if tonguocso(n) == n:
        return True
    else:
        return False

def checklocphat(n):
    while n > 0:
        socuoi = n % 10
        if str(socuoi) not in '68':
            return False
        n //= 10
    return True

def lietkelocphat(n):
    print(f'Cac so loc phat < {n}: ')
    for i in range(n):
        if checklocphat(i):
            print(i, end=' ')

def tinhtongbinhphuong(p):
    tongbinhphuong = 0
    while p > 0:
        so = p % 10
        p = p // 10
        tongbinhphuong = so**2
    return tongbinhphuong

# def somayman(k):
#     for i in range(100):
#         tong = tinhtongbinhphuong(k)
#         if tong == 1

n = nhapn()
print('Cau a:')
if sophongphu(n) == True:
    print(f'{n} la so phong phu')
else:
    print(f'{n} khong phai la so phong phu')
print('Cau b:')
if sohoanhao(n) == True:
    print(f'{n} la so hoan hao')
else:
    print(f'{n} khong phai la so hoan hao')
print('Cau c:')
if checklocphat(n) == True:
    print(f'{n} la so loc phat')
else:
    print(f'{n} khong phai la so loc phat')
lietkelocphat(n)