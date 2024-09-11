import unittest

import capital_letter
import cece
import semicolon_africa


class TestSwapping(unittest.TestCase):
    def test_that_the_swipe_function_exist(self):
        cece.swipe_the_character("word", "character")

    def test_that_the_functionality(self):
        actual = cece.swipe_the_character("hello")
        expected = "helcelo"
        self.assertEqual(expected, actual)


class TestCapitalLetter(unittest.TestCase):
    def test_that_the_function_exist(self):
        capital_letter.check_capital_letter("word")

    def test_that_the_capital_letter_comes_first(self):
        actual = capital_letter.check_capital_letter("AdeNike")
        expected = "ANdeike"
        self.assertEqual(expected, actual)


class TestSemicolon(unittest.TestCase):
    def test_that_the_function_exist(self):
        semicolon_africa.count_letter("character")
    def test_that_the_functionality(self):
        actual = 'semicolon.africa'
        expected = {'s':1,'e':1,'m':1,'i':2,'c':2,'o':2,'l':1,'n':1,'.':1,'a':2,'f':1,'r':1}
        self.assertEqual(expected, actual)
