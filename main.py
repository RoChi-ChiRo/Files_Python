import os


def read_receipts(file):
    _res = {}
    with open(file, 'r', encoding='UTF8') as _f:
        while True:
            _name = _f.readline().strip()
            try:
                _num = int(_f.readline().strip())
            except:  # escape end of file
                break
            _res[_name] = []
            _line_dict = {}
            for _iteration_number in range(_num):
                _line_str = _f.readline()
                _line_list = _line_str.split('|')
                _line_dict['ingredient_name'] = _line_list[0].strip()
                _line_dict['quantity'] = int(_line_list[1].strip())
                _line_dict['measure'] = _line_list[2].strip()
                _res[_name].append(_line_dict.copy())
            _f.readline()
    return _res


def get_shop_list_by_dishes(dishes, person_count):
    _res = {}
    _ingredient_name = []
    for dish in dishes:  # list recipes
        if dish in cook_book:  # recipe in book?
            for _ingredient in cook_book[dish]:  # ingredients in recipe
                _ingredient['quantity'] = _ingredient['quantity']
                if _ingredient['ingredient_name'] in _res:
                    _res[_ingredient['ingredient_name']]['quantity'] += person_count * _ingredient['quantity']
                else:
                    _res[_ingredient['ingredient_name']] = {}
                    _res[_ingredient['ingredient_name']]['quantity'] = person_count * _ingredient['quantity']
                _res[_ingredient['ingredient_name']]['measure'] = _ingredient['measure']
    return _res


def open_files_by_list(list_files):
    res = []
    for name in list_files:
        dict_file = {}
        with open(name, 'rt') as f:
            _input = f.readlines()
            dict_file['name'] = name
            dict_file['length'] = len(_input)
            dict_file['info'] = _input
        res.append(dict_file.copy())
    return res


def sort_by_strings(dict_file, order=False):
    # bubble sort because i'm lazy, so my code will be slow
    for i in range(len(dict_file)-1):
        for k in range(len(dict_file)-1):
            if (dict_file[k]['length'] < dict_file[k+1]['length']) == order:
                dict_file[k], dict_file[k+1] = dict_file[k+1], dict_file[k]


def write_file_by_other(name, dicts_files):
    with open(name, 'wt') as f:
        pass
    with open(name, 'at') as f:
        for element in dicts_files:
            f.write(str(element['name']) + '\n')
            f.write(str(element['length']) + '\n')
            _info = ''
            for line in element['info']:
                _info += line
            f.write(_info.strip() + '\n')


if __name__ == '__main__':
    path = os.getcwd()

    # №1
    cook_book = read_receipts(os.path.join(path, 'book.txt'))

    # №2
    ingredients_dict = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

    # №3
    os.chdir(os.path.join(path, 'working directory'))
    files_list = os.listdir()
    files_dict = open_files_by_list(files_list)
    sort_by_strings(files_dict)
    os.chdir(os.path.join(path))
    write_file_by_other('txt.txt', files_dict)
