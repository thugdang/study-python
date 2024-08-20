import csv
def DocNoiDungFile_CSV_3(filename):
    try:
        with open(filename, encoding='utf8') as f:
            csvReaderObj = csv.reader(f)
            fieldList = csvReaderObj.__next__()
            for row in csvReaderObj:
                print(row)
            print('Tong cong co %d dong' %(csvReaderObj.line_num - 1))
            print('Ten cac cot lan luot la: ', end='')
            print(', '.join(field for field in fieldList))
    except FileNotFoundError:
        print('Khong tim thay tap tin %s' %filename)
    else:
        print('Da thuc hien hoan tat ham DocNoiDungFile_CSV_3')
DocNoiDungFile_CSV_3('E:/Documents/Studies/Python/ProgrammingLanguage.csv')