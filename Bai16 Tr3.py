x = int(input('Nhap vao so tien: '))

namtram = x // 500
x %= 500
haitram = x // 200
x %= 200
mottram = x // 100
x %= 100
namchuc = x // 50
x %= 50
haichuc = x // 20
x %= 20
muoi = x // 10
x %= 10
nam = x // 5
x %= 5
hai = x // 2
x %= 2
mot = x // 1
x %= 1

tong = namtram + haitram + mottram + namchuc + haichuc + muoi + nam + hai + mot
soloai = 0

if namtram != 0:
    print(f'So to 500 la {namtram} to')
    soloai += 1
if haitram != 0:
    print(f'So to 200 la {haitram} to')
    soloai += 1
if mottram != 0:
    print(f'So to 100 la {mottram} to')
    soloai += 1
if namchuc != 0:
    print(f'So to 50 la {namchuc} to')
    soloai += 1
if haichuc != 0:
    print(f'So to 20 la {haichuc} to')
    soloai += 1
if muoi != 0:
    print(f'So to 10 la {muoi} to')
    soloai += 1
if nam != 0:
    print(f'So to 5 la {nam} to')
    soloai += 1
if hai != 0:
    print(f'So to 2 la {hai} to')
    soloai += 1
if mot != 0:
    print(f'So to 1 la {mot} to')
    soloai += 1
print(f'Tong so to la: {tong}')
print(f'Tong so loai la: {soloai}')
