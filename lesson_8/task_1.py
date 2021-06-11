"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

from collections import Counter


class Tree:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def get_code(root, codes=dict(), code=''):
    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')

    return codes


def get_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        my_tree = Tree(None)

        if len(string_count) == 1:
            my_tree.left = Tree([key for key in string_count][0])
            my_tree.right = Tree(None)

        string_count = {my_tree: 1}

    while len(string_count) != 1:
        my_tree = Tree(None)
        spam = string_count.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            my_tree.left = Tree(spam[0][0])

        else:
            my_tree.left = spam[0][0]

        if isinstance(spam[1][0], str):
            my_tree.right = Tree(spam[1][0])

        else:
            my_tree.right = spam[1][0]

        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[my_tree] = spam[0][1] + spam[1][1]

    return [key for key in string_count][0]


def coding(string, codes):
    result = ''

    for symbol in string:
        result += codes[symbol]

    return result


def decoding(new_string, codes):
    result = ''
    i = 0

    while i < len(new_string):

        for code in codes:

            if new_string[i:].find(codes[code]) == 0:
                result += code
                i += len(codes[code])

    return result


my_string = input('Введите строку для сжатия: ')
tree = get_tree(my_string)

codes = get_code(tree)
print(f'Шифр: {codes}')

coding_str = coding(my_string, codes)
print(f'Сжатая строка: {coding_str}')

decoding_str = decoding(coding_str, codes)
print(f'Исходная строка: {decoding_str}')

if my_string == decoding_str:
    print('Кодирование и декодироание прошло успешно!')
else:
    print('Ошибка в операции!')
