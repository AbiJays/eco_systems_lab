import unittest
from src.bear import Bear
from src.fish import Fish
from src.river import River
from tests.river_test import TestRiver
# do test part first in order to conceptualise what it is we are going to test. this is what we are going to do here. 

class TestBear(unittest.TestCase):
    # convention to define and refer to classes with this capitalisation syntax. uppercase classes.
    def setUp(self):
        self.bear_1 = Bear("Yogi", "grizzly")

        self.fish_1 = Fish("Swimmy")
        self.fish_2 = Fish("Goldie")
        self.fish_3 = Fish("Silverie")
    
        self.fish = [ self.fish_1, self.fish_2, self.fish_3]

        self.river_1 = River("Amazon", self.fish)
    
    def test_bear_has_name(self):
        self.assertEqual("Yogi", self.bear_1.name)
    
    def test_bear_roar(self):
        self.assertEqual("roar", self.bear_1.bear_roar())

    def test_food_count(self):
        self.assertEqual(0, self.bear_1.food_count())
    
    def test_bear_take_fish_from_river(self):
        self.bear_1.bear_take_fish_from_river(self.river_1)
        self.assertEqual(1, self.bear_1.food_count())
        self.assertTrue(TestRiver.test_lose_fish)