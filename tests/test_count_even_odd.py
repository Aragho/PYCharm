import unittest

import count_even_odd


class TestCountEvenOdd(unittest.TestCase):
    def test_that_the_function_exist(self):
        count_even_odd.count_even_odd([3,2])

    def test_the_functionality(self):
        actual = count_even_odd.count_even_odd([2,1,5,7,8])
        expected = [2,3]
        self.assertEqual(expected,actual)
    def test_the_functionality2(self):
        actual = count_even_odd.count_even_odd([4,1,5,7,9])
        expected = [1,4]
        self.assertEqual(expected,actual)
