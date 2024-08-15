print("Cau a:")
n = int(input('Nhap n: '))
i = 1
while i <= n:
    print(i)
    i += 1

print('Cau b:')
i = n
while i > 0:
    if i % 5 == 0:
        print(i)
    i -= 1

print('Cau c:')
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print(sum)

print('Cau d:')
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1

print('Cau e:')
i = 1
sum = 0
while i <= n:
    if n % i == 0:
        print(i)
        sum += i
    i += 1
print(f'Tong cac uoc so: {sum}')

print('Cau f:')
i = n - 1
while i > 0:
    if n % i == 0 and i % 2 == 0:
        print(f'Uoc gan voi n nhat va la so chan la: {i}')
    i -= 1
