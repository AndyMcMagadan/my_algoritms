"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import timeit
import random


def merge_sort(new_list, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(new_list, start, mid)
        merge_sort(new_list, mid, end)
        merge_list(new_list, start, mid, end)
    return new_list


def merge_list(new_list, start, mid, end):
    left = new_list[start:mid]
    right = new_list[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            new_list[k] = left[i]
            i = i + 1
        else:
            new_list[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            new_list[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            new_list[k] = right[j]
            j = j + 1
            k = k + 1


my_number = int(input('Введите количество элементов массива: '))
my_list = [(random.randint(10000000000, 1000000000000) / 10000000000) for _ in range(my_number)]
print('Исходный массив: ', my_list)
merge_sort(my_list, 0, len(my_list))
print('Итоговый массив: ', merge_sort(my_list, 0, len(my_list)))
print(f'Время выполнения: {timeit.timeit("merge_sort(my_list, 0, len(my_list))", globals=globals(), number=1000)}')

"""
Время работы алгоритма растет практически в логарифмической последовательности от количества элементов массива:
10 элементов: 0.011838618000000078
100 элементов: 0.149750649
1000 элементов: 2.2154033179999995
10000  элементов: 28.458854216
"""
