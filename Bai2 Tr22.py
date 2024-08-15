def nhapn():
    n = int(input('Nhap n: '))
    return n

def sochan(k):
    if k % 2 == 0:
        return True
    else:
        return False

n = nhapn()
if sochan(n) == True:
    print(f'{n} la so chan')
else:
    print(f'{n} la so le')