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

print(f'''So to 500 la {namtram} to
So to 200 la {haitram} to
So to 100 la {mottram} to
So to 50 la {namchuc} to
So to 20 la {haichuc} to
So to 10 la {muoi} to
So to 5 la {nam} to
So to 2 la {hai} to
So to 1 la {mot} to
Tong so to la: {tong}''')
