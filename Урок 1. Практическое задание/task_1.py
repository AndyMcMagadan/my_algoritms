# Задание 1.
# Для каждой из трех задач выполнить следующее:
# 1) для каждого выражения вместо !!! укажите сложность этого выражения.
# 2) определите сложность задачи в целом.

import random


# Алгоритм 3: Создать множество из списка
def check_1(lst_obj):                       # O(len(lst_obj)) + O(1)
    lst_to_set = set(lst_obj)               # O(len(lst_obj))
    return lst_to_set                       # O(1)


# Алгоритм 1: Проходимся по списку и для каждого элемента проверяем,
# что такой элемент отстутствует в оставшихся справа элементах
def check_2(lst_obj):                       # O(N**2) + O(1)
    for j in range(len(lst_obj)):           # O(N)
        if lst_obj[j] in lst_obj[j + 1:]:   # O(N)
            return False                    # O(1)
    return True                             # O(1)


# Алгоритм 2: Вначале выполним для списка сортировку, далее, сравниваем элементы попарно.
# Если присутствуют дубли, они будут находиться рядом.
def check_3(lst_obj):                       # O(N) + O(N*logN) + O(N**2) + O(1)
    lst_copy = list(lst_obj)                # O(N)
    lst_copy.sort()                         # O(N*logN)
    for i in range(len(lst_obj) - 1):       # O(N)
        if lst_copy[i] == lst_copy[i + 1]:  # O(N)
            return False                    # O(1)
    return True                             # O(1)


for j in (50, 500, 1000, 5000, 10000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))
