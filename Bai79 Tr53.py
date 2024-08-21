import random
n = int(input('Nhap n: '))
myset = set()
for i in range(n+1):
    myset.add(random.randint(0, 10))
print('Set: ', myset)
print('Tong: ', sum(myset))