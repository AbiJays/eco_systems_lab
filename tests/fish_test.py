import unittest

from src.fish import Fish

class TestFish(unittest.TestCase):
    def setUp(self):
        self.fish_1 = Fish("Swimmy")
        self.fish_2 = Fish("Goldie")
        self.fish_3 = Fish("Silverie")
    
    def test_fish_has_name(self):
        self.assertEqual("Swimmy", self.fish_1.name)
    
