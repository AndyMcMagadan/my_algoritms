"""
Задание 4.

Приведены два алгоритма. В них определяется число, которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""

from timeit import timeit
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1, 6, 8, 9, 1, 4, 5, 4, 5, 6, 9]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    num = list(Counter(array))[0]
    max_3 = max(Counter(array).values())
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {max_3} раз(а)'


def func_4():
    for k, v in Counter(array).items():
        return f'Чаще всего встречается число {k}, ' \
               f'оно появилось в массиве {v} раз(а)'



print(func_1())
print(timeit("func_1()", setup='from __main__ import func_1', number=100000))
print(func_2())
print(timeit("func_2()", setup='from __main__ import func_2', number=100000))
print(func_3())
print(timeit("func_3()", setup='from __main__ import func_3', number=100000))
print(func_4())
print(timeit("func_4()", setup='from __main__ import func_4', number=100000))

"""
Использование collections.Counter позволило получить самый быстрый алгоритм для определения числа, наиболее часто
встречающегося в массиве данных. Особенно это будет заметно для массивов с большой длиной и большим количеством данных.
Первый алгоритм основан только на цикле for, и поэтому гораздо быстрее второго, где кроме цикла for есть еще получение 
элемента массива по его индексу.
Третий же алгоритм содержит два вычисления с использованием встроенного модуля, поэтому является самым быстрым, 
несмотря на преобразование типов данных. Оптимизация третьего алогритма - вывод всего одного значения "ключ-значение"
из цикла, сделала его примерно в два раз быстрее. По другому у меня не выходило получить первую пару "ключ-значение" 
из словаря collections.Counter, зато избавился от преобразования в другой тип данных, что сэкономило время и память.
"""
