class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):  # проверка, что стек пустой
        return self.elems == []

    def push_in(self, el):  # наполняем стек
        self.elems.append(el)

    def pop_out(self):  # убираем элемент с вершины стека и возвращаем его значение
        return self.elems.pop()

    def get_val(self):  # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
        return self.elems[len(self.elems) - 1]

    def get_value(self):  # получаем содержимое стека
        return self.elems

    def clear_value(self):  # очищаем весь стек сразу
        return self.elems.clear()

    def stack_size(self):  # узнаем размер стека
        return len(self.elems)


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):  # проверка, что очередь пустая
        return self.elems == []

    def to_queue(self, item):  # помещаем объекты в очередь
        self.elems.insert(0, item)

    def from_queue(self):  # получаем первый (верхний) элемент из очереди
        return self.elems.pop()

    def queue_size(self):  # размер очереди
        return len(self.elems)

    def get_value(self):  # получаем содержимое очереди
        return self.elems

    def clear_value(self):  # очищаем всю очередь сразу
        return self.elems.clear()


class DequeClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):  # проверка, что дек пустой
        return self.elems == []

    def add_to_front(self, elem):  # добавить элемент в начало дека
        self.elems.append(elem)

    def add_to_rear(self, elem):  # добавить элемент в хвост дека
        self.elems.insert(0, elem)

    def remove_from_front(self):  # извлечь элемент с начала дека
        return self.elems.pop()

    def remove_from_rear(self):  # извлечь элемент с конца дека
        return self.elems.pop(0)

    def deque_size(self):  # размер дека
        return len(self.elems)

    def get_value(self):  # получаем содержимое дека
        return self.elems

    def clear_value(self):  # очищаем весь дек сразу
        return self.elems.clear()


if __name__ == '__main__':
    SC_OBJ = StackClass()
    print(SC_OBJ.is_empty())  # -> True. Cтек пустой
    print(SC_OBJ.get_value())

    QC_OBJ = QueueClass()
    print(QC_OBJ.is_empty())  # -> True. Очередь пустая
    print(QC_OBJ.get_value())

    DC_OBJ = DequeClass()
    print(DC_OBJ.is_empty())  # -> True. Дек пустой
    print(DC_OBJ.get_value())
