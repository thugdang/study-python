a, b, c = map(int, input('Nhap so a, b, c cach nhau boi khoang trang: ').split(' '))

# Cach 1
max = max(a, b, c)
min = min(a, b, c)
mid = a + b + c - max - min
cong1 = min + min
cong2 = cong1 + cong1
if cong1 == mid and cong2 == max:
    print(f'Day la cap so cong. So ke tiep la: {max + max}')
else:
    print('Day khong la cap so cong')
nhan1 = min * min
nhan2 = nhan1 * nhan1
if nhan1 == mid and nhan2 == max:
    print(f'Day la cap so nhan. So ke tiep la: {max * max}')
else:
    print('Day khong la cap so nhan')

# Cach 2
if (c - b == b - a):
    print("Day la cap so cong. So tiep theo la:", c + c - b)
else:
    print ("Day khong la cap so cong")
if (c / b == b / a):
    print("Day la cap so nhan. So tiep theo la:", c * c / b)
else:
    print ("Day khong la cap so nhan")
