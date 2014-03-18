import unittest
from selenate import Selenate

class SelenateTest(unittest.TestCase):
    def test_start_without_server(self):
        message = ""
        try:
            browser = Selenate(server=None)
        except Exception as e:
            message = e.msg
        else:
            browser.quit()
        self.assertTrue(message)
        self.assertEqual(message, "Please start the selenium server")

    def test_quit_a_closed_browser(self):
        message = ""
        browser = Selenate()
        browser.get("http://www.github.com/wmak/selenate")
        browser.quit()
        try:
            browser.quit()
        except Exception as e:
            message = e.msg
        self.assertTrue(message)
        self.assertEqual(message, 
                "The browser died before you could complete that action")

    def test_readme_code(self):
        try:
            browser = Selenate() # start your browser
            browser.get("https://github.com/wmak/selenate") # go to this url
            browser.click(".mega-octicon") # click on this css element
            browser.quit()
        except:
            self.assertTrue(False)
