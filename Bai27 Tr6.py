n = int(input('Nhap n: '))

print("Cau a:")
print('In ra cac so tu 1 den n:')
i = 1
while i <= n:
    print(i, end=' ')
    i += 1

print('\nCau b:')
print(f'Cac so nho hon {n} va la boi so cua 5:')
i = n
while i > 0:
    if i % 5 == 0:
        print(i, end=' ')
    i -= 1

print('\nCau c:')
print(f'Tong cac so tu 1 den {n}: ', end=' ')
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print(sum)

print('Cau d:')
print(f'Tong cac so chan nho hon {n}: ', end=' ')
i = 1
sum = 0
while i < n:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)

print('Cau e:')
print(f'Cac uoc so chan cua {n}:')
i = 1
sum = 0
while i <= n:
    if n % i == 0 and i % 2 == 0:
        print(i, end=' ')
        sum += i
    i += 1
print(f'\nTong cac uoc so: {sum}')

print('Cau f:')
i = n - 1
if i % 2 == 0:
    print(f'So chan gan voi {n} nhat la: {i}')
else:
    print(f'So chan gan voi {n} nhat la: {i - 1}')

print('Cau g:')
print(f'Uoc so le lon nhat cua {n} va nho hon {n}: ', end=' ')
i = n - 1
while i > 0:
    if n % i == 0 and i % 2 != 0:
        print(i)
        break
    else:
        i -= 1