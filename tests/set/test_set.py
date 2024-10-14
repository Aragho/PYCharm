import unittest

from set.set import Set



class TestSet(unittest.TestCase):
    def setUp(self):
        self.set = Set()

    def test_is_empty(self):
        self.assertTrue(self.set.is_empty())

    def test_that_add_an_element_to_set(self):
        self.set.add(20)
        self.assertFalse(self.set.is_empty())

    def test_that_add_all_elements_to_set(self):
        self.set.add_all(10,20,30,40,50)
        self.assertEqual(5,self.set.size())

    def test_that_remove_an_element_from_set(self):
        self.set.add_all(10, 20, 30, 40, 50)
        self.set.remove(30)
        self.assertEqual(4,self.set.size())
    def test_that_clear_all_elements_from_set(self):
        self.set.add_all(10, 20, 30, 40, 50)
        self.set.clear()
        self.assertTrue(self.set.is_empty())
    def test_contains_element_throws_exception(self):
        self.assertTrue(self.set.is_empty())
        with self.assertRaises(KeyError):
            self.set.contains(100)
    def test_remove_element_throws_exception(self):
        self.assertTrue(self.set.is_empty())
        with self.assertRaises(KeyError):
            self.set.remove(130)
    def test_add_duplicate_element_size_remains_unchanged(self):
        self.set.add_all(10, 20, 30, 40, 50)
        self.set.add(10)
        self.assertEqual(5,self.set.size())
