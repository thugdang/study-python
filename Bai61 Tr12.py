n = int(input('Nhap so nguyen n: '))
s = 0

print('Cach 1:')
for i in range(1, n+1):
    for j in range(1, i+1):
        s += j
print(s)

print('Cach 2:')
k = sum(i for x in range(1, n+1) for i in range(1, x+1))
print(k)
