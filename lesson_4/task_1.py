"""
Задание 1.

Приведен код, который позволяет сохранить в массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения. Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""

from timeit import timeit
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(0, len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = [i for i, num in enumerate(nums) if num % 2 == 0]
    return new_arr


my_nums = [randint(0, n * 33) for n in range(0, 100)]

print(timeit("func_1(my_nums)", setup='from __main__ import func_1, my_nums', number=100000))
print(func_1(my_nums))
print(timeit("func_2(my_nums)", setup='from __main__ import func_2, my_nums', number=100000))
print(func_2(my_nums))
print(timeit("func_3(my_nums)", setup='from __main__ import func_3, my_nums', number=100000))
print(func_3(my_nums))

"""
ИМХО, способ оптимизации заполнения второго массива индексами четных чисел из первого по сравнению с циклом for - сразу
вспомнил из своего небольшого опыта про list comprehension. Реализовал, замерил время выполнения с разными размерами 
массивов - работает на 20-25% быстрее, чем через цикл for. Применение enumerate() вместо for внутри list comprehension
позволило выиграть еще около от 1% до 5% скорости. С увеличением исходного массива на порядок и более разница в 
скорости работы (эффективность) снижается.
"""
