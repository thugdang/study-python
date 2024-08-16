n = int(input('Nhap n: '))
j = 1
for i in range (n, (n * 10) + 1, n):
    print(f'{n} x {j} = {i}')
    j += 1
