import csv
def DocNoiDungFile_CSV_2(filename):
    try:
        with open(filename,'rt') as f:
            csvReaderObj = csv.reader(f, delimiter=',')
            for row in csvReaderObj:
                print(row)
            print('Tong cong co %d dong' %csvReaderObj.line_num)
    except FileNotFoundError:
        print('Khong tim thay tap tin %s' %filename)
    else:
        print('Da thuc hien hoan tat ham DocNoiDungFile_CSV_2')
DocNoiDungFile_CSV_2('E:/Documents/Studies/Python/ProgrammingLanguage.csv')