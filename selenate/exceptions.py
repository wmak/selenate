class SelenateException(Exception):
    pass

class StartSeleniumError(SelenateException):
    def __init__(self):
        self.msg = "Please start the selenium server"
