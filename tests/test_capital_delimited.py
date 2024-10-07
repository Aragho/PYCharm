import unittest
from lagbajaschool.capitals_delimited import capital

class TestCapitalized(unittest.TestCase):
    def test_that_the_function_exist(self):
        capital("character")

    def test_the_functionality(self):
        word = "The-Stealth-Warrior"
        actual = capital(word)
        expected = "TheStealthWarrior"
        self.assertEqual(expected, actual)

