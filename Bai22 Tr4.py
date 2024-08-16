import math

a, b, c = map(int, input('Nhap a, b, c cach nhau boi khoang trang: ').split(' '))

delta = b ** 2 - 4 * a * c
if delta < 0:
    print('Pt vo nghiem')
elif delta == 0:
    x = -(b / (2 * a))
    print(f'Pt co nghiem kep: x1 = x2 = {x}')
else:
    print('Pt co 2 nghiem phan biet:')
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'Pt co x1 = {round(x1, 2)} va x2 = {round(x2, 2)}')
