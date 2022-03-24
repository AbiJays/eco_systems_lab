import unittest
from src.river import River
from src.fish import Fish

class TestRiver(unittest.TestCase):
    def setUp(self):
        self.fish_1 = Fish("Swimmy")
        self.fish_2 = Fish("Goldie")
        self.fish_3 = Fish("Silverie")
    
        self.fish = [ self.fish_1, self.fish_2, self.fish_3]

        self.river_1 = River("Amazon", self.fish)
    
    def test_river_has_name(self):
        self.assertEqual("Amazon", self.river_1.name)
    
    def test_lose_fish(self):
        lost_fish = self.river_1.lose_fish(self.fish_1)
        self.assertEqual(2, len(self.fish))
        self.assertIsNotNone(lost_fish)
    
    
