import unittest
from selenate import Selenate

class SelenateTest(unittest.TestCase):
    def test_start(self):
        driver = Selenate()

