import csv
def DocNoiDungFile_CSV(filename):
    try:
        with open(filename, 'rt', encoding='utf8') as f:
            csvReaderObj = csv.reader(f)
            print('Danh sach cac thi sinh dau (Tong diem >= 20):')
            lst = csvReaderObj.__next__()
            lst.append('Tong')
            lst1 = list(csvReaderObj)
            print('|', lst[0].center(3), '|', lst[1].center(20), '|', lst[2].center(7), '|', lst[3].center(7), '|', lst[4].center(7), '|', lst[5].center(7), '|', lst[6].center(7), '|')
            print('_' * 81)
            for row in lst1:
                tong = float(row[2]) + float(row[3]) + float(row[4]) + float(row[5])
                if tong >= 20:
                    print('|{: <4s}'.format(row[0]), '|', '{: <20s}'.format(row[1]), '| %7s | %7s | %7s | %8s | %7s |' %(row[2], row[3], row[4], row[5], tong))
            print('Danh sach cac thi sinh rot (Tong diem < 20):')
            print('|', lst[0].center(3), '|', lst[1].center(20), '|', lst[2].center(7), '|', lst[3].center(7), '|', lst[4].center(7), '|', lst[5].center(7), '|', lst[6].center(7), '|')
            print('_' * 81)
            for row in lst1:
                tong = float(row[2]) + float(row[3]) + float(row[4]) + float(row[5])
                if tong < 20:
                    print('|{: <4s}'.format(row[0]), '|', '{: <20s}'.format(row[1]), '| %7s | %7s | %7s | %8s | %7s |' %(row[2], row[3], row[4], row[5], tong))
    except FileNotFoundError:
        print('Khong tim thay tap tin %s' %filename)
    else:
        print('Da thuc hien hoan tat')

def GhiNoiDungFileCSV(filename, listcontent):
    try:
        with open(filename, 'a', newline='') as f:
            f.write('\n')
            f.write(listcontent)
    except FileNotFoundError:
        print('Khong tim thay tap tin %s' %filename)
    else:
        print('Da ghi noi dung hoan tat')

def NhapThongTin():
    while True:
        try:
            stt = int(input('Nhap STT: '))
            hoten = str(input('Nhap ho ten: '))
            mon1 = float(input('Nhap diem mon 1: '))
            mon2 = float(input('Nhap diem mon 2: '))
            mon3 = float(input('Nhap diem mon 3: '))
            uutien = float(input('Nhap diem uu tien: '))
            data = (f'{stt}, {hoten}, {mon1}, {mon2}, {mon3}, {uutien}')
            return data
        except Exception as e:
            print('Input khong hop le! Nhap lai!')

def GhiCSVDauRot(filegoc, filedau, filerot):
    with open(filegoc, 'rt', encoding='utf8') as f:
        csvReaderObj = csv.reader(f)
        header = next(csvReaderObj)
        lst = list(csvReaderObj)
        dau = f'{header[0]}, {header[1]}, {header[2]}, {header[3]}, {header[4]}, {header[5]}\n'
        rot = f'{header[0]}, {header[1]}, {header[2]}, {header[3]}, {header[4]}, {header[5]}\n'
        for row in lst:
            tong = float(row[2]) + float(row[3]) + float(row[4]) + float(row[5])
            if tong >= 20:
                dau += f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}\n'
            else:
                rot += f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}\n'
        with open(filedau, 'w', newline='') as d:
            d.write(dau)
            print('Da ghi noi dung vao file: dau.csv')
        with open(filerot, 'w', newline='') as r:
            r.write(rot)
            print('Da ghi noi dung vao file: rot.csv')

while True:
    user_input = str(input('Nhap thong tin thi sinh moi? (yes/no): '))
    if user_input.lower() in ['yes', 'y']:
        data = NhapThongTin()
        GhiNoiDungFileCSV('D:/thuc.dangdong/My Documents/Studies/Python/danhsach.csv', data)
    elif user_input.lower() in ['no', 'n']:
        break
    else:
        print('Input khong hop le!')
DocNoiDungFile_CSV('D:/thuc.dangdong/My Documents/Studies/Python/danhsach.csv')
GhiCSVDauRot('D:/thuc.dangdong/My Documents/Studies/Python/danhsach.csv', 'D:/thuc.dangdong/My Documents/Studies/Python/dau.csv', 'D:/thuc.dangdong/My Documents/Studies/Python/rot.csv')