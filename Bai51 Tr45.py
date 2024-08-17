# s = str(input('Nhap chuoi: '))
# s = 'Python 3.9.1'
s = '227 nguyen van cu p.1 q.5'

print('Cau a:')
sochudem = {}
for char in s:
    if char in sochudem:
        sochudem[char] += 1
    else:
        sochudem[char] = 1
result = [char for char, count in sochudem.items() if count == 1]
print('Ky tu chi xuat hien 1 lan: ', result)

print('Cau b:')
# for char in s:
#     if char in sochudem:
#         sochudem[char] += 1
#     else:
#         sochudem[char] = 1
for k, v in sochudem.items():
    if v == 1:
        print('Ky tu dau tien chi xuat hien 1 lan: ', k)
        break

print('Cau c:')