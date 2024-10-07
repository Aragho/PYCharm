import unittest
from television import Tv

class TestForTelevision(unittest.TestCase):
    def setUp(self):
        self.tv = Tv()
    def test_that_tv_can_be_turn_on(self):
        self.assertTrue(self.tv.turn_on())

    def test_that_tv_can_be_turn_off(self):
        self.assertFalse(self.tv.turn_Off())

    def test_that_the_tv_can_get_channel(self):
        self.tv.turn_on()
        self.assertEqual(0,self.tv.get_Channel())

    def test_that_the_tv_can_set_channel(self):
        self.tv.turn_on()
        self.assertEqual(7,self.tv.set_Channel(7))

    def test_that_the_tv_can_get_volume(self):
        self.tv.turn_on()
        self.assertEqual(0,self.tv.get_volume())

    def test_that_the_tv_can_set_volume(self):
        self.tv.turn_on()
        self.assertEqual(50,self.tv.set_volume(50))

    def test_that_the_tv_can_channel_up(self):
        self.tv.turn_on()
        self.tv.set_Channel(10)
        self.assertEqual(10 ,self.tv.get_Channel())
        self.tv.channel_up()
        self.assertEqual(11,self.tv.get_Channel())

    def test_that_the_tv_can_channel_down(self):
        self.tv.turn_on()
        self.tv.set_Channel(11)
        self.assertEqual(11 ,self.tv.get_Channel())
        self.tv.channel_down()
        self.assertEqual(10,self.tv.get_Channel())

    def test_that_the_tv_can_volume_up(self):
        self.tv.turn_on()
        self.tv.set_volume(20)
        self.assertEqual(20,self.tv.get_volume())
        self.tv.volume_up()
        self.assertEqual(21,self.tv.get_volume())

    def test_that_the_tv_can_volume_down(self):
        self.tv.turn_on()
        self.tv.set_volume(17)
        self.assertEqual(17,self.tv.get_volume())
        self.tv.volume_down()
        self.assertEqual(16,self.tv.get_volume())




