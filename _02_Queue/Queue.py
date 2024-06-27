class Node:
    """Класс узла связанного списка. Содержит данные (data) и ссылку на следующий узел (next_node)"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс использующий узлы(Класс Node), чтобы создать очередь"""
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """Метод добавления элемента в очередь"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

    def dequeue(self):
        """Метод удаления элемента из очереди"""
        if self.head is None:
            return None
        else:
            dequeue_item = self.head
            self.head = self.head.next_node
        return dequeue_item.data
