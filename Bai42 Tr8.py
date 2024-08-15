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

def locphat(n):
    # m = n % 10
    # if m == 6 or m == 8:
    #     locphat(n // 10)
    # else:
    #     return False
    # return True
    while n > 0:
        so = n % 10
        n //= 10
        if so != 6 and so != 8:
            return False
        return True

def tinhtongbinhphuong(p):
    tongbinhphuong = 0
    while p > 0:
        so = p % 10
        p = p // 10
        tongbinhphuong = so**2
    return tongbinhphuong

def somayman(k):
    for i in range(100):
        tong = tinhtongbinhphuong(k)
        if tong == 1

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
# if locphat(n) == True:
#     print(f'{n} la so loc phat')
# else:
#     print(f'{n} khong phai la so loc phat')
print('So loc phat: ', end='')
for i in range(1,n+1):
    if locphat(i) == True:
        print(i, end=' ')
print('')
