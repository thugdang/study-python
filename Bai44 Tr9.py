n = int(input('Nhap n: '))
for i in range (2, n + 1):
    dem = 0
    for j in range (2, i + 1):
        if i % j == 0:
            dem += 1
    if dem <= 2:
        print(j, end=' ')
