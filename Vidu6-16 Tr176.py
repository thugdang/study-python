import csv
def DocNoiDungFile_CSV_1(filename):
    try:
        with open(filename,'rt') as f:
            csvReaderObj = csv.reader(f, delimiter=',')
            print(list(csvReaderObj))
    except FileNotFoundError:
        print('Khong tim thay tap tin %s' %filename)
    else:
        print('Da thuc hien hoan tat ham DocNoiDungFile_CSV_1')
DocNoiDungFile_CSV_1('E:/Documents/Studies/Python/ProgrammingLanguage.csv')