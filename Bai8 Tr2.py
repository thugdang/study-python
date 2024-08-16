a, b, c = map(int, input('Nhap 3 so cach nhau boi dau cach: ').split(' '))
print('So tu be den lon: ', min(a, b, c), a + b + c -max(a, b, c) - min(a, b, c), max(a, b, c))
