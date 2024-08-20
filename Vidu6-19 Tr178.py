import csv
def DocNoiDungFile_CSV_4(filename):
    try:
        with open(filename, 'rt', encoding='utf8') as f:
            csvReaderObj = csv.reader(f)
            lst = csvReaderObj.__next__()
            print('|', lst[0].center(20), '|', lst[1].center(20), '|', lst[2].center(10), '|', lst[3].center(13), '|')
            print('_' * 76)
            for row in csvReaderObj:
                print('|{: <21s}'.format(row[0]), '|', '{: <20s}'.format(row[1]), '| %10s | %13s | ' %(row[2], row[3]))
            print(f'Du lieu gom {csvReaderObj.line_num - 1} dong')
    except FileNotFoundError:
        print('Khong tim thay tap tin %s' %filename)
    else:
        print('Da thuc hien hoan tat ham DocNoiDungFile_CSV_4')
DocNoiDungFile_CSV_4('E:/Documents/Studies/Python/ProgrammingLanguage.csv')