import random

def nhapn():
    n = int(input('Nhap n: '))
    return n

def caua(n):
    if n > 0:
        ds = []
        for i in range(1, n, 1):
            if i % 3 == 0:
                ds.append(i)
        if not ds:
            return print(f'Khong co so nao chia het cho 3 va nho hon {n}')
        else:
            return print(f'Cac so chia het cho 3 va nho hon {n}: {ds}')

def caub(n):
    if 0 <= n <= 9:
        match n:
            case 1:
                return print('Mot')
            case 2:
                return print('Hai')
            case 3:
                return print('Ba')
            case 4:
                return print('Bon')
            case 5:
                return print('Nam')
            case 6:
                return print('Sau')
            case 7:
                return print('Bay')
            case 8:
                return print('Tam')
            case 9:
                return print('Chin')
        return print(f'{n} khong nam trong khoang tu 0 den 9')

def cauc(n):
    if n < 10 or n > 50:
        print(f'In ra {n} so ngau nhien: ', end='')
        for i in range(1, n+1, 1):
            print(round(random.random(), 2), end=' ')
            i+=1
        print('')
    else:
        print('Khong dung dieu kien')

def bangcuuchuong(n):
    print(f'''{n} x 1 = {n * 1}
{n} x 2 = {n * 2}
{n} x 3 = {n * 3}
{n} x 4 = {n * 4}
{n} x 5 = {n * 5}
{n} x 6 = {n * 6}
{n} x 7 = {n * 7}
{n} x 8 = {n * 8}
{n} x 9 = {n * 9}
{n} x 10 = {n * 10}''')

def caud(n):
    if n % 5 == 0:
        print(f'Vi {n} la boi so cua 5:')
        bangcuuchuong(5)
    else:
        print(f'{n} khong phai la boi so cua 5')

def caue(n):
    if n == 2 or n == 4 or n == 6 or n == 8 or n == 10:
        a, d = map(int, input('Nhap a, d: ').split(' '))
        ds = []
        ds.append(a)
        for i in range(1, n+1):
            a += d
            ds.append(a)
        return print(ds)
    else:
        return print('Khong thoa man dieu kien')

def dieukien():
    n = nhapn()
    print('Cau a:')
    caua(n)
    print('Cau b:')
    caub(n)
    print('Cau c:')
    cauc(n)
    print('Cau d:')
    caud(n)
    print('Cau e:')
    caue(n)

dieukien()