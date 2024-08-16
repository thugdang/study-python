# a
def nhapn():
    while True:
        try:
            n = eval(input('Nhap n lon hon 0: '))
        except Exception:
            print('Gia tri khong phai kieu so. Vui long nhap lai!')
        else:
            if type(n) is not int:
                print('Khong phai so nguyen lon hon 0. Vui long nhap lai!')
            elif n <= 0:
                print('So nho hon 0. Vui long nhap lai!')
            else:
                return n

# b
import random
def tao_list_random(n):
    l = []
    for i in range(n):
        l.append(random.randint(0, 1000))
    return l

# c
def tao_list_chan(l):
    l_chan = []
    for i in l:
        if i % 10 == 0:
            l_chan.append(i)
            return l_chan
        elif i % 2 == 0:
            l_chan.append(i)
    return l_chan

# ham main
n = nhapn()
l = tao_list_random(n)
print(l)
l_chan = tao_list_chan(l)
print(l_chan)