class Node:
    """Класс узла связанного списка. Содержит данные (data) и ссылку на следующий узел (next_node)"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс использующий узлы(Класс Node), чтобы создать стек"""
    def __init__(self, stack_size=5, top=None):
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    def push(self, data):
        """Метод добавления элемента в стек"""
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            print("Стэк переполнен")
            return "Стэк переполнен"

    def pop(self):
        """Метод удаления верхнего элемента в стеке"""
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"

    def is_empty(self):
        """Метод возвращает True, если стек пуст, иначе возвращает False"""
        if self.top:
            return False
        else:
            return True

    def is_full(self):
        """Метод возвращает True, если стек заполнен, иначе возвращает False"""
        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    def clear_stack(self):
        """Метод очищает полностью стек"""
        while self.top:
            self.pop()
        return 'Stack cleared'

    def get_data(self, index):
        """Метод возвращает элемент по выбранному индексу. Если такого индекса нет возвращает 'Out of range'"""
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    def size_stack(self):
        """Метод для подсчета кол-ва элементов в стеке"""
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):
        """Метод для подсчета кол-ва целых чисел в стеке"""
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter