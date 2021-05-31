"""
Задание 3.

Приведен код, формирующий из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit.

Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""

from timeit import timeit
from random import randint
from cProfile import run

num_1 = randint(10000000000, 10000000000000000)


def revers_1(enter_num, revers_num=0):  # -> Рекурсия, самое большое время выполнения. Сложность О(n!)
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return int(revers_1(enter_num, revers_num))


def revers_2(enter_num, revers_num=0):  # -> Цикл с условием while - второй по медленности. Сложность О(n)
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


def revers_3(enter_num):  # -> Преобразование числа в строку и взятие обратного среза. Самый быстрый. Сложность О(1)
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return int(revers_num)


def my_revers(enter_num):
    """
    Двойное преобразование числа в строку и список и получение обратного списка. Второй по скорости. Сложность О(n),
    но за счет того, что функция reverse() - встроенная, работает быстрее, чем цикл while.
    """

    my_list = list(str(enter_num))
    my_list.reverse()
    return int(''.join(my_list))


print(revers_1(num_1))
print(timeit("revers_1(num_1)", setup='from __main__ import revers_1, num_1', number=100000))
run('revers_1(num_1)')
print(revers_2(num_1))
print(timeit("revers_2(num_1)", setup='from __main__ import revers_2, num_1', number=100000))
run('revers_2(num_1)')
print(revers_3(num_1))
print(timeit("revers_3(num_1)", setup='from __main__ import revers_3, num_1', number=100000))
run('revers_3(num_1)')
print(my_revers(num_1))
print(timeit('my_revers(num_1)', setup='from __main__ import my_revers, num_1', number=100000))
run('my_revers(num_1)')
