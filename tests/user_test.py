import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user_1 = User("Andrew High")
        self.user_2 = User("Fraser High")
        self.user_3 = User("Johnny Laing")

    def test_user_has_name(self):
        self.assertEqual("Andrew High", self.user_1.name)
