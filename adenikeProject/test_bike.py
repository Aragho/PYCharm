import unittest
from bike import Bike

class  TestBike(unittest.TestCase):
    def setUp(self):
        self.bike = Bike()
    def test_that_the_bike_exist(self):
         self.bike = Bike()

    def test_that_the_bike_is_on(self):
        self.assertTrue(self.bike.turn_on())

    def test_that_the_bike_is_off(self):
        self.assertFalse(self.bike.turn_off())
    def test_that_the_bike_accelerate_at_gear_one(self):
        self.bike = Bike()
        self.assertTrue(self.bike.turn_on())
        self.bike.accelerate(19,1)
        self.assertEqual(20,self.bike.get_accelerate())

    def test_that_the_bike_accelerate_at_gear_two(self):
         self.assertTrue(self.bike.turn_on())
         self.bike.accelerate(24, 2)
         self.assertEqual(26, self.bike.get_accelerate())

    def test_that_the_bike_accelerate_at_gear_three(self):
         self.assertTrue(self.bike.turn_on())
         self.bike.accelerate(35, 3)
         self.assertEqual(38, self.bike.get_accelerate())

    def test_that_the_bike_accelerate_at_gear_four(self):
         self.assertTrue(self.bike.turn_on())
         self.bike.accelerate(41, 4)
         self.assertEqual(45, self.bike.get_accelerate())

    def test_that_the_bike_deccelerate_at_gear_one(self):
        self.assertTrue(self.bike.turn_on())
        self.bike.deccelerate(15, 1)
        self.assertEqual(14, self.bike.get_decelerate())

    def test_that_the_bike_deccelerate_at_gear_two(self):
        self.assertTrue(self.bike.turn_on())
        self.bike.deccelerate(24, 2)
        self.assertEqual(22, self.bike.get_decelerate())

    def test_that_the_bike_deccelerate_at_gear_three(self):
        self.assertTrue(self.bike.turn_on())
        self.bike.deccelerate(35, 3)
        self.assertEqual(32, self.bike.get_decelerate())

    def test_that_the_bike_deccelerate_at_gear_four(self):
        self.assertTrue(self.bike.turn_on())
        self.bike.deccelerate(44, 4)
        self.assertEqual(40, self.bike.get_decelerate())









