n = int(input('Nhap n: '))

print('Cau 1:')
m = n
for i in range(1,m+1):
    print('*\t' * m)
    m-=1

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (i + j) <= n + 1:
#             print('*')
#         else:
#             print(' ')
print('Cau 5:')
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='\t')
    print('')
