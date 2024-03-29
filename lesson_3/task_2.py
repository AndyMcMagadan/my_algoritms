"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""

import hashlib
import os
import shutil

new_folder = "my_hash_password"  # -> В этом блоке создаем файл для хранения хеша
new_file = 'hash'
new_path = os.path.join(new_folder, new_file)
if not os.path.isdir(new_folder):
    os.makedirs(new_folder)
else:
    shutil.rmtree(new_folder)
    os.mkdir(new_folder)

my_salt = input('Введите логин: ')  # -> В качестве соли используем логин, чтобы соль была постоянной
passw_1 = input('Введите пароль: ')
result_1 = hashlib.sha256(my_salt.encode() + passw_1.encode()).hexdigest()

with open(new_path, 'w', encoding='utf-8') as f:  # -> записываем хеш 1го "соленого" пароля в файл
    f.writelines(result_1)

passw_2 = input('Введите пароль еще раз для проверки: ')
result_2 = hashlib.sha256(my_salt.encode() + passw_2.encode()).hexdigest()

with open(new_path, 'r', encoding='utf-8') as f:  # -> читаем хеш 1го "соленого" пароля из файла
    result_read = f.readline()

if result_2 == result_read:  # -> сравниваем хеши "соленых" паролей
    print('Вы ввели правильный пароль.')
