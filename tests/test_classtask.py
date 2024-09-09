import unittest
import class_task

class TestCount(unittest.TestCase):
    def test_that_count_function_exists(self):
        class_task.count_in_dict("word")

    def test_that_count_the_number_of_characters(self):
        result ={"n":1, "i":1, "k":1, "e":2}
        self.assertEqual(result, class_task.count_in_dict("nikee"))
        self.assertEqual({'a':1, 'w':1, 'e':1}, class_task.count_in_dict("awe"))

    def test_that_count_of_number_ignore_case(self):
        self.assertEqual({'a':1, 'w':1, 'e':2}, class_task.count_in_dict("awEe"))

