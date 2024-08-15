datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}, {3.14, 9, "python"}]

print('Cau A:')
for item in datalist:
    if type(item) == int: print(f'Data type of {item} is int.')
    elif type(item) == float: print(f'Data type of {item} is float.')
    elif type(item) == complex: print(f'Data type of {item} is complex.')
    elif type(item) == bool: print(f'Data type of {item} is boolean.')
    elif type(item) == str: print(f'Data type of {item} is string.')
    elif type(item) == list: print(f'Data type of {item} is list.')
    elif type(item) == tuple: print(f'Data type of {item} is tuple.')
    elif type(item) == set: print(f'Data type of {item} is set.')
    elif type(item) == dict: print(f'Data type of {item} is dictionary.')
    else: print(f'Data type of {item} is unknown.')

print('Cau B:')
for item in datalist:
    if isinstance(item, int): print(f'Data type of {item} is int.')
    elif isinstance(item, float):  print(f'Data type of {item} is float.')
    elif isinstance(item, complex):  print(f'Data type of {item} is complex.')
    elif isinstance(item, bool):  print(f'Data type of {item} is boolean.')
    elif isinstance(item, str):  print(f'Data type of {item} is str.')
    elif isinstance(item, list):  print(f'Data type of {item} is list.')
    elif isinstance(item, tuple):  print(f'Data type of {item} is tuple.')
    elif isinstance(item, set):  print(f'Data type of {item} is set.')
    elif isinstance(item, dict):  print(f'Data type of {item} is dictionary.')
    else: print(f'Data type of {item} is unknown.')