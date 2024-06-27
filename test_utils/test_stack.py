import unittest
from _01_Stack.Stack import Stack


class TestStack(unittest.TestCase):
    my_stack = Stack()

    def test01_push(self):
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.my_stack.push('test')
        self.my_stack.push(2.1)
        self.my_stack.push(3)
        self.assertEqual(self.my_stack.top.data, 3)
        self.assertEqual(self.my_stack.top.next_node.data, 2.1)
        self.assertEqual(self.my_stack.top.next_node.next_node.data, 'test')
        self.assertEqual(self.my_stack.top.next_node.next_node.next_node.data, 2)
        self.assertEqual(self.my_stack.top.next_node.next_node.next_node.next_node.data, 1)
        self.assertEqual(self.my_stack.push(12), 'Стэк переполнен')

    def test02_get_data(self):
        self.assertEqual(self.my_stack.get_data(0), 3)
        self.assertEqual(self.my_stack.get_data(1), 2.1)
        self.assertEqual(self.my_stack.get_data(2), 'test')
        self.assertEqual(self.my_stack.get_data(3), 2)
        self.assertEqual(self.my_stack.get_data(4), 1)
        self.assertEqual(self.my_stack.get_data(5), 'Out of range')

    def test03_size_stack(self):
        self.assertEqual(self.my_stack.size_stack(), 5)

    def test04_counter_int(self):
        self.assertEqual(self.my_stack.counter_int(), 3)

    def test05_is_full(self):
        self.assertEqual(self.my_stack.is_full(), True)
        self.my_stack.pop()
        self.my_stack.pop()
        self.my_stack.pop()
        self.my_stack.pop()
        self.my_stack.pop()
        self.assertEqual(self.my_stack.is_full(), False)

    def test06_pop(self):
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.my_stack.push('test')
        self.my_stack.push(2.1)
        self.my_stack.push(3)
        self.assertEqual(self.my_stack.pop(), 3)
        self.assertEqual(self.my_stack.pop(), 2.1)
        self.assertEqual(self.my_stack.pop(), 'test')
        self.assertEqual(self.my_stack.pop(), 2)
        self.assertEqual(self.my_stack.pop(), 1)
        self.assertEqual(self.my_stack.pop(), 'Стэк пуст')

    def test07_is_empty(self):
        self.assertEqual(self.my_stack.is_empty(), True)
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.my_stack.push('test')
        self.my_stack.push(2.1)
        self.my_stack.push(3)
        self.assertEqual(self.my_stack.is_empty(), False)

    def test08_clear_stack(self):
        self.assertEqual(self.my_stack.clear_stack(), 'Stack cleared')
