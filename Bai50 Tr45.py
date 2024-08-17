# s = str(input('Nhap chuoi: '))
# s = 'Python 3.9.1'
s = '227 nguyen van cu p.1 q.5'

print('Cau a:')
d = {'kyso':0, 'kytu':0, 'khac':0}
for i in s:
    if i.isdigit():
        d['kyso'] += 1
    elif i.isalpha():
        d['kytu'] += 1
    else:
        d['khac'] += 1
print(f'Co {d['kyso']} ky so; {d['kytu']} ky tu; {d['khac']} ky tu khac')

print('Cau b:')
tong = 0
for i in s:
    if i.isdigit():
        tong += int(i)
print('Tong ky so: ', tong)