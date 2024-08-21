color = input('Input comma seperated sequence of words: ').split(',')
sortedcolor = sorted(set(color))
print('Sap xep theo alphabet:')
print(', '.join(sortedcolor))
print('Xoa phan tu dau tien:')
for x in sortedcolor:
    sortedcolor.remove(x)
    break
print(', '.join(sortedcolor))