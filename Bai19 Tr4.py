nang = float(input('Nhap can nang: '))
cao = float(input('Nhap chieu cao: '))

bmi = nang / (cao * cao)
print(f'So BMI: {bmi}')
if bmi < 18.5:
    print('Thieu can')
elif bmi >= 18.5 and bmi < 22.99:
    print('Binh thuong')
elif bmi >= 23 and bmi < 24.99:
    print('Thua can')
elif bmi > 25:
    print('Beo phi')
