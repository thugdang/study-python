diem = float(input('Nhap diem: '))
if diem < 0 or diem > 100:
    print('Nhap sai')
else:
    match diem:
        case _ if diem >= 90:
            print('A')
        case _ if diem >= 80 and diem <= 89:
            print('B')
        case _ if diem >= 70 and diem <= 79:
            print('C')
        case _ if diem >= 65 and diem <= 69:
            print('D')
        case _ if diem <= 65:
            print('E')
