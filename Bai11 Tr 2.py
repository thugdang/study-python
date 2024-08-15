import math

r = float(input('Nhap r: '))

# chieu dai canh hinh vuong va duong kinh
d = r * 2
# dien tich hinh vuong
v = d * d

# dien tich hinh tron
t = math.pi * r * r

print(f'Chieu dai hinh vuong va la duong kinh: {round(d, 2)}cm')
print(f'Dien tich hinh vuong: {round(v, 2)}cm\u00b2')
print(f'Dien tich hinh tron: {round(t, 2)}cm\u00b2')
print(f'Dien tich hinh vuong ngoai tiep: {round(v - t, 2)}cm\u00b2')