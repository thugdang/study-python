def nhapn():
    n = int(input('Nhap n: '))
    return n

def uocso(n):
    sum = 0
    # print(f'Cac uoc so cua {n} la: ', end='')
    # for i in range(1, n + 1, 1):
    #     if n % i == 0:
    #        print(i, end=' ')
    #        sum += i
    # print(f'\nTong cac uoc so cua {n} la: {sum}')
    ds = []
    for i in range(1, n + 1, 1):
        if n % i == 0:
            ds.append(i)
            sum += i
    return print(f'Cac uoc so cua {n} la: {ds}\nTong cac uoc so cua {n} la: {sum}')

n = nhapn()
uocso(n)