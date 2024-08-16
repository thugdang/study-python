def nhapn():
    n = int(input('Nhap n: '))
    if n <= 1:
        print("Nhap sai! Nhap lai!")
        nhapn()
    else:
        return n

def fibonacci1a(n):
    f = [0, 1]
    for i in range(1,n+1):
        if i == f[-1] + f[-2]:
            f.append(i)
    return f

def fibonacci2a(n):
    f = [0, 1]
    for i in range(1, n-1):
        j = f[-1] + f[-2]
        f.append(j)
    return f

def fibonacci1b(n):
    nhat = 0
    nhi = 1
    print(f'{nhat} {nhi} ', end='')
    i = 1
    while nhat + nhi <= n:
        ba = nhat + nhi
        print(ba, end=' ')
        nhat = nhi
        nhi = ba
        i += 1

def fibonacci2b(n):
    nhat = 0
    nhi = 1
    print(f'{nhat} {nhi} ', end='')
    for i in range(n-2):
        ba = nhat + nhi
        print(ba, end=' ')
        nhat = nhi
        nhi = ba

n = nhapn()
print(fibonacci1a(n))
print(fibonacci2a(n))
print(fibonacci1b(n))
print(fibonacci2b(n))
