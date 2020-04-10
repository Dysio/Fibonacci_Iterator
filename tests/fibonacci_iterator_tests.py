import unittest

from fibonacci_iterator import FibonacciIterable


class FibonacciTest(unittest.TestCase):

    def test_proper_value(self):
        self.assertRaises(TypeError, FibonacciIterable, 'a')
        self.assertRaises(TypeError, FibonacciIterable, 3.4)

    def test_values(self):
        i_num = 6
        fibonacci = FibonacciIterable(i_num)

        fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

        i = 0
        while i < i_num:
            fib_next = fibonacci.__next__()
            self.assertEqual(fib_next, fib_list[i])
            i += 1
