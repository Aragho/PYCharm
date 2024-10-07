import unittest

import separated_numbers


class TestGeneratingNumbers(unittest.TestCase):
    def test_that_the_function_works(self):
        separated_numbers.sequence_of_numbers("numbers")

    def test_the_function_works(self):
        numbers = '34,67,55,33,12,98'
        actual = separated_numbers.sequence_of_numbers(numbers)
        expected = f"['34', '67', '55', '33', '12', '98']('34', '67', '55', '33', '12', '98')"
        self.assertEqual(actual, expected)

    def test_the_function_works_2(self):
          numbers = '34,67,55,33,12,98'
          actual = separated_numbers.sequence_of_numbers(numbers)
          expected = f"['34', '67', '55', '33', '12', '98']('34', '67', '55', '33', '12', '98')"
          self.assertEqual(actual, expected)


