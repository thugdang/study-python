a, b = map(int, input('Nhap a, b cach nhau boi khoang trang: ').split(' '))

if a == 0 and b == 0:
    print('Pt vo so nghiem')
elif a == 0 and b != 0:
    print('Pt vo nghiem')
else:
    print(f'Nghiem x: {-b / a}')
