from django.test import TestCase
from .utils import Queue
import unittest

# Create your tests here.

class TestQueue (unittest.TestCase):
    def test_init_queue(self):
        queue = Queue("FIFO")

    def test_raise_value_error(self):
        with self.assertRaises(ValueError):
            queue = Queue("FIFO")

    def test_add_fifo_value(self):
        queue = Queue("FIFO")
        first_value = 5
        queue.add(first_value)
        value = queue.pop() # возвращение числа из очереди
        self.assertRaises(value, first_value)

