import unittest
from _02_Queue.Queue import Queue


class TestQueue(unittest.TestCase):
    my_queue = Queue()

    def test01_enqueue(self):
        self.my_queue.enqueue('test_1')
        self.assertEqual(self.my_queue.head.data, 'test_1')
        self.assertEqual(self.my_queue.tail.data, 'test_1')
        self.my_queue.enqueue('test_2')
        self.assertEqual(self.my_queue.head.data, 'test_1')
        self.assertEqual(self.my_queue.tail.data, 'test_2')

    def test02_dequeue(self):
        self.assertEqual(self.my_queue.dequeue(), 'test_1')
        self.assertEqual(self.my_queue.dequeue(), 'test_2')
        self.assertEqual(self.my_queue.dequeue(), None)
