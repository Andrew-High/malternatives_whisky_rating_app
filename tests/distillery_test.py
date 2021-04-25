import unittest
from models.distillery import Distillery
from models.whisky import Whisky

class TestDistillery(unittest.TestCase):
    def setUp(self):
        self.distillery_1 = Distillery("Bruichladdich", "Islay", 1881, [whisky_1, whisky_3])
        self.distillery_2 = Distillery("Aberlour", "Speyside", 1879)
        self.whisky_1 = Whisky("Classic Laddie", "Single Malt", "Coastal")
        self.whisky_2 = Whisky("Famous Grouse", "Blended Whisky", "Cereal")
        self.whisky_3 = Whisky("Port Charlotte 10", "Single Malt", "Peated")

    def test_distillery_has_name(self):
        self.assertEqual("Bruichladdich", self.distillery_1.name)

    def test_distillery_has_one_whisky(self):
        self.assertEqual("Classic Laddie", self.distillery_1.whiskies[0])

    def test_distillery_has_multiple_whiskies(self):
        self.assertEqual(2, len(self.distillery_1.whiskies))

    def test_distillery_whisky_has_type(self):
        self.assertEqual("Single Malt", self.distillery_1.whiskies[0].type)