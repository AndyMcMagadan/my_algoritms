"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение.
Обязательно сделайте замеры времени обеих реализаций и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере, а по убыванию.

Сделайте выводы!!! Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import random
import timeit
from time import time


def time_decorator(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполнения функции {func.__name__} составило {end - start}')
        return result

    return timer


@time_decorator
def reverse_bubble(new_list):
    for k in range(100000):
        num = 1
        while num < len(new_list):
            for i in range(len(new_list) - num):
                if new_list[i] < new_list[i + 1]:
                    new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
                num += 1
    return new_list


@time_decorator
def reverse_bubble_mod(new_list):
    for k in range(100000):
        exchange, k, step = True, 0, 0
        for i in range(0, len(new_list) - 1):
            if not exchange:
                break
            exchange = False

            for j in range(len(new_list) - 1, step, -1):
                if new_list[j] > new_list[j - 1]:
                    exchange = True
                    new_list[j - 1], new_list[j] = new_list[j], new_list[j - 1]
                    k = j
            step = k
    return new_list


my_list = [random.randint(-100, 100) for _ in range(200)]
print(f'Исходный список:\n{my_list}')
result = reverse_bubble(my_list[:])
print(f'Получен новый список:\n{result}')
print(f'Время выполнения, замерянное модулем timeit: '
      f'{timeit.timeit("reverse_bubble(my_list[:])", globals=globals(), number=1)}')
print(f'Исходный список:\n{my_list}')
result_mod = reverse_bubble_mod(my_list[:])
print(f'Получен новый список:\n{result_mod}')

"""
Обратная сортировка достигается заменой знака ">" на "<" при сравнении элементов списка.
Разные способы замеров времени работы "пузырька" - через декоратор и модуль timeit дают результаты одного порядка.
При отстуствии изменений в одной иттерации функция модифицированная переходит к следующей иттерации. 
Выигрыш во времени от 10 до 25% в зависимости от размера массива.
"""
