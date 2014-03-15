import unittest
from selenate import Selenate

class SelenateTest(unittest.TestCase):
    def test_start_without_server(self):
        message = ""
        try:
            driver = Selenate()
        except Exception as e:
            message = e.msg
        self.assertTrue(message)
        self.assertEqual(message, "Please start the selenium server")

