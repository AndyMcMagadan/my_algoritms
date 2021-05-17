"""
Задание 7.

В рассмотренном на уроке листинге есть один недостаток:
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'
Но могут быть и такие палиндромы, как 'молоко делили ледоколом'
Нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""

from my_class_module import DequeClass


def pal_checker(string):
    dc_obj = DequeClass()
    for el in string:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.deque_size() > 1 and still_equal:
        if dc_obj.deque_size() == 1:
            break
        else:
            first = dc_obj.remove_from_front()
            if first == ' ':
                first = dc_obj.remove_from_front()
            last = dc_obj.remove_from_rear()
            if last == ' ':
                last = dc_obj.remove_from_rear()
            if first != last:
                still_equal = False

    return still_equal


print(pal_checker("молоко делили ледоколом"))
