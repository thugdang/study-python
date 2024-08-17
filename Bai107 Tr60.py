# a
lst1 = [2**i for i in range(0,9)]
print('lst1 = ', lst1)

# b
lst2 = [i * (i + 1) for i in range(0,10)]
print('lst2 = ', lst2)

# c
lst3 = [chr(i) for i in range(97,123)] # cach 1
print('lst3 = ', lst3)
lst3 = [chr(i) for i in range(ord('a'),ord('z') + 1)] # cach 2
print('lst3 = ', lst3)

# d
def fibonacci(n):
    lst4 = [0, 1]
    [lst4.append(lst4[-1] + lst4[-2]) for _ in range(n - 2)]
    return lst4
n = int(input('Nhap n: '))
lst4 = fibonacci(n)
print('lst4 = ', lst4)

# e
start = int(input('Nhap Start: '))
stop = int(input('Nhap Stop: '))
step = int(input('Nhap Step: '))
lst5 = [i for i in range(start, stop, step if (start < stop) else -step)]
print('lst5 = ', lst5)

# f
start = int(input('Nhap Start: '))
stop = int(input('Nhap Stop: '))
step = int(input('Nhap Step: '))
import math
f = int(math.log(stop/start, step))
lst6 = [start * step**i for i in range(0, f + 1)]
print('lst6 = ', lst6)