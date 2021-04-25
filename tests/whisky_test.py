import unittest
from models.whisky import Whisky

class TestWhisky(unittest.TestCase):
    def setUp(self):
        self.whisky_1 = Whisky("Classic Laddie", "Single Malt", "Coastal")
        self.whisky_2 = Whisky("Famous Grouse", "Blended Whisky")
        self.whisky_3 = Whisky("Port Charlotte 10", "Single Malt", "Peated")

    def test_whisky_has_name(self):
        self.assertEqual("Famous Grouse", self.whisky_2.name)

    def test_whisky_has_type(self):
        self.assertEqual("Single Malt", self.whisky_3.type)

    def test_whisky_has_flavour_profile(self):
        self.assertEqual("Coastal", self.whisky_1.flavour_profile)