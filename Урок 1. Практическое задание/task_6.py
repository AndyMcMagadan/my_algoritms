"""
Задание 6.
Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются на корректировку решения

"""

from my_class_module import QueueClass


def done_kanban(duration, rate):
    i = 0
    for day in range(duration):
        elem = new_tasks.from_queue()
        i += rate
        if not i < 1:
            deferred_tasks.to_queue(elem)
            i = 0
        else:
            done_tasks.to_queue(elem)
    print(f'Выполнено работ в течение {done_tasks.queue_size()} дней, в составе {done_tasks.get_value()}')
    print(f'Отложено работ на {deferred_tasks.queue_size()} дней, в составе {deferred_tasks.get_value()}')


def my_kanban(dict, duration, rate):  # заполняем доску задач
    for event, days in dict.items():
        for day in range(days):
            new_tasks.to_queue(event)
    print(f'Запланировано работ на {new_tasks.queue_size()} дней, в составе {new_tasks.get_value()}')
    done_kanban(duration, rate) # запускаем работу в течение duration, с процентом выполнения rate



new_tasks = QueueClass()  # доска задач
deferred_tasks = QueueClass()  # отложенные задачи
done_tasks = QueueClass()  # выполненные задачи
event_dict = {  # название работы-задачи и продолжительность в днях
    "планировать": 2,
    "коструировать лопату": 3,
    "коструировать тяпку": 3,
    "изготавливать лопату": 3,
    "изготавливать тяпку": 4,
    "искать клад": 5,
    "искать огород": 3,
    "копать клад": 5,
    "копать грядки": 7,
    "сажать рассаду": 3
}

my_kanban(event_dict, 25, 0.2) # передаем перечень задач, продолжительность выполнения работ и процент отложенных
