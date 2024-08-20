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

# def GhiNoiDungFileCSV(filename, listcontent):
#     with open(filename, 'w', newline='') as csvfile:
#         fieldnames = ['name', 'branch', 'year', 'cgpa']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(listcontent)

def GhiListNoiDungCSV(filename):
    hoten = str(input('Nhap ten: '))
    mon1 = float(input('Nhap diem mon 1: '))
    mon2 = float(input('Nhap diem mon 2: '))
    mon3 = float(input('Nhap diem mon 3: '))
    uutien = float(input('Nhap diem uu tien: '))
    with open(filename, '+wt', newline='') as f:
        csvReaderObj = csv.reader(f)
        lst = list(csvReaderObj)
        hang = 0
        for row in lst:
            hang += 1
        l = [hang, hoten, mon1, mon2, mon3, uutien]
        writer = csv.DictWriter(f)
        writer.writerow(l)

# DocNoiDungFile_CSV('E:/Documents/Studies/Python/danhsach.csv')
data = [
    {'name': 'Nikhil', 'branch': 'COE', 'year': 2, 'cgpa': 9.0},
    {'name': 'Sanchit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1},
    {'name': 'Aditya', 'branch': 'IT', 'year': 2, 'cgpa': 9.3},
    {'name': 'Sagar', 'branch': 'SE', 'year': 1, 'cgpa': 9.5},
    {'name': 'Prateek', 'branch': 'MCE', 'year': 3, 'cgpa': 7.8},
    {'name': 'Sahil', 'branch': 'EP', 'year': 2, 'cgpa': 9.1}
]
GhiListNoiDungCSV('D:/thuc.dangdong/My Documents/Studies/Python/data.csv')
DocNoiDungFile_CSV('D:/thuc.dangdong/My Documents/Studies/Python/data.csv')