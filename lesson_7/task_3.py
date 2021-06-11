"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные по длине части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]

from statistics import median

[3, 4, 3, 3, 5, 3, 3]

left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()
"""
import timeit
from my_class_module import DequeClass


def shell_sort(a):  # -> Почему то не корректно отрабатывает сортировка Шелла из методички, с ошибками
    def new_increment(a):
        i = int(len(a) / 2)
        yield i
        while i != 1:
            if i == 2:
                i = 1
            else:
                i = int(round(i / 2.2))
                yield i

    for increment in new_increment(a):
        for i in range(increment, len(a)):
            for j in range(i, increment - 1, -increment):
                if a[j - increment] < a[j]:
                    break
                a[j], a[j - increment] = a[j - increment], a[j]
    return a


def shell_sort_forum(new_list):  # -> Более короткий код с форума работает корректно и быстрее
    inc = len(new_list) // 2
    while inc:
        for i, el in enumerate(new_list):
            while i >= inc and new_list[i - inc] > el:
                new_list[i] = new_list[i - inc]
                i -= inc
            new_list[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return new_list


def mediana_find(new_list):
    dc_obj = DequeClass()  # -> воспользуемся классом Deque из первого урока
    result = shell_sort_forum(new_list)
    for el in result:
        dc_obj.add_to_rear(el)
    while dc_obj.deque_size() > 1:
        dc_obj.remove_from_front()
        dc_obj.remove_from_rear()
        if dc_obj.deque_size() == 1:
            return dc_obj.remove_from_rear()


my_list = [54, 1, 25, 3, 52, 3, 1, 2, 15, 28, 36, 14, 3, 1, 1, 15, 23, 67, 3, 82, 543]
print('Длина исходного массива 2m + 1 = ', len(my_list))
print('Сортировка исходного массива shell_sort', shell_sort(my_list[:]))
print(f'Время выполнения shell_sort function: '
      f'{timeit.timeit("shell_sort(my_list[:])", globals=globals(), number=10000)}')
print('Сортировка исходного массива shell_sort_forum: ', shell_sort_forum(my_list[:]))
print(f'Время выполнения shell_sort_forum function: '
      f'{timeit.timeit("mediana_find(my_list[:])", globals=globals(), number=10000)}')
print('Медиана исходного массива: ', mediana_find(my_list[:]))
print(f'Время выполнения mediana_find с вызовом shell_sort_forum: '
      f'{timeit.timeit("mediana_find(my_list[:])", globals=globals(), number=10000)}')
