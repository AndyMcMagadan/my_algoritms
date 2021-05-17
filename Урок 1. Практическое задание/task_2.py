# Задание 2.
# Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
# В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
# Сложность такого алгоритма: O(n^2) - квадратичная.
# Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
# Сложность такого алгоритма: O(n) - линейная.

# Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
# можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

def first_search_min(my_list):      # O(N**2) + O(1) + O(1) + O(1)
    for minim in my_list:           # O(N)
        for num in my_list:         # O(N)
            if minim > num:         # O(1)
                minim = num         # O(1)
    return minim                    # O(1)


def second_search_min(my_list):     # O(N) + O(1)
    result = min(my_list)           # O(N)
    return result                   # O(N)


def my_search_min(my_list):         # O(N*logN) + O(1)
    my_list.sort()                  # O(N*logN)
    return my_list[0]               # O(1)


lst = [11, 12, 13, - 14, - 1, 2, 3, 4, 13, - 14, - 1, 2, 3, 4, 5, 6, 7, 8, 9, - 10, 43, 15]
print(f'Minimum: in 1t time: {first_search_min(lst)}, in 2d time: {second_search_min(lst)}, in my proba: {my_search_min(lst)}.')
