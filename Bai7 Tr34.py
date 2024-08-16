import random
import math

# a
def nhapn():
    while True:
        try:
            n = eval(input('Nhap n 50 - 100: '))
        except Exception:
            print('Gia tri khong phai kieu so. Vui long nhap lai!')
        else:
            if type(n) is not int:
                print('Khong phai so nguyen. Vui long nhap lai!')
            elif n < 50 or n > 100:
                print('So khong nam trong 50 - 100. Vui long nhap lai!')
            else:
                return n

# b
def tao_list_random(n):
    l = []
    for i in range(n):
        l.append(random.randint(0, 2*n))
    return l

# c
def checksnt(k):
    if k < 2:
        return False
    i = 2
    while i * i <= k:
        if k % i == 0:
            return False
        i += 1
    return True

def lstsnt(l):
    l_snt = []
    for i in l:
        if checksnt(i):
            l_snt.append(i)
    return l_snt

# d
def checkcp(k):
    if math.sqrt(k).is_integer():
        return True
    else:
        return False

def lstcp(l):
    l_cp = []
    for i in l:
        if checkcp(i):
            l_cp.append(i)
    return l_cp

# e
def checklp(k):
    for i in str(k):
        if i not in '68':
            return False
    return True

def lstlp(l):
    l_lp = []
    for i in l:
        if checklp(i):
            l_lp.append(i)
    return l_lp

# f
def xoasnt(l):
    l_nosnt = []
    for i in l:
        if checksnt(i) == False:
            l_nosnt.append(i)
    return l_nosnt

# g
def xoacp(l):
    l_nocp = []
    for i in l:
        if checkcp(i) == False:
            l_nocp.append(i)
    return l_nocp

n = nhapn()
l = tao_list_random(n)
print(l)
l_snt = lstsnt(l)
print(l_snt)
l_cp = lstcp(l)
print(l_cp)
l_lp = lstlp(l)
print(l_lp)
l_nosnt = xoasnt(l)
print(l_nosnt)
l_nocp = xoacp(l)
print(l_nocp)