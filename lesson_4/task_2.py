"""
Задание 2.

Приведен код, который формирует из введенного числа обратное по порядку входящих в него цифр.
Задача решена через рекурсию. Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Будьте внимательны, задание хитрое. Не все так просто, как кажется.
"""

from timeit import timeit
from random import randint

num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)
num_100000 = randint(10000000000, 10000000000000000)


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=100000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=100000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=100000))
print(
    timeit(
        'recursive_reverse(num_100000)',
        setup='from __main__ import recursive_reverse, num_100000',
        number=100000))



def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=100000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=100000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=100000))
print(
    timeit(
        'recursive_reverse_mem(num_100000)',
        setup='from __main__ import recursive_reverse_mem, num_100000',
        number=100000))

"""
Мемоизация нужна, так как позволяет сохранить результаты всего десяти операций целочисленного деления на 10, и затем, 
вместо вычисления, запрашивать результаты из кеша, что гораздо быстрее вычислительной операции. Что и показывают замеры:
скорость оптимизированной функции примерно в 15-20 быстрее, в обратной зависимости от количества разрядов числа.
"""
