"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Подсказка:
Базовый случай здесь - угадали число или закончились попытки

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

import random


def check_number(number, check_num):
    if check_num < 10:
        user_number = int(input('Введите Ваше число от 0 до 100: '))
        if user_number == number:
            print(f'Число отгадано верно: {user_number} за {check_num} попыток.')
        else:
            if user_number < number:
                print(f'Загаданное число больше Вашего.')
            else:
                print(f'Загаданное число меньше Вашего.')
            check_num += 1
            print(f'Число не отгадано. Осталось {(10 - check_num)} попыток.')
            check_number(number, check_num)
    else:
        print(f'Вы не угадали. Было загадано число {number}.')


num_2 = 0
num_1 = random.randint(0, 100)
check_number(num_1, num_2)
