def checkDongNhat1(n):
    socuoi = n % 10
    while n > 0:
        tachso = n % 10
        if tachso != socuoi:
            return False
        n = n // 10
    return True

def checkDongNhat2(n):
    m = str(n)
    for i in range(1, len(m)):
        if m[0] != m[i]:
            return False
    return True

def cau85a(n):
    print(f'Cac so dong nhat < {n}: ', end=' ')
    for i in range(n):
        if checkDongNhat1(i):
            print(i, end=' ')

def cau85b(n):
    print(f'Cac so dong nhat < {n}: ', end=' ')
    for i in range(n):
        if checkDongNhat2(i):
            print(i, end=' ')

n = int(input('Nhap n: '))
cau85a(n)
print('')
cau85b(n)