"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


# Как вариант упрощения и реализации мне понравилась вот эта структура:

class Node: # -> класс узел - место крепления ветвей и сравнения значений для правого или левого добавления
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree: # -> класс дерево, собственно
    def __init__(self):
        self.root = None

    def getRoot(self): # -> метод получения значений у дерева
        return self.root

    def add(self, val):  # -> метод добавления корня (первого значения)
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):  # -> метод добавления ветвей
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):  # -> метод поиска значения корня
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):  # -> метод поиска значения (при наличии) ветвей
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)

    def deleteTree(self):  # -> метод удаления дерева
        self.root = None

    def printTree(self):  # -> методы печати (работают не стабильно и не отображают корректно почему-то)
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)


#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print(tree.find(3).v)
print(tree.find(8))
