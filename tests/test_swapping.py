import unittest

import swapping


class TestSwapping(unittest.TestCase):
    def test_that_the_swap_function_exist(self):
        swapping.swap_the_string("word", "character")

    def test_that_the_swap_the_characters(self):
        actual =  swapping.swap_the_string("abc", "xyz")
        expected = "xyc abz"
        self.assertEqual(expected, actual )