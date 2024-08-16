n = int(input('Nhap n: '))
chan = 0
le = 0
while n > 1:
    a = n % 10
    if a % 2 == 0:
        chan += 1
    else:
        le += 1
    n //= 10
print('So chan: ', chan)
print('So le: ', le)
