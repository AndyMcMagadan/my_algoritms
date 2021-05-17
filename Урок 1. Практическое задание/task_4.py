""" Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию. В системе хранятся логин, пароль и отметка об активации учетной
записи. Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу. При этом его учетка должна быть
активирована. А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции. Для реализации хранилища можно
применить любой подход, который вы придумаете, например, реализовать словарь.
"""

users_data = {
    # Login : [Password, Name, Last_name, Birthday, Mobile, Status]
    'alex_88': ['my_soul#777', 'Alex', 'Broggy', '22.03.1988', '765-985-4555', 0],
    'sophichka': ['5898&higirl', 'Sophia', 'Smith', '12.09.1991', '235-788-2333', 0],
    'cracker': ['555999', 'Cracker', 'Bug', '01.01.1990', '555-555-5555', 0]
}


# First way. Total >> # O(N)
def check_login(login):                                                 # O(1)
    if login in users_data:                                             # O(N)
        check_pass()                                                    # O(1)
    else:                                                               # O(1)
        print('Login does not exist. Please register now.')             # O(1)


def check_pass():                                                       # O(1)
    i = 0                                                               # O(1)
    while i < 3:                                                        # O(1)
        password = input('Please enter Your password: ')                # O(1)
        if password == users_data[user_login][0]:                       # O(N)
            users_data[user_login].pop(-1)                              # O(1)
            users_data[user_login].append(1)                            # O(1)
            print("Your account is activated. Welcome!")                # O(1)
            break                                                       # O(1)
        else:                                                           # O(1)
            i += 1                                                      # O(1)
            print(f'Wrong password. You have yet {(3 - i)} attemps!')   # O(1)


user_login = input('Please enter Your login: ')                         # O(1)
check_login(user_login)                                                 # O(1)


# Second way. Total >> O(N**2) Теперь понимаю, почему функции надо разносить - упрощать.
def check_user(login, password):                                            # O(1)
    if login in users_data:                                                 # O(N)
        i = 0                                                               # O(1)
        while i < 3:                                                        # O(1)
            if password == users_data[user_login][0]:                       # O(N) - вот эта вложенность в поиске по
                users_data[user_login].pop(-1)                              # O(1)   словарю, привела к О(N**2)
                users_data[user_login].append(1)                            # O(1)
                print("Your account is activated. Welcome!")                # O(1)
                break                                                       # O(1)
            else:                                                           # O(1)
                i += 1                                                      # O(1)
                print(f'Wrong password. You have yet {(3 - i)} attemps!')   # O(1)
                password = input('Please enter Your password: ')            # O(1)
    else:                                                                   # O(1)
        print('Login does not exist. Please register now.')                 # O(1)


user_login = input('Please enter Your login: ')                             # O(1)
user_password = input('Please enter Your password: ')                       # O(1)
check_user(user_login, user_password)                                       # O(1)
