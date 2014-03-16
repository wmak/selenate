import unittest
from selenate import Selenate

class SelenateTest(unittest.TestCase):
    def test_start_without_server(self):
        message = ""
        try:
            driver = Selenate(server=None)
        except Exception as e:
            message = e.msg
        self.assertTrue(message)
        self.assertEqual(message, "Please start the selenium server")

    def test_quit_a_closed_browser(self):
        message = ""
        driver = Selenate()
        driver.get("http://www.github.com/wmak/Selenate")
        driver.quit()
        try:
            driver.quit()
        except Exception as e:
            message = e.msg
        self.assertTrue(message)
        self.assertEqual(message, 
                "The browser died before you could complete that action")
