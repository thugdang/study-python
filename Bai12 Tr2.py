import math

r = float(input('Nhap r: '))

# duong kinh va la duong cheo hinh vuong
d = r * 2
# dien tich hinh tron
t = math.pi * r * r

# cach 1 -- tinh dien tich hinh vuong tu duong cheo -> dien tich
v = (d * d) / 2

# cach 2 -- tinh dien tich hinh vuong tu duong cheo -> canh hinh vuong -> dien tich
# do dai canh hinh vuong
c = d / math.sqrt(2)
# dien tich hinh vuong
v = c ** 2

print(f'Chieu dai duong kinh va la duong cheo hinh vuong: {round(d, 2)}cm')
print(f'Dien tich hinh tron: {round(t, 2)}cm\u00b2')
print(f'Dien tich hinh vuong: {round(v, 2)}cm\u00b2')
print(f'Dien tich hinh tron ngoai tiep: {round(t - v, 2)}cm\u00b2')
