while True:
    a = int(input('Nhap so thu 1: '))
    b = int(input('Nhap so thu 2: '))
    pt = input('Nhap phep tinh (+, -, *, /, ^, %, <<, >>): ')
    match pt:
        case '+':
            print(f'{a} + {b} = {a + b}')
        case '-':
            print(f'{a} - {b} = {a - b}')
        case '*':
            print(f'{a} * {b} = {a * b}')
        case '/':
            print(f'{a} / {b} = {a / b}')
        case '^':
            print(f'{a} ^ {b} = {a ^ b}')
        case '%':
            print(f'{a} % {b} = {a % b}')
        case '<<':
            print(f'{a} << {b} = {a << b}')
        case '>>':
            print(f'{a} >> {b} = {a >> b}')
        case _:
            print('Chua nhap dung phep tinh!')
    tieptuc = input('Tiep tuc? (y/n): ')
    if tieptuc.lower() in ('no', 'n'):
        break
