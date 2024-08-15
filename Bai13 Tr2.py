import datetime

ten = input('Nhap ten: ')
tuoi = int(input('Nhap tuoi: '))

tuoithieu = 100 - tuoi
nam100 = datetime.datetime.now().year + tuoithieu

print(f'Den nam {nam100}, ban {ten} se tron 100 tuoi')
