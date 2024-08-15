# lst = [1, -1, 2, 0, 5, 8, -13, 21, -34, 55, 87, 0]
import random

sl = 10
lst = []
for i in range(sl):
    lst.append(random.randint(-100, 100))

print('Cau a:')
print(lst)

print('Cau b:')
for j in lst:
    if j <= 5:
        print(j, end=' ')
print('')

print('Cau c:')
lst2 = []
for j in lst:
    if j <= 5:
        lst2.append(j)
print(lst2)

print('Cau d:')
m = int(input('Nhap vao m: '))
for n in lst:
    if n % m == 0:
        print(n, end=' ')
print('')

print('Cau e:')
so_duong = 0
so_0 = 0
so_am = 0
for l in lst:
    if l > 0:
        so_duong += 1
    elif l == 0:
        so_0 += 1
    else:
        so_am += 1
print('Ty le so duong: {:.2f}%'.format(so_duong * 100 / sl))
print('Ty le so 0: {:.2f}%'.format(so_0 * 100 / sl))
print('Ty le so am: {:.2f}%'.format(so_am * 100 / sl))