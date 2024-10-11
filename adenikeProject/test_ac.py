import unittest

from ac import Ac


class TestAc(unittest.TestCase):
    def setUp(self):
        self.ac = Ac()

    def test_that_the_ac_exist(self):
        self.ac = Ac()

    def test_that_the_ac_is_on(self):
        self.assertTrue(self.ac.turn_on())

    def test_that_the_ac_is_off(self):
        self.assertFalse(self.ac.turn_off())

    def test_that_the_ac_is_increased(self):
        self.ac = Ac()
        self.assertTrue(self.ac.turn_on())
        self.ac.increased()
        self.assertEqual(17, self.ac.get_temperature())

    def test_that_the_ac_is_decreased(self):
        self.ac = Ac()
        self.assertTrue(self.ac.turn_on())
        self.ac.decreased()
        self.assertEqual(1, self.ac.get_temperature())
