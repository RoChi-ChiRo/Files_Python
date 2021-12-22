import os


def read_receipts(file):
    _res = {}
    with open(file, 'r', encoding='UTF8') as _f:
        while True:
            _name = _f.readline().strip()
            try:
                _num = int(_f.readline().strip())
            except:
                break # escape end of file
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
    for dish in dishes: # list recipes
        if dish in cook_book: # recipe in book?
            for _ingredient in cook_book[dish]: # ingredients in recipe
                _ingredient['quantity'] = _ingredient['quantity']
                if _ingredient['ingredient_name'] in _res:
                    _res[_ingredient['ingredient_name']]['quantity'] += person_count * _ingredient['quantity']
                else:
                    _res[_ingredient['ingredient_name']] = {}
                    _res[_ingredient['ingredient_name']]['quantity'] = person_count * _ingredient['quantity']
                _res[_ingredient['ingredient_name']]['measure'] = _ingredient['measure']
    return _res


if __name__ == '__main__':
    print('\n№1')
    path = os.getcwd()
    file_path = os.path.join(path, 'book.txt')

    cook_book = read_receipts(file_path)
    for recipes in cook_book:
        print(recipes)
        for ingredient in cook_book[recipes]:
            print(ingredient)
        print()

    print('\n№2')
    ingredients_dict = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    for name, number in ingredients_dict.items():
        print(name, number)

    print('\n№3')
    file_path1 = os.path.join(path, '1.txt')
    with open(file_path1, 'rt') as f:
        text1 = f.readlines()

    file_path2 = os.path.join(path, '2.txt')
    with open(file_path2, 'rt') as f:
        text2 = f.readlines()

    file_path3 = os.path.join(path, '3.txt')
    with open(file_path3, 'wt') as f:
        if text1 > text2:
            f.write(f'1.txt\n{len(text1)}\n')
            for string in text1:
                f.write(string)
            f.write(f't2.txt\n{len(text2)}\n')
            for string in text2:
                f.write(string)
        else:
            f.write(f't2.txt\n{len(text2)}\n')
            for string in text2:
                f.write(string)
            f.write(f'1.txt\n{len(text1)}\n')
            for string in text1:
                f.write(string)
    print('Look files')
